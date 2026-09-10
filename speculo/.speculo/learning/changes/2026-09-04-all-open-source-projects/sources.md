# 学习来源与证据范围：Sub2API Plus

## 项目事实

| 来源 | 用途 | 当前状态 |
| --- | --- | --- |
| `.gitmodules` | 确认 `open-ai-agent/sub2api-plus` 的路径、远程 URL 和跟踪分支 | 已读取 |
| `open-ai-agent/sub2api-plus/README.md`、`README_CN.md` | 项目定位、功能、Provider 支持、部署方式和合规提示 | 已读取 |
| `open-ai-agent/sub2api-plus/backend/` | Go 后端入口、API、领域逻辑、数据访问和测试 | 待按模块逐步核对 |
| `open-ai-agent/sub2api-plus/frontend/` | 管理界面、路由、状态和 API 调用 | 待按模块逐步核对 |
| `open-ai-agent/sub2api-plus/deploy/`、`Dockerfile` | 进程启动、容器构建、反向代理和运行时边界 | 已完成初筛，待深入核对 |
| `open-ai-agent/sub2api-plus/docs/`、`AGENTS.md` | 协议、支付、安全、发布和贡献约束 | 待按学习目标精确引用 |

## 权威外部来源

- 各项目 `.gitmodules` 中登记的官方仓库 URL：用于核对项目定位、版本说明和官方架构文档。
- 项目官方文档、发布说明和源码内规范：使用具体结论时再逐条验证。

## 横向比较维度

后续计划围绕入口与生命周期、Provider/协议适配、账户调度与故障转移、认证/配额/计费、状态与数据模型、持久化与并发、错误处理、测试策略、部署形态、安全边界和可扩展性展开。比较结论必须回链到项目源码或可靠文档。

## 当前未知

- 学习者对 Sub2API Plus 的已有掌握程度尚未通过基线验证；
- 项目内部模块和垂直链路的优先顺序需要结合基线和每次可用时间确定；
- 部分项目可能缺少完整测试或文档，届时在对应来源记录中标明证据缺口，不用推测补齐。
