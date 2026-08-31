# 交接：sub2api-plus 提示词审计记录排查

## 当前目标

用户希望让 `open-ai-agent/sub2api-plus/` 记录所有经过中转且能够成功提取的用户提示词，主要关心“用户问了什么”。当前最新问题是：提示词审计事件页显示“没有事件”，但配置页运行概览出现约 875 条，用户想知道原因以及数据实际写入数据库的什么位置。

本轮只进行了只读诊断与教学文档生成，没有修改 `open-ai-agent/sub2api-plus/` 源码，也没有连接到用户实际部署环境。

## 已确认结论

1. 运行概览中的数字不等于事件数。页面可能显示 Guard `总计`、队列 `done` 或 `累计处理`；它们分别表示扫描次数、完成任务数或当前进程启动后的成功处理数。
2. PostgreSQL 使用两张独立表：
   - `prompt_audit_jobs`：每个审计任务及其状态、脱敏预览、Hash、身份和入口元数据。
   - `prompt_audit_events`：事件页的数据源；完整未脱敏提示词存放在 `full_prompt`。
3. 安全结果只有在 `store_pass_events=true` 时才插入 `prompt_audit_events`。`flag` 和 `critical` 风险事件始终保存。
4. 因此，若 875 个任务为 `done`、事件表为 0，最可能是这些任务处理时“保存安全事件”未生效。开启该开关不会回填旧任务。
5. 异步任务完成后，Redis 临时提示词 payload 会被删除；未生成事件的旧任务只剩 `redacted_preview` 等元数据，完整提示词通常无法恢复。
6. 事件页查询只读取 `prompt_audit_events`，并受当前筛选条件约束。若数据库已有事件但页面为空，先清空筛选，再核对当前管理端连接的是否是同一个部署实例和数据库。
7. 普通业务模型响应不由 Prompt Audit 保存。当前功能只保存已适配协议中成功提取的用户提示词，并排除 system/developer 指令、模型回复、reasoning、工具定义、参数和结果。

## 源码证据

- 数据表：`open-ai-agent/sub2api-plus/backend/migrations/181_prompt_audit.sql`
- 完整提示词列：`open-ai-agent/sub2api-plus/backend/migrations/182_prompt_audit_full_prompt.sql`
- 安全事件保存条件及事件插入：`open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_repository.go`
- Worker 处理、Redis payload 删除和内存处理计数：`open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_worker.go`
- 运行概览数据组装：`open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_service.go`
- 事件列表仅查询事件表：`open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_event_repository.go`
- 前端指标展示：`open-ai-agent/sub2api-plus/frontend/src/features/prompt-audit/components/RuntimeOverview.vue`
- 内容提取边界：`open-ai-agent/sub2api-plus/docs/SECURITY_AUDIT_CONTENT_COVERAGE.md`

## 部署数据库检查

本机执行 `docker ps` 未发现运行中的 sub2api-plus/PostgreSQL 容器，因此必须在用户实际部署服务器检查。标准 Compose 的 PostgreSQL 容器名是 `sub2api-postgres`，默认数据库和用户均为 `sub2api`，数据卷挂载到容器内 `/var/lib/postgresql/data`。

进入数据库：

```bash
docker exec -it sub2api-postgres sh -lc \
  'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'
```

核心 SQL：

```sql
SELECT status, COUNT(*)
FROM prompt_audit_jobs
GROUP BY status
ORDER BY status;

SELECT
    COUNT(*) AS event_total,
    COUNT(*) FILTER (WHERE decision = 'pass') AS pass_events,
    COUNT(*) FILTER (WHERE decision = 'flag') AS flag_events,
    COUNT(*) FILTER (WHERE decision = 'critical') AS critical_events
FROM prompt_audit_events;

SELECT COUNT(*) AS done_without_event
FROM prompt_audit_jobs j
LEFT JOIN prompt_audit_events e ON e.job_id = j.id
WHERE j.status = 'done' AND e.id IS NULL;

SELECT
    value::jsonb ->> 'enabled' AS enabled,
    value::jsonb ->> 'store_pass_events' AS store_pass_events,
    value::jsonb ->> 'config_version' AS config_version
FROM settings
WHERE key = 'prompt_audit_config';
```

