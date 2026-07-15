# 持久化根目录规则

> 本文件是 **teach-goal 持久化规则的唯一来源**。SKILL.md、goal-loop.md、task-order.md、output-structure.md、coverage-checklist.md、teach-review.md 均引用此处，不另行维护副本。

## 目录

- [TEACH_ROOT 定义](#teach_root-定义)
- [禁止目录清单](#禁止目录清单)
- [路径公式](#路径公式)
- [init_topic.sh 正确调用](#init_topicsh-正确调用)
- [路径校验](#路径校验)
- [误放检测](#误放检测)

## TEACH_ROOT 定义

教学持久化的**唯一合法根目录**是工作区根目录下的 `teach/<path>/`：

```
{工作区根目录}/teach/<path>/
```

- `{工作区根目录}`：包含 `.gitmodules` 的 monorepo 根目录（**不是** `.agents/`）
- `<path>`：来自 `.gitmodules` 的逻辑项目路径（如 `open-ai-agent/pi`、`open-java/RuoYiVuePlus`）

**TEACH_ROOT** = `teach/<path>/`（相对工作区根目录）

## 禁止目录清单

以下路径**严禁**写入任何教学持久化内容（MISSION.md、lessons/、reference/、_progress.json 等）：

| 禁止路径 | 常见误用原因 |
|---------|-------------|
| `.agents/` | 与 skill 目录混淆，或 init_topic.sh 工作区根目录计算错误 |
| `.agents/teach/` | init_topic.sh 将 `.agents/` 当作工作区根目录 |
| `.agents/<项目名>/` | 省略 `teach/` 前缀，直接用项目名建目录 |
| 任何不以 `teach/` 开头的相对路径 | 任务单 output_path 填写错误 |
| 源项目子模块目录（`open-ai-agent/pi/` 等） | 与教学产出目录混淆 |

`.agents/skills/teach/` 是 **skill 定义目录**（SKILL.md、脚本），不是教学产出目录。

## 路径公式

| 层级 | 路径模式 | 示例 |
|------|---------|------|
| 项目级 | `teach/<path>/` | `teach/open-ai-agent/pi/` |
| 进度台账 | `teach/<path>/_progress.json` | `teach/open-ai-agent/pi/_progress.json` |
| Wiki 导航 | `teach/<path>/00-index.md` | `teach/open-ai-agent/pi/00-index.md` |
| 项目索引 | `teach/<path>/index.md` | `teach/open-ai-agent/pi/index.md` |
| 主题级 | `teach/<path>/<topic>/` | `teach/open-ai-agent/pi/00-overview/` |
| L0 主入口 | `teach/<path>/00-overview/lessons/000N-<slug>.html` | 至少 1 节，命名由模型自主决定 |
| L0 参考 | `teach/<path>/00-overview/reference/00-overview.html` | — |
| L1 主入口 | `teach/<path>/module-<slug>/lessons/000N-<slug>.html` | 至少 1 节，命名由模型自主决定 |
| L1 参考 | `teach/<path>/module-<slug>/reference/<slug>-overview.html` | — |
| L2 主入口 | `teach/<path>/slice-<slug>/lessons/000N-<slug>.html` | 至少 1 节，命名由模型自主决定 |
| L3 参考 | `teach/<path>/module-<slug>/reference/<slug>-api.html` | — |
| L4 主入口 | `teach/<path>/deep-dive-<slug>/lessons/000N-<slug>.html` | 至少 1 节，命名由模型自主决定 |

**任务单中的 `output_path` 只是主入口路径**，完整交付物以 `required_outputs` 为准。subagent 不得自行改目录；若需要拆成多节短课，必须写入同一主题目录下的 `lessons/000N-*.html`，并在回报中列出 `lesson_manifest`。

## init_topic.sh 正确调用

```bash
bash .agents/skills/teach/scripts/init_topic.sh teach/<path> <topic-slug>
```

示例：

```bash
bash .agents/skills/teach/scripts/init_topic.sh teach/open-ai-agent/pi 00-overview
bash .agents/skills/teach/scripts/init_topic.sh teach/open-ai-desktop/openhanako module-core
```

**第一个参数必须以 `teach/` 开头**，否则脚本会报错退出。脚本会打印目标绝对路径，主 Agent 必须确认路径落在工作区根目录的 `teach/` 下，而非 `.agents/` 下。

## 路径校验

主 Agent 和 subagent 在写入前后执行以下校验：

```
function validate_output_path(path):
    if not path.startswith("teach/"):
        return FAIL("路径必须以 teach/ 开头")
    if ".agents/" in path or path.startswith(".agents"):
        return FAIL("严禁写入 .agents/ 目录")
    if path contains "..":
        return FAIL("路径不得包含 ..")
    return OK
```

**校验时机**：

1. **派发前**：主 Agent 组装任务单时，校验 `output_path`、`required_outputs` 和 `TEACH_ROOT`
2. **写入前**：subagent 写入任何文件前再次确认路径合规
3. **回报后**：主 Agent 收集 subagent 回报后，验证 `output_path` 以 `teach/` 开头且文件实际存在
4. **主题审计前**：主 Agent 运行 `.agents/skills/teach/scripts/audit_topic.py <topic-path>`，确保元文件、lessons 和短课规则达标
5. **标记 done 前**：路径校验或主题审计失败 → goal 标记 `needs_fix`，不进入 done
6. **审查时**：teach-review 将路径违规、reference-only 主题、占位元文件、巨型 lesson 标为 Critical

## 误放检测

每轮 Goal Loop 开始前，主 Agent 扫描 `.agents/` 目录，检查是否存在教学产出标记文件：

- `MISSION.md`、`SNAPSHOT.md`、`RESOURCES.md`
- `lessons/`、`reference/`、`learning-records/` 目录
- `_progress.json`、`00-index.md`

若发现上述文件/目录存在于 `.agents/` 下（排除 `.agents/skills/` 内的 skill 定义文件），**立即告警并中止循环**，提示将内容迁移到正确的 `teach/<path>/` 后再继续。
