快速开始：

```bash
npx skills add mattpocock/skills --skill=grill-with-docs
```

```bash
npx skills update grill-with-docs
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)

## 功能说明

`grill-with-docs` 就一个方案或设计对你进行无休止的质询，一次一个问题，直到你和 Agent 达成共识——并在过程中同步记录词汇和决策。

质询**留下了书面痕迹**。普通的访谈虽然能帮助你理清思路，但会话结束后就消失了；而这个 skill 在每个术语解决的当下就将其捕获到 `CONTEXT.md` 词汇表中，并将那些艰难的、不可逆的决策记录为 ADR。达成的共识在对话结束后依然存在，而不仅仅存在于你的脑海中。

## 何时使用

输入 `/grill-with-docs` 来调用它——Agent 不会自行调用此 skill。

在一个变更的最开始阶段使用它，当方案仍然模糊、领域语言尚未确定时，你希望在编写任何代码之前对这两者进行压力测试。如果你只想要访谈而不需要产出物，使用 [grilling](https://aihero.dev/skills-grilling)；如果方案已经清晰，你只需要确定或记录术语，使用 [domain-modeling](https://aihero.dev/skills-domain-modeling)。而如果变更太大，无法在一次会话中完成，且其路径仍然迷雾重重——一个绿地项目、一个巨大的功能构建——则从上游的 [wayfinder](https://aihero.dev/skills-wayfinder) 开始：它将工作量绘制成一张决策地图，然后在路径清晰后交回给这条主流程。

## 前置条件

此 skill 是带有状态的——它在质询过程中将内容写入你的仓库。已解决的术语写入根目录的 `CONTEXT.md` 词汇表（或由 `CONTEXT-MAP.md` 标记的多上下文仓库中对应上下文的 `CONTEXT.md`），而真正难以撤销的决策作为 ADR 写入 `docs/adr/`。两者都是惰性创建的——在第一个术语或决策结晶成型之前不存在任何文件——所以你不需要提前搭建任何东西，但你需要在一个可以安全写入这些文件的位置。

## 质询引擎

引擎是一个**质询器**（grill）：一次一个问题、沿着设计树不懈地向下深入，在推进之前先解决决策之间的依赖关系，每个问题都提供推荐答案。代码库能回答的问题通过阅读代码库来回答，而非询问你。

使这个变体成为独立 skill 的关键在于答案的去向。随着质询进行，模糊的语言被磨砺为权威术语，并即时写入词汇表——而非在结尾批量处理。词汇表保持纯粹：只有词汇，没有实现细节，没有规格说明。ADR 只在小概率下被提出，仅当决策难以撤销、没有上下文会令后来者惊讶且经历了真正的权衡时才产生。大多数会话会产出一个更清晰的词汇表和很少甚至没有 ADR，这就是预期的结果形态。

## 有效的标志

- 它一次只问一个问题并等待回答，而非一口气抛出一份问卷。
- 术语在解决的当下就被写入 `CONTEXT.md`，使用项目自己的语言。
- 它尽可能深入代码库来回答自己的问题。
- ADR 保持罕见——你不会被要求对可逆的选择做橡皮图章式的背书。

## 在系统中的位置

`grill-with-docs` 是主构建链的起始步骤：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

它排在第一位，在一切被写成规格说明之前：它产出共享的理解和已确定的词汇表，然后 [to-spec](https://aihero.dev/skills-to-spec) 将这些合成规格说明而无需再次访谈你。它的近邻是 [grilling](https://aihero.dev/skills-grilling)（相同的访谈但不出具文档）和 [domain-modeling](https://aihero.dev/skills-domain-modeling)（它所驱动的词汇表和 ADR 机制）。当你不确定该用哪个 skill 或流程时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你导航。
