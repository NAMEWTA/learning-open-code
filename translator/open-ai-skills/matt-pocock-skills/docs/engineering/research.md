快速开始：

```bash
npx skills add mattpocock/skills --skill=research
```

```bash
npx skills update research
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/research)

## 功能说明

`research` 通过阅读掌握答案的源头资料来回答问题，并留下一份带引用的 Markdown 文件。它只基于**一手资料**工作 —— 官方文档、源代码、规范、第一方 API —— 而不是对它们的二手转述，因此它保存的东西可以追溯到权威来源，而不是摘要的摘要。

## 何时使用

输入 `/research`，或者当任务变成需要阅读资料的体力活时 Agent 会自动触发。

当下一步是*查明某事*时使用它 —— API 的行为是怎样的、规范到底说了什么、某个说法是否成立 —— 而你不想因为自己去做阅读而阻塞自己的主线工作。对于通过访谈而非阅读来打磨计划，使用 [grilling](https://aihero.dev/skills-grilling) ；对于用可丢弃的代码探索要构建什么，使用 [prototype](https://aihero.dev/skills-prototype)。

## 委托的体力活

其标志性特征是阅读工作作为**后台 Agent** 运行。你继续工作，它去执行任务，将每个说法追溯到它的一手资料，然后把一份带引用的 Markdown 文件放入仓库中存放此类笔记的地方。Research 是你委托出去的体力活，不是你外包出去的思考 —— 你拿回的是一份可以回应的文档，其资料来源附在后面。

## 在系统中的位置

一个随时可用的独立工具，为思考类 skill 提供输入：它生成的文件是 grilling、planning 或 design 的基础素材，因此它位于 [grilling](https://aihero.dev/skills-grilling) 和 [to-prd](https://aihero.dev/skills-to-prd) 等工作流程的上游，而非在构建链中。要查看完整地图，参见 [ask-matt](https://aihero.dev/skills-ask-matt)。
