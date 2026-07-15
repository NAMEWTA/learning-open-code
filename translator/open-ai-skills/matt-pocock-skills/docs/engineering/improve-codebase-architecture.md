快速开始：

```bash
npx skills add mattpocock/skills --skill=improve-codebase-architecture
```

```bash
npx skills update improve-codebase-architecture
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)

## 功能说明

`improve-codebase-architecture` 扫描代码库，寻找**深化机会**—— 即浅层模块（接口几乎与它所隐藏的东西一样复杂）可以变成深层模块的地方 —— 将其以独立的可视化 HTML 报告呈现，然后对你选择的任何一个候选方案进行 grilling 推敲。

它**不会**给你一个扁平的 refactor 列表。每个候选方案都必须通过**删除测试**—— 移除这个模块是否会将复杂性**集中**到一个更小的接口后面，还是仅仅将其移动到别处？只有"集中"的情况才能获得一张卡片。这个过滤器确保报告不会变成泛泛的清理建议。

## 何时使用

通过输入 `/improve-codebase-architecture` 来调用 —— Agent 不会自行触发它。

将其作为定期的健康检查使用：每隔几天执行一次，或者当你感觉代码库中为了理解一个概念需要在小模块之间跳来跳去太多时使用。它读取现有架构并提出深化方案。如果你已经知道想要重新设计的模块，只需要相关的术语来思考它，请使用 [codebase-design](https://aihero.dev/skills-codebase-design) —— 本 skill 是做调研找出候选方案的；那个 skill 是设计的操作台。

## 深化机会

整个 skill 围绕一个理念：**深度**。深模块在一个小而稳定的接口背后隐藏了大量功能；浅模块则通过一个几乎和底层代码一样庞大的接口暴露其实现。报告搜寻的是浅薄 —— 仅为可测试性提取的纯函数，而真正的 bug 藏在了调用方式中（缺乏**局部性**），模块在其**切面**上泄漏，不打开五个文件就无法理解的概念 —— 并提议解决这些问题所需的深化方案。

它使用共享的设计语言（**模块**、**接口**、**深度**、**切面**、**适配器**、**杠杆**、**局部性**）以及来自 `CONTEXT.md` 的项目领域语言来表达，因此一个候选方案读起来应该是"深化订单接收模块"，而不是"重构 FooBarHandler"。

## 报告，然后是 grilling

输出是一个可在浏览器中打开的 HTML 文件，写入操作系统的临时目录 —— 不会进入仓库。每个候选方案都是一张卡片，包含涉及的文件、痛点、用平实语言描述的解决方案、在局部性和杠杆方面的收益、前后对比图，以及一个标签（`Strong` / `Worth exploring` / `Speculative`）。报告的末尾会指明它建议优先处理的那一个。

然后它会停下来，询问你想探索哪一个。选择后，它会对该设计运行 [grilling](https://aihero.dev/skills-grilling) 循环 —— 约束条件、切面背后是什么、哪些测试会保留 —— 随着决策固化，内联更新领域模型。

## 在系统中的位置

`improve-codebase-architecture` 是**定期维护**工具 —— 每隔几天运行一次，而不是链条中的一个步骤。它的邻居是 [codebase-design](https://aihero.dev/skills-codebase-design) ，它拥有每个候选方案所用的深度与切面术语；[grilling](https://aihero.dev/skills-grilling) ，它在选定候选方案后对设计树进行遍历；以及 [domain-modeling](https://aihero.dev/skills-domain-modeling) ，它在重新设计落定时保持 `CONTEXT.md` 和 ADR 是最新的。当你拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
