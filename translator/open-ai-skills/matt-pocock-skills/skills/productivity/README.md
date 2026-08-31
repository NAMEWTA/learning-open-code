# 生产力

通用工作流工具，不限于编码。

## 用户调用

只能由用户输入来访问（Claude Code：`disable-model-invocation: true`；Codex：`agents/openai.yaml` 中的 `policy.allow_implicit_invocation: false`）。

- **[grill-me](./grill-me/SKILL.md)** — 接受关于计划或设计的 relentless 访谈，直到设计树的每个分支都被解决。
- **[handoff](./handoff/SKILL.md)** — 将当前对话压缩为交接文档，以便另一个 agent 可以继续工作。
- **[teach](./teach/SKILL.md)** — 在多个会话中向用户教授新 skill 或概念，使用当前目录作为有状态的教学工作区。
- **[to-questionnaire](./to-questionnaire/SKILL.md)** — 把一个你无法独立回答的决策，转化为一份交给唯一能回答之人的 Markdown 问卷 —— 异步填写，或在会议中一起完成。
- **[wait-what](./wait-what/SKILL.md)** — 消息没说到点的那一刻就触发它。agent 会带着你缺失的上下文、用简单的语言、使用你的 `CONTEXT.md` 词汇表重新阐述。

## 模型调用

模型或用户均可访问（丰富的触发措辞使模型能够使用它们）。

- **[grilling](./grilling/SKILL.md)** — relentlessly 访谈用户关于计划、决策或想法，直到设计树的每个分支都被解决。
- **[writing-for-agents](./writing-for-agents/SKILL.md)** — 为 agent 撰写文档：skills、AGENTS.md/CLAUDE.md，以及任何 agent 通过指针到达的文档。
