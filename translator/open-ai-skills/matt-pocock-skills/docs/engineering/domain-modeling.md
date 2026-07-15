快速开始：

```bash
npx skills add mattpocock/skills --skill=domain-modeling
```

```bash
npx skills update domain-modeling
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)

## 功能说明

`domain-modeling` 在设计中构建和打磨项目的**通用语言**——挑战模糊的术语、用具体场景对关系进行压力测试，并在术语和决策结晶成型的那一刻将它们记录下来。

这是一种**主动的**训练，而非被动的。仅仅阅读 `CONTEXT.md` 来借用其词汇是任何 skill 都能做到的一行指令的习惯性操作；此 skill 适用于你正在*改变*模型时——铸造一个权威术语、捕捉代码与你刚说过的话之间的矛盾、记录一个难以撤销的决策。而且它保持词汇表的整洁：`CONTEXT.md` 是一个纯粹的词汇表——没有实现细节、没有规格说明、没有草稿纸。

## 何时使用

输入 `/domain-modeling`，或在任务合适时 Agent 会自动调用它——当你正在确定术语、解决多义词问题或记录架构决策时。

当*词语*本身成为问题时使用它：两个人对"取消"的理解不一样，"账户"承担了三种不同的职责，或设计对话总是卡在一个从未被精确定义的概念上。如果问题是模块的*形状*——接缝在哪里、接口有多深——改用 [codebase-design](https://aihero.dev/skills-codebase-design)。如果你想在构建前对方案本身进行质询，使用 [grilling](https://aihero.dev/skills-grilling)。

## 前置条件

此 skill 写入两个位置，都是惰性创建的——只有在有内容需要记录时才创建。已解决的术语写入根目录的 `CONTEXT.md`（或在由 `CONTEXT-MAP.md` 标记的多上下文仓库中，写入对应上下文的 `CONTEXT.md`）。决策写入 `docs/adr/`。无需提前准备任何东西；第一个解决的术语会创建词汇表，第一个真正的权衡会创建 ADR。

## 词汇表与 ADR

两种产出物，两种不同的准入标准：

- **词汇表**（`CONTEXT.md`）捕获语言。每当一个模糊术语被规范化，它就会被即时写入——而非批量处理——以便共享词汇表与对话保持同步。它严格排除任何实现细节。
- **ADR** 捕获一个决策，准入标准很高：仅在决策**难以撤销**、**没有上下文会令后来者惊讶**且**经历了真正的权衡**时才提出。三者缺其一，就不产生 ADR。这是让 `docs/adr/` 成为重要分叉的记录而非流水日记的关键。

让这一切打通的关键动作：当你说出某事的工作方式时，此 skill 会交叉引用代码并揭示矛盾——"你的代码取消了整个订单，但你刚才说部分取消是可行的——到底哪一个是对的？" 语言和代码被强制达成一致。

## 有意独立

`domain-modeling` 是构建项目通用语言的**单一事实来源**，被抽离为独立的模型调用型 skill，以便任何其他 skill 都能引用它。[grill-with-docs](https://aihero.dev/skills-grill-with-docs) 依赖它在质询过程中记录术语和决策，[triage](https://aihero.dev/skills-triage) 用它来保持工单使用项目自己的语言，[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 在工作过程中引用它。

保持其独立意味着你也可以直接使用它——作为如何打磨模型的**参考**——而不必承诺执行那些 skill 所要求的步骤。语言存放在一个地方，所有需要它的东西都指向那里。

## 在系统中的位置

`domain-modeling` 是一个**随时可用的独立 skill**，在其他 skill 的下层运行，就像在固定步骤上一样频繁。它的最近邻是 [codebase-design](https://aihero.dev/skills-codebase-design)，因为共享语言正是让你能够精确命名深层模块及其接缝的前提；下游方面，已确定的词汇表正是 [to-spec](https://aihero.dev/skills-to-spec) 合成为项目自有语言的规格说明所使用的素材。当你不确定该用哪个 skill 或流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你导航。
