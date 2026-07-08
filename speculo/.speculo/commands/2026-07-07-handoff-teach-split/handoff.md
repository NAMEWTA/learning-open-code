# Handoff

## 目标

将 teach-goal 生成的单文件巨无霸 L2/L4 课程（1000-1600行）拆分为符合 `teach/SKILL.md` 规范的多章节短课程序列（每课 170-290 行），与 RuoYiVuePlus `ai-integration` 格式对齐。

**用户下一步重点：继续对 hello-halo（8 个 L2）和 pi（6 个 L2 + 4 个 L4）执行同样的拆分。强调「拆分」——不是重新生成内容，而是将已有的源码分析、时序图、异常路径重新组织为编号递进章节。**

## 已完成

### openhanako 试点拆分 — 11 个 topic → 52 课，全部完成 ✅

| # | Topic | 类型 | 拆分 | 状态 |
|---|-------|------|------|------|
| 1 | sandbox-exec-flow | L2 | 1→5课 (1157行) | ✅ |
| 2 | plugin-lifecycle-flow | L2 | 1→5课 (1125行) | ✅ |
| 3 | agent-conversation-flow | L2 | 1→5课 (1150行) | ✅ |
| 4 | bridge-message-flow | L2 | 1→5课 (1092行) | ✅ |
| 5 | memory-compile-flow | L2 | 1→5课 (1062行) | ✅ |
| 6 | desk-automation-flow | L2 | 1→4课 (783行) | ✅ |
| 7 | first-run-onboarding-flow | L2 | 1→5课 (1083行) | ✅ |
| 8 | sandbox-architecture | L4 | 1→5课 (1125行) | ✅ |
| 9 | memory-conveyor | L4 | 1→5课 (1261行) | ✅ |
| 10 | plugin-sdk-architecture | L4 | 1→5课 (912行) | ✅ |
| 11 | session-coordinator | L4 | 1→4课 (744行) | ✅ |

**关键文件路径（参考格式）：**
- 参考格式源：`teach/open-java/RuoYiVuePlus/ai-integration/lessons/0001.html`（216行，CSS/测验/导航模板）
- 拆分示例：`teach/open-ai-desktop/openhanako/slice-sandbox-exec-flow/lessons/0001.html`~`0005.html`

**拆分规范（每课必须包含）：**
- `.mission` — 使命提醒块
- `.step` + `.num` + `.where` — 步骤引导
- `<pre><code>` — 深色背景真实代码片段
- `.quiz` + 4 选项 + `<details>` 答案 — 检索练习
- `.nav` — 前后课程序列导航
- `.reminder` — "有疑问？向 Agent 追问"
- `.cite` — 一手资料推荐
- CSS 与 RuoYiVuePlus `0001.html` 完全一致（字体、颜色、间距、响应式）
- 旧单文件 HTML 拆分后必须删除

**拆分原则：**
- 按「认知层级递进」组织：全景认知 → 逐层深入 → 异常路径 → 综合测验
- 每课一个核心主题，内聚且独立
- 第 N 课为终章综合测验，覆盖全部前置课程
- 测验题必须有 4 个选项 + 详细解析

### 更早完成的工作

- hello-halo: 13 L1 + 8 L2 全部生成完毕
- openhanako: 10 L1 + 7 L2 + 4 L4 全部生成完毕
- pi: 20/20 已完成（原有）
- hermes-agen: 24/24 已完成（原有）

## 未完成

### hello-halo — 8 个 L2 待拆分

| Topic | 源文件 | 大小 | 建议拆分 |
|-------|--------|------|---------|
| agent-conversation | `slice-agent-conversation/lessons/agent-conversation.html` | 1060行 | 5课 |
| digital-human-lifecycle | `slice-digital-human-lifecycle/lessons/digital-human-lifecycle.html` | 1020行 | 5课 |
| browser-action-exec | `slice-browser-action-exec/lessons/browser-action-exec.html` | 769行 | 4课 |
| remote-access-connect | `slice-remote-access-connect/lessons/remote-access-connect.html` | 1213行 | 5课 |
| mcp-tool-register | `slice-mcp-tool-register/lessons/mcp-tool-register.html` | ~900行 | 4课 |
| skill-install | `slice-skill-install/lessons/skill-install.html` | ~800行 | 4课 |
| openai-compat-proxy | `slice-openai-compat-proxy/lessons/openai-compat-proxy.html` | 1135行 | 5课 |
| artifact-preview | `slice-artifact-preview/lessons/artifact-preview.html` | 1135行 | 5课 |

