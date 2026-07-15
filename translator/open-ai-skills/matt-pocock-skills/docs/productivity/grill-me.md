快速开始：

```bash
npx skills add mattpocock/skills --skill=grill-me
```

```bash
npx skills update grill-me
```

[源代码](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)

## 功能说明

`grill-me` 对某个计划或设计执行一场不留情面的面试，遍历决策树的每一个分支，直到你和 Agent 达成**共识**。

它每次只问**一个问题**并等待回答。它从不会一次性向你抛出一堆问题——那会让人无所适从——而且如果某个问题可以通过阅读代码库来回答，它会直接去读而不是来问你。每个问题都附带 Agent 自己的推荐答案，因此你是在对一项提议做出反应，而不是盯着空白的提示框发呆。

## 何时使用

你通过输入 `/grill-me` 来调用它——Agent 不会自己主动使用它。

当你准备动手构建之前，某个方案感觉大致正确，但你隐约感觉其中藏着尚未解决的决策时，就是使用它的时机——你希望那些薄弱环节被发现并暴露出来。如果你希望同样的问询过程还能留下 ADR 和术语表的书面记录，请使用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)。而如果任务太大、一次会话无法承载，且通往目标的路径仍然模糊不清——比如一个全新项目或一个大型功能构建——则应从更上游的 [wayfinder](https://aihero.dev/skills-wayfinder) 开始，它会先将任务绘制成一张决策地图，然后再合并回当前流程。

## 设计树

整个会话将计划视为一棵决策树，逐一解决决策之间的依赖关系——先解决父级决策，再处理悬挂在其上的子级决策。重点不在于快速达成一致，而在于将每一个隐含的决策显式化，确保没有任何重要事项被默默地假定。结束时，你将得到一个所有分支都已被遍历过的计划。

`grill-me` 是**无状态的**：它不写入任何内容，也不留下工作区。它可以在任何地方运行，唯一的产出物就是对话中那份被磨砺得更加清晰的认知。这与 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 形成刻意对比，后者将同样的面试过程以持久化的 ADR 和术语表形式记录下来。

## 在系统中的位置

`grill-me` 是一个随时可用的独立工具——在计划需要加固时进行的构建前压力测试。它是通往 [grilling](https://aihero.dev/skills-grilling) 原语的无状态、用户调用型入口；它最近的邻居是 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，后者是有状态的同胞技能，执行相同的面试但额外将决策记录为 ADR 和术语表。如果最终产出是你希望书面化的规范，则交接给 [to-spec](https://aihero.dev/skills-to-spec)，它会将已达成共识的认知合成为规范而无需重新面试你。当你不确定哪个流程适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
