快速开始：

```bash
npx skills add mattpocock/skills --skill=grilling
```

```bash
npx skills update grilling
```

[源代码](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)

## 功能说明

`grilling` 是在你构建之前对计划或设计进行压力测试的不留情面的面试。它沿着设计树逐分支深入，逐一解决决策之间的依赖关系，直到你和 Agent 达成共识。

它每次只问**一个问题**并等待你的回答，然后再问下一个——绝不会批量提问，那会让人无所适从。每个问题都附带 Agent 自己的推荐答案，而任何代码库能够解答的问题，它都会自行探索而不是来问你。在你确认已达成共识之前，它不会开始执行计划。

## 何时使用

输入 `/grilling`，或者当任务适合时 Agent 会自动使用它——这是底层原语，不只是用户专属入口。

当你感觉某个计划或设计还有薄弱环节、希望在写代码之前让它们暴露出来时，就是使用它的时机。在实践中，你通常是通过它的两个封装器来调用它，而不是直接按名称调用：进行普通面试会话使用 [grill-me](https://aihero.dev/skills-grill-me)；希望会话过程中同时生成 ADR 和术语表，则使用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。

## 设计树

心智模型是一棵**设计树**：每个计划都会分支为若干决策，而决策之间又相互依赖。`grilling` 一次只深入树中的一个节点，因此早期的回答可能会重塑后续问题的走向。这就是问题一个接一个按依赖顺序出现的原因——并行倾泻大量问题会丢失那种使面试最终收敛于共识的结构。

## 刻意抽离

`grilling` 是面试技术的**单一事实来源**，被抽离为一个由模型自动调用的**原语**，这样每个需要面试的技能都可以使用它，而不用各自重新发明一套。[grill-me](https://aihero.dev/skills-grill-me) 和 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 是它的两个用户调用型入口，但 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 和 [triage](https://aihero.dev/skills-triage) 也会借助它来对自己的决策进行压力测试。

将这项技术集中在一个地方，意味着当你只想要面试本身——不需要其封装器附加的 ADR 撰写或工单整理——你也可以直接使用它。

## 在系统中的位置

`grilling` 是主构建链路之下的面试**原语**：[grill-with-docs](https://aihero.dev/skills-grill-with-docs) 在 [to-spec](https://aihero.dev/skills-to-spec) 撰写规范之前运行它来打磨上下文。当你不确定哪个入口适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
