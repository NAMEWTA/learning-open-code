# 标准任务单与全局上下文包

> 本文件是 **GCP 模板与字段填充规则的唯一来源**。goal-loop.md、teach-review.md 均引用此处，不另行维护副本。

## 目录

- [teach subagent 派发模板](#teach-subagent-派发模板)
- [全局上下文包（GCP）模板](#全局上下文包gcp模板)
- [标准任务单模板](#标准任务单模板)
- [Subagent 执行流程](#subagent-执行流程)
- [不同层级的任务单差异](#不同层级的任务单差异)

持久化路径规则见 [persistence.md](persistence.md)。派发前必须校验 `output_path`、`required_outputs` 和 `TEACH_ROOT` 合规。

**teach 执行硬约束**：派发 teach subagent 时，prompt 中必须包含显式指令——**Read 并激活 `.agents/skills/teach/SKILL.md`**，按其中教学规范生成 HTML 课程或参考文档。不得省略此路径引用。

每次从 Goal 队列取出一个目标后，主 Agent 按以下两步组装 subagent prompt：

1. **先生成全局上下文包（GCP）**——提供项目全局信息、进度状态、已生成内容的目录快照
2. **再填充标准任务单**——描述当前 goal 的具体要求

二者拼接后作为 subagent 的完整 prompt 派发。**一个 subagent prompt = GCP + 任务单，一个 subagent 只处理一个 goal。**

## teach subagent 派发模板

主 Agent 使用 Task 工具派发 teach subagent 时，prompt **必须**包含以下显式激活指令（不得改写路径、不得省略）：

```
【首要指令 — 必须执行】
在开始任何教学内容生成之前，你必须 Read 并激活 `.agents/skills/teach/SKILL.md`，
严格按其中教学规范执行。不得跳过此步骤，不得凭记忆或自行撰写替代。

{此处拼接 GCP 模板内容}

{此处拼接标准任务单模板内容}
```

修复轮次（`needs_fix`）重新派发时，同样必须包含上述首要指令。

## 全局上下文包（GCP）模板

**每次派发 subagent 必须前置此模板。** GCP 让 subagent 在无前置记忆的情况下也能了解项目全局、自主探查已生成内容。

```
═══════════════════════════════════════
全局上下文包 (GCP) — 由 teach-goal 编排器自动生成
═══════════════════════════════════════

【项目标识】
PROJECT_NAME: {项目名称}
PROJECT_ROOT: {目标仓库绝对路径}
TEACH_ROOT: teach/<path>/    ← 唯一合法持久化根目录，严禁写入 .agents/

【teach/<project>/ 当前目录树】
{list_dir teach/<project>/ 的完整输出}
↑ 你可以使用 list_dir、read_file 等工具自主探查以上目录中的任何文件

【整体进度】
已完成: {done_count} / {total_count} goals（{percentage}%）
最近完成的 5 个 goal:
  1. {goal_id} — {title} → {output_path}（主入口）
  2. ...
  3. ...
  4. ...
  5. ...

【当前 Goal 的依赖状态】
{depends_on 中每个依赖 goal 的完成状态}:
  - {dep_goal_id}: ✅ done → {dep_output_path}（可交叉引用）
  - {dep_goal_id}: ⏳ pending（尚未完成，但当前 goal 不依赖其结果）

【锚点参考】
L0 项目导览课: teach/<project>/00-overview/lessons/000N-<slug>.html（课程命名由模型自主决定）
L0 项目总览参考: teach/<project>/00-overview/reference/00-overview.html

【关联文档路径】
{以下路径如不存在则标注"尚未生成"}
父模块导览/总览 (L1): {parent_output_path}
同级垂直切片 (L2): {sibling_slice_paths}
同级 API 参考 (L3): {sibling_api_paths}
关联深度剖析 (L4): {related_deepdive_paths}

═══════════════════════════════════════
以下是本次任务单 — 你的唯一执行目标
═══════════════════════════════════════
```

### GCP 字段填充规则

| 字段 | 填充规则 |
|------|---------|
| PROJECT_NAME | 从用户输入或仓库名推断 |
| PROJECT_ROOT | 目标仓库的绝对路径 |
| TEACH_ROOT | 固定为 `teach/<path>/`，`<path>` 为 `.gitmodules` 逻辑项目路径。subagent 所有写入必须在此目录树下 |
| 目录树 | 使用 `list_dir` 工具获取 `teach/<project>/` 的完整输出，**不要裁剪**。subagent 据此可自主探查 |
| 整体进度 | 从 `_progress.json` 统计 status=done 的数量 |
| 最近完成 | 从 `_progress.json` 按 `completed_at` 倒序取前 5 个 status=done 的 goal |
| 依赖状态 | 遍历当前 goal 的 `depends_on`，查 `_progress.json` 中各依赖 goal 的 status 和 output_path |
| 锚点参考 | 固定路径，L0 导览课与总览参考始终在此位置 |
| 关联文档 | 从 `_progress.json` 筛选同 `parent` 的其他 goal 的 output_path，按 level 分类列出。尚未生成的标注"尚未生成" |

## 标准任务单模板

```
【教学生成任务单】
goal_id: {id}
层级: L0 / L1 / L2(垂直切片) / L3 / L4
标题: {title}
所属模块: {parent}
前置知识回顾: {对已完成的依赖 goal 的 2-3 句话概括，避免重复讲解。引用上方 GCP 中依赖状态所列的文档路径}
涉及源码:
  - {文件路径}:{起始行}-{结束行}   # 一句话说明这段代码的作用
  - ...
是否为垂直切片: {是/否}；若是，列出涉及的层级顺序（如：路由 → 中间件 → Service → DAO → 数据库）
目标读者水平: {TARGET_AUDIENCE}
输出语言: {OUTPUT_LANGUAGE}
持久化根目录: teach/<path>/    ← 所有产出必须在此目录树下
主题目录: {topic_dir}          ← 必须以 teach/ 开头，不得含 .agents/
主入口路径: {output_path}      ← 必须以 teach/ 开头，不得含 .agents/
必备产出 required_outputs:
  meta:
    - {topic_dir}/MISSION.md
    - {topic_dir}/RESOURCES.md
    - {topic_dir}/SNAPSHOT.md
  lessons:
    - {至少 1 个 lessons/000N-*.html；复杂主题拆成多节短课}
  reference:
    - {本层级要求的 reference/*.html；没有则填 []}
短课规则:
  - 每节 lesson 只讲一个学习目标，15 分钟内完成
  - 正文目标 800-1200 中文字，硬上限 1500 中文字
  - 最多 4 个主章节、3 个源码文件、3 个短代码片段；单个代码片段最多 35 行
  - 超限必须拆成同一主题目录下的多节 `lessons/000N-*.html`
---
【必须执行】Read 并激活 `.agents/skills/teach/SKILL.md`，严格按其中教学规范
（主题完成硬闸门、短课合约、HTML 课程格式、参考文档格式等）生成完整教学内容。
不要自行简化或另起一套格式。本次为批量生成模式，MISSION.md 使用自动生成的默认使命（不交互等待用户输入），但必须写成真实内容，不能保留 init_topic.sh 占位符。

**严禁将任何文件写入 .agents/ 目录。** 写入前确认所有产出路径以 teach/ 开头。

完成前必须执行：
1. 填写/更新 `MISSION.md`、`RESOURCES.md`
2. 生成 required_outputs 中的 lessons 与 reference
3. 运行 `.agents/skills/teach/scripts/generate_snapshot.py {topic_dir}` 更新 `SNAPSHOT.md`
4. 运行 `.agents/skills/teach/scripts/audit_topic.py {topic_dir}`，只有审计通过才能回报 success

完成后请回报：
1. 主入口路径（相对工作区根目录）
2. 产出摘要（2-3 句话）
3. created_files（本次创建/更新的所有文件）
4. lesson_manifest（每节 lesson 的路径、学习目标、估计时长）
5. topic_audit_passed: true
6. 新发现的、尚未覆盖的模块/函数/依赖（如有）
7. path_validated: true（确认所有路径以 teach/ 开头且不含 .agents/）
```

## 字段说明

| 字段 | 说明 | 示例 |
|------|------|------|
| `goal_id` | Goal 唯一标识 | `L2-auth-login-flow` |
| `层级` | L0 / L1 / L2(垂直切片) / L3 / L4 | `L2(垂直切片)` |
| `标题` | 中文简短标题 | `用户登录鉴权全链路` |
| `所属模块` | 父 goal 的 id，L0 填 `-` | `L1-auth-module` |
| `前置知识回顾` | 2-3 句概括已完成的依赖 goal 讲了什么 | `L1-auth-module 已讲解认证模块的三层架构(Controller→Service→DAO)及 JWT 配置` |
| `涉及源码` | 每行一个文件路径 + 行号范围 + 一句话说明 | `src/middleware/authGuard.ts:30-58 # JWT 验证与刷新逻辑` |
| `是否为垂直切片` | 是/否 | `是；层级顺序：路由 → 中间件 → Service → DAO → 数据库` |
| `目标读者水平` | 学习者背景描述 | `具备一定编程基础、希望从0到1精通该项目架构与实现细节的开发者` |
| `输出语言` | 教学文档输出语言 | `中文` |
| `持久化根目录` | 唯一合法写入根目录 | `teach/open-ai-agent/pi/` |
| `主题目录` | 当前 goal 所属 teach 主题目录，必须以 `teach/` 开头 | `teach/open-java/RuoYiVuePlus/slice-auth-login-flow/` |
| `主入口路径` | goal 的主入口文件，必须以 `teach/` 开头；不代表全部交付物 | `teach/open-java/RuoYiVuePlus/slice-auth-login-flow/lessons/000N-<slug>.html` |
| `required_outputs` | 元文件、lesson、reference 的完整交付清单 | 课程数量与命名由模型自主决定，如 `lessons: [0001-auth-overview.html, 0002-token-refresh.html]` |

## Subagent 执行流程

> **重要：本节描述的是 subagent 拿到 GCP + 任务单后的执行流程。主 Agent 不直接执行这些步骤。**

teach-goal 负责"喂料"（决定讲什么、给什么代码上下文、按什么顺序讲），教学内容的**具体写法完全交给 `.agents/skills/teach/SKILL.md` 决定**。这个决策由 subagent 执行。

subagent 拿到 GCP + 任务单后，执行以下步骤：

1. **Read 并激活 `.agents/skills/teach/SKILL.md`**：作为第一步，必须 Read 该文件并按其中流程执行。不得跳过或凭记忆替代。
2. **理解上下文**：阅读 GCP 了解项目全局、已有产出、依赖关系；阅读任务单了解当前 goal 的具体要求
3. **读取源码**：根据任务单中的 `涉及源码` 列表读取相关源文件，必要时使用 `list_dir`、`grep_search` 等工具自主探查更多上下文
4. **按 `.agents/skills/teach/SKILL.md` 生成内容**：将任务单内容和源码上下文传入 teach 工作流，明确告知本次为批量生成模式、MISSION.md 使用自动生成的默认使命（不交互等待用户输入），但必须写实并去除占位符
5. **拆成短课**：如果内容超过 `.agents/skills/teach/SKILL.md` 的短课合约，在同一主题目录下拆成多节 `lessons/000N-*.html`，把长表格/源码索引放进 `reference/`
6. **路径校验后写入**：确认所有产出路径以 `teach/` 开头、不含 `.agents/`，然后写入 required_outputs
7. **快照与主题审计**：运行 `generate_snapshot.py {topic_dir}`，再运行 `audit_topic.py {topic_dir}`；审计失败不得回报 success
8. **回报结果**：返回以下信息给主 Agent：
   - 是否成功生成主题交付物（含完整相对路径）
   - `path_validated: true/false`（写入前是否确认路径合规）
   - `topic_audit_passed: true/false`
   - `created_files` 与 `lesson_manifest`
   - 主题产出的摘要（2-3 句话）
   - 本次分析中新发现的、尚未覆盖的模块/函数/依赖（供主 Agent 生成新 goal）

> **重要：** teach subagent **不负责自我审查**。产出文件的质量审查由独立的 `teach-review` subagent 执行（见 [agent/teach-review.md](../agent/teach-review.md)）。主 Agent 在收到回报后会立即派发 teach-review。如果审查发现 Critical 问题，主 Agent 会将修复任务反馈给本 subagent——**修复时须重新 Read 并激活 `.agents/skills/teach/SKILL.md`**。

### Subagent 回报格式

```
【Subagent 回报】
goal_id: {id}
status: success / failed
topic_dir: {主题目录，必须以 teach/ 开头}
output_path: {主入口文件相对路径，必须以 teach/ 开头}
path_validated: true / false
topic_audit_passed: true / false
created_files:
  - {本次创建/更新的文件路径}
lesson_manifest:
  - path: {lessons/0001-*.html}
    objective: {这一节只解决什么学习目标}
    estimated_minutes: {<=15}
summary: {2-3 句话摘要}
new_discoveries:
  - {新发现的模块/函数/依赖的简短描述}
  - ...
audit_errors: {如审计失败，逐条列出 audit_topic.py 输出}
errors: {如失败，简述原因}
```

> **回报后的流程：** 主 Agent 收到此回报后 → 派发 teach-review subagent 审查产出 → 根据审查结论决定 goal 状态。如有 Critical 问题，可能要求本 subagent 修复后重新提交（最多 2 轮修复-审查循环）。

## 不同层级的任务单差异

### L0 项目总览

输出到独立 teach 主题 `teach/<project>/00-overview/`。必备产出：
- `lessons/` 下至少 1 节短课：项目导览短课，帮助学习者建立全局地图。课程数量与命名由模型根据项目规模自主决定。
- `reference/00-overview.html`：技术栈、目录、架构图、豁免清单等速查参考。

### L1 模块总览

输出到独立 teach 主题 `teach/<project>/module-<slug>/`。必备产出：
- `lessons/` 下至少 1 节短课：模块导览短课。课程数量与命名由模型根据模块复杂度自主决定。
- `reference/<slug>-overview.html`：模块职责、接口、分层、依赖速查。

### L2 垂直切片

输出到独立 teach 主题 `teach/<project>/slice-<slug>/`。至少 1 节短课；课程数量与命名由模型根据功能复杂度自主决定——模型综合源码文件数量、链路深度、逻辑复杂度和 L2 五要素覆盖需求，自行判断需要几节课、每节课聚焦什么角度。复杂链路必须在同一主题目录中拆成多节短课，不得生成巨型单页。
- `reference/<slug>-flow-map.html`：长源码索引或流程速查（可选）。

### L3 微观 API

输出到其父 L1 模块的 teach 主题 `teach/<project>/module-<slug>/`（与 L1 同目录）。产出文件为 `reference/<slug>-api.html`。注意：L3 不创建新的 teach 主题目录，而是复用 L1 已创建的 `module-<slug>/` 目录；如果该目录还没有 lesson，必须补至少 1 节短课（课程名称由模型自主决定），禁止 reference-only 主题。

### L4 深度剖析

输出到独立 teach 主题 `teach/<project>/deep-dive-<slug>/`。至少 1 节短课；课程数量与结构由模型根据主题复杂度自主决定。长表格、源码索引、伪代码索引写入 `reference/`。
