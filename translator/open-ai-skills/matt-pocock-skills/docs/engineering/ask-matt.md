快速开始：

```bash
npx skills add mattpocock/skills --skill=ask-matt
```

```bash
npx skills update ask-matt
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt)

## 功能说明

`ask-matt` 是本仓库中所有 skill 的路由器。你描述自己面临的情况，它告诉你适合使用哪个 skill 或流程，以及按什么顺序执行它们。

它**本身不做任何实际工作**。它不会质询、不会写规格说明、也不会修复任何问题——它只负责导航引导。它主要为**用户调用的** skill 服务：没有机制会替你调用这些 skill，所以*你*必须记住它们的存在，而 `ask-matt` 就是你外包这份记忆的地方。它同样能指引你找到那些按名称调用的模型驱动 skill——`/tdd`、`/diagnosing-bugs`、`/prototype`、`/code-review`，以及两个词汇参考 skill：`/domain-modeling` 和 `/codebase-design`。它回答"用哪个、什么时候用"，然后将你交接给真正干活的 skill。

## 何时使用

输入 `/ask-matt` 来调用它——Agent 不会自行调用此 skill。

当你不确定某个情况该用哪个 skill 或流程时使用它：你有了一个想法但不知道从哪里开始；手头一堆 bug 报告，不清楚是否属于 `/triage` 的范畴；或者两个 skill 看起来可以互换，你分不清它们。如果你已经知道自己要用的 skill，跳过路由器直接调用它即可。

## 流程，而非单个 skill

`ask-matt` 给你的核心理念是**流程**——一条*贯穿*各个 skill 的路径，而非单个 skill。大多数工作沿着一条**主流程**推进（想法 → 交付：grill → spec → tickets → implement → review），两条**入口通道**汇入主流程（一条是面向外来 bug 和需求的 triage 通道；一条是生成改进想法的代码健康通道），其余所有 skill 都是**独立**使用的，按需取用。提出问题，你会被放到正确的流程、正确的步骤上——而不仅仅是拿到一个工具。

## 在系统中的位置

`ask-matt` 是**路由器**——覆盖整套 skill 的独立地图。它是所有其他文档页面反向链接的节点，参见 [ask-matt](https://aihero.dev/skills-ask-matt)，因此它不处于任何*链条之中*，而是*指向*每一条链条。从这里出发，你最常到达的是 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)（主流程的起点），或 [triage](https://aihero.dev/skills-triage)（处理非自主创建工作的入口通道）。当路由器自身的示意图也过时时，它的 [Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt) 就是记录中的权威地图。
