快速开始：

```bash
npx skills add mattpocock/skills --skill=to-spec
```

```bash
npx skills update to-spec
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec)

## 功能说明

`to-spec` 将当前对话和你的代码库理解转化为一份规范（你可能称此文档为 PRD），然后将其发布到你的问题追踪器。

它**不会**再次采访你。当你用到它的时候，对齐工作已经完成——`to-spec` 是对已知信息的综合整理，而非提出新一轮的问题。

## 何时使用

输入 `/to-spec` 来调用它——Agent 不会自己触发它。

当一个变更已经过充分讨论、领域语言已经确定，并且你希望在编写任何代码之前将这些共识记录成文时，使用它。如果*还没有*对齐，先进行深入访谈——此时应使用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。要将完成的规范拆分为 ticket，使用 [to-tickets](https://aihero.dev/skills-to-tickets)。

## 前置条件

`to-spec` 会发布到你的问题追踪器，因此 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须先为当前仓库配置好追踪器和分类标签。它会自行应用 `ready-for-agent` 标签——无需额外走一遍分类流程。

## 规范包含的内容

- **问题陈述**——什么出了问题或缺失了什么，以及为什么值得解决，使用项目自身的术语体系。
- **解决方案**——在实现细节之前，对修复方案的高层概述。
- **用户故事**——一系列详尽的、编号的具体行为要求，每个行为均可独立验证。
- **实现决策**——在对话中已经达成的选择，避免后续再被重新争论。
- **测试决策**——功能将在哪些接缝处进行测试，以及"完成"的定义。
- **范围外事项**——该变更明确*不*涵盖的内容，以保持 ticket 边界清晰。
- **补充说明**——其他值得记录但不适合归入上述各节的信息。

## 深度模块

在编写规范之前，`to-spec` 会先描绘功能将在哪些**接缝**处进行测试，并寻找**深度模块**的机会——在小型、稳定的接口背后隐藏大量功能。它优先选择已有接缝而非新建接缝，并尽可能选择最高层的接缝，理想情况下整个变更只需要一个接缝。

这对 Agent 化开发至关重要：良好的接口为测试提供了持久的锚点，使得底层代码可以变更而测试无需随之改动。

## 有效的标志

- 它开始编写规范，而不是再问你一轮新问题。
- 在撰写之前，它会与你确认接缝的选择，并尽可能少地提出接缝。
- 规范使用你项目的领域术语，而非通用的套话模板。

## 在系统中的位置

`to-spec` 是主构建链中的一个步骤：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

在计划和领域语言确定之后、将工作拆分为实现 ticket 之前使用它。它的关键邻近技能是 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，用于打磨上下文使规范更精确；以及 [to-tickets](https://aihero.dev/skills-to-tickets)，用于将规范转化为供 [implement](https://aihero.dev/skills-implement) 构建的一组 ticket。当你不确定哪个技能或流程适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