路径前缀：`teach/open-ai-desktop/hello-halo/`

### pi — 6 个 L2 + 4 个 L4 待拆分

L2（路径前缀 `teach/open-ai-agent/pi/`）：

| Topic | 源文件 | 建议拆分 |
|-------|--------|---------|
| agent-session-flow | `slice-agent-session-flow/lessons/agent-session-flow.html` | 5课 |
| cli-startup-flow | `slice-cli-startup-flow/lessons/cli-startup-flow.html` | 4课 |
| context-compaction-flow | `slice-context-compaction-flow/lessons/context-compaction-flow.html` | 4课 |
| tui-render-cycle | `slice-tui-render-cycle/lessons/tui-render-cycle.html` | 4课 |
| oauth-auth-flow | `slice-oauth-auth-flow/lessons/oauth-auth-flow.html` | 4课 |
| rpc-orchestration | `slice-rpc-orchestration/lessons/rpc-orchestration.html` | 4课 |

L4（路径前缀 `teach/open-ai-agent/pi/`）：

| Topic | 源文件 | 建议拆分 |
|-------|--------|---------|
| compat-unification | `deep-dive-compat-unification/lessons/compat-unification.html` | 4课 |
| agent-loop-double | `deep-dive-agent-loop-double/lessons/agent-loop-double.html` | 5课 |
| diff-rendering | `deep-dive-diff-rendering/lessons/diff-rendering.html` | 4课 |
| agent-session-arch | `deep-dive-agent-session-arch/lessons/agent-session-arch.html` | 5课 |

### 总计剩余

- hello-halo: 8 个 L2 → 预计 ~37 课
- pi: 6 个 L2 + 4 个 L4 → 预计 ~43 课
- **合计：18 个 topic → 预计 ~80 课**

## 验证

- 所有 openhanako 拆分文件已写入对应 `lessons/` 目录，旧单文件已删除
- 每课文件通过 wc -l 验证行数在 170-290 范围
- CSS 一致性已与 RuoYiVuePlus `0001.html` 对比确认
- hello-halo 和 pi 的源文件尚未验证——需在拆分前逐文件确认存在且内容非空

## 推荐技能

下一个 agent 必须按顺序读取和激活：

1. `.agents/skills/teach/SKILL.md` — **教学规范（课程格式、章节结构、测验要求、CSS 参考）**
2. `.agents/skills/teach-goal/SKILL.md` — 了解 teach-goal 框架和目标体系
3. `.agents/skills/teach-goal/references/output-structure.md` — 了解 L0-L4 层级路径规范
4. 参考模板：`teach/open-java/RuoYiVuePlus/ai-integration/lessons/0001.html` — CSS + 测验 + 导航格式
5. 拆分样例：`teach/open-ai-desktop/openhanako/slice-sandbox-exec-flow/lessons/0001.html` — 已完成拆分的参考

## 摘要

1. **openhanako 试点完成**：7 个 L2 + 4 个 L4 = 11 个 topic，全部拆分为编号多课程序列（`0001.html`~`000N.html`），总计 52 课，每课 170-290 行
2. **拆分核心规范**：CSS 与 RuoYiVuePlus `0001.html` 一致，每课含使命提醒、步骤引导、真实代码、4 选项测验、前后导航、追问题醒，旧单文件拆分后删除
3. **hello-halo 待拆分**：8 个 L2 垂直切片（agent-conversation、digital-human-lifecycle、browser-action-exec、remote-access-connect、mcp-tool-register、skill-install、openai-compat-proxy、artifact-preview），预计 37 课
4. **pi 待拆分**：6 个 L2 + 4 个 L4 = 10 个 topic（agent-session-flow、cli-startup-flow、context-compaction-flow、tui-render-cycle、oauth-auth-flow、rpc-orchestration、compat-unification、agent-loop-double、diff-rendering、agent-session-arch），预计 43 课
5. **执行方式**：每 2-3 个 topic 可合并为一个 Agent 派发，参考已完成的拆分样例格式，保持每课 200-290 行、每课含 4 题测验、CSS 与 RuoYiVuePlus 一致