查看最新完整提示词：

```sql
SELECT id, created_at, decision, request_id,
       LEFT(full_prompt, 500) AS prompt
FROM prompt_audit_events
ORDER BY id DESC
LIMIT 20;
```

如果没有事件，可查看任务脱敏摘要：

```sql
SELECT id, created_at, status, request_id, model,
       prompt_length, redacted_preview, last_error_code
FROM prompt_audit_jobs
ORDER BY id DESC
LIMIT 20;
```

## 建议的下一步

1. 先让用户确认“875”旁边的准确标签，或提供运行概览截图；不要把这个数字直接当成事件总数。
2. 在实际服务器执行上述四组 SQL，优先比较 `done`、`event_total` 和 `done_without_event`。
3. 管理端确认“保存安全事件”已开启并点击保存，且“生效 / 期望版本”一致。
4. 清空事件页全部筛选条件。
5. 发送一条全新、带唯一标记的提示词，例如 `AUDIT_NEW_TEST_20260829 请只回复 OK`，等待数秒后刷新事件页并再次查询事件表。
6. 若新请求仍无事件：检查运行态的数据库、Redis、Guard 节点健康状态，以及 `failed`、`last_error_code`、提取成功和丢弃计数。
7. 若数据库存在事件但 UI 为空：检查筛选条件、管理端 API 请求返回值，以及管理端与数据库是否属于同一部署实例。

## 已有产物

- 操作短课：`teach/open-ai-agent/sub2api-plus/prompt-audit-operations/lessons/0001-configure-prompt-audit.html`
- 字段与排障清单：`teach/open-ai-agent/sub2api-plus/prompt-audit-operations/reference/prompt-audit-checklist.html`
- 教学主题快照：`teach/open-ai-agent/sub2api-plus/prompt-audit-operations/SNAPSHOT.md`
- SpecDev change：`speculo/.speculo/specdev/changes/2026-08-28-sub2api-request-response-logs/`
- ELI5 工件：`speculo/.speculo/specdev/changes/2026-08-28-sub2api-request-response-logs/01_sub2api请求响应日志.md`
- Change 状态：`speculo/.speculo/specdev/changes/2026-08-28-sub2api-request-response-logs/.status.json`

该 change 当前为 `active`，`current_work=null`，只运行过 `specdev/eli5`。没有生成 `source.md` 或 `triage.md`，因此无对应文件可引用；当前 owning 工件为上述 ELI5 文档。实现提交、本地集成和清理权限均为 `not-authorized`，没有远程 `external_action`。

## 工作区注意事项

工作区存在大量与本任务无关的已修改、已暂存、新增和删除内容，其中包括 Speculo 静态资产替换、多个子模块、翻译目录和其他教学产物。新 agent 必须保留这些用户改动，不得执行 reset、checkout 或批量清理，也不要同步根仓 gitlink，除非用户明确授权。

`open-ai-agent/sub2api-plus/` 当前子模块提交为 `e5b84a4d2e0b198619bb992bfadac932f12f8825`，根仓中该子模块为新增 gitlink 状态；本轮没有改动其内部文件。

## 建议 skills

- `teach`：当用户希望继续以操作课、截图解读或逐步排障方式学习时使用，并增量更新现有教学主题。
- 当前纯数据库诊断不需要额外 skill；若用户要求修改实现，再按 SpecDev change 状态进入相应 Work，并先取得必要授权。

## 安全边界

- 不要在对话或交接文档中输出 PostgreSQL 密码、Guard API Key、用户完整提示词或其他个人信息。
- 查询完整提示词时只在受控管理员终端操作；示例使用 `LEFT(full_prompt, 500)` 限制输出。
- 不要直接编辑 PostgreSQL 数据卷文件，应通过 SQL 查询和管理端删除接口操作。
