快速开始：

```bash
npx skills add mattpocock/skills --skill=codebase-design
```

```bash
npx skills update codebase-design
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)

## 功能说明

`codebase-design` 为你提供一套共享的、精确的词汇，用于设计**深层模块**——大量行为隐藏在小接口之后，置于清晰的接缝处，可通过该接口进行测试。

它是一种**语言，而非流程**。它不会重构你的代码或给你一套重构计划——它只是固定词语（module、interface、depth、seam、adapter、leverage、locality），让每一次设计对话和每一个涉及设计的 skill 都以同样的方式表达。统一的语言就是全部意义所在；"component"、"service"、"API"和"boundary"这些词被刻意禁用，因为它们会模糊那些真正重要的区分。

## 何时使用

输入 `/codebase-design`，或在任务合适时 Agent 会自动调用它。

当你正在设计或改进模块的接口、寻找深化机会、决定接缝应该设置在哪里，或让代码更易于测试和 AI 导航时使用此 skill。其他 skill 在需要深层模块词汇时会自行引入它。如果你想打磨项目的*领域*术语而非其模块设计，请改用 [domain-modeling](https://aihero.dev/skills-domain-modeling)；要对现有代码库执行完整的架构审查，使用 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture)。

## 深层，而非浅层

当一个模块的大量行为隐藏在小接口之后时，它是**深层**的；当接口几乎和实现一样复杂时，它是**浅层**的。深度以**杠杆率**（leverage）来衡量——调用者（或测试）每学习一个单位的接口能撬动多少行为。关键在于，深度是*接口*的属性，而非实现的属性：一个深层模块内部可以由小型、可替换的部件组成，只要这些部件从不暴露给调用者。

两个检查承担了大部分工作。**删除测试**：想象删除该模块——如果复杂度随之消失，它就是个中间人传递层；如果复杂度在 N 个调用者中重现，那它一直在赚取自己的存在价值。以及**一个适配器意味着假设的接缝；两个适配器意味着真正的接缝**——不要在有东西真正跨接缝变化之前切割接缝。

## 接口就是测试面

调用者和测试穿越同一道接缝，因此设计良好的接口为测试提供了一个持久的目标，而接口背后的代码可以自由改动。这就是为什么词汇表坚持使用 **seam**（Feathers 的术语——一个可以在不编辑原代码的情况下改变行为的地方）而非被滥用的"boundary"，也是为什么这里的"接口"意味着*调用者必须知道的每一个事实*：签名，是的，还有不变量、顺序、错误模式和性能——不仅仅是类型层面的接口。

## 有意独立

`codebase-design` 是深层模块词汇的**单一事实来源**，被抽离为独立的模型调用型 skill，以便任何东西都能引用它。其他 skill 指向它而非复述这些词汇：[tdd](https://aihero.dev/skills-tdd) 借它来在编写测试前放置接缝，[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 在重构现有代码时依赖它，而 [to-spec](https://aihero.dev/skills-to-spec) 在草拟接缝和深化机会后编写规格说明时使用它。

保持其独立的意义在于，你也可以单独使用它——作为思考模块设计的**参考**——而不触发其他 skill 所要求的更大流程。在同一个地方一次性固定好词汇，每一次设计对话都会继承它们。

## 在系统中的位置

`codebase-design` 是一个**随时可用的独立 skill**——位于工程类 skill 之下的共享词汇层。它的最近邻是 [domain-modeling](https://aihero.dev/skills-domain-modeling)，后者是与之平行的词汇 skill，面向问题领域而非模块结构。当你不确定该用哪个 skill 或流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你导航。
