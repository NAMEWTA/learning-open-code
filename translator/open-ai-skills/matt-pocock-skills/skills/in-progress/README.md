# 开发中

Beta 版。这些 skill 是有意公开的 —— 试试它们，告诉我哪里坏了。在毕业到稳定分类之前，它们被排除在插件和顶层 README 之外，它们没有文档页面，并且可以随时变更或消失而不另行通知。

插件不会提供这些。直接安装其中一个：

```bash
npx skills@latest add mattpocock/skills --skill=<name>
```

- **[loop-me](./loop-me/SKILL.md)** — 在多个会话中把自己访谈成可实施的工作流规范，使用当前目录作为有状态的工作区。用户调用。
- **[writing-beats](./writing-beats/SKILL.md)** — 将文章塑造成一段节拍的旅程，选择你自己的冒险风格。选择一个起始节拍，只写那个节拍，然后转向下一个，直到文章达到自然结束。
- **[writing-fragments](./writing-fragments/SKILL.md)** — 挖掘式访谈会话，挖掘您的碎片——异质的写作素材——并将其追加到单个文档中，作为未来文章的原始材料。
- **[writing-shape](./writing-shape/SKILL.md)** — 获取原始材料的 markdown 文件，逐段塑造成文章，在每一步争论格式选择。
- **[claude-handoff](./claude-handoff/SKILL.md)** — 将当前对话移交给一个新的后台 agent，该 agent 通过 `claude --bg` 种子化的交接摘要立即接手工作。用户调用。
- **[setup-ts-deep-modules](./setup-ts-deep-modules/SKILL.md)** — 将 dependency-cruiser 接入 TypeScript 仓库，使每个包都是深层模块 —— 实现隐藏在子文件夹中，只能通过其入口文件访问，测试通过入口点进行。用户调用。
