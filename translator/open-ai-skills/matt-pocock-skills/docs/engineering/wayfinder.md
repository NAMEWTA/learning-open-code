快速开始：

```bash
npx skills add mattpocock/skills --skill=wayfinder
```

```bash
npx skills update wayfinder
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)

## 功能说明

`wayfinder` 接受一项超出单个 Agent 会话能力的工作——被迷雾笼罩，从当前到目标的路径尚不可见——将其绘制为一份问题追踪器上的调查 ticket **共享地图**，然后逐个解决这些 ticket 直到道路清晰。它**做规划，不做执行**：每个 ticket 解决一个决策，当在有人着手构建之前不需要再做决策时，地图就完成了——因此它产出的是决策，而非可交付物。

## 何时使用

输入 `/wayfinder` 来调用它——Agent 不会自己触发它。

当一项工作**超出了单个 Agent 会话的承受能力**，并且通往其**目的地**的路线仍然迷雾重重时使用它——你能感觉到工作的轮廓，但还无法写出一份规范或计划。要将一个*已经清晰*的讨论转化为规范，使用 [to-spec](https://aihero.dev/skills-to-spec)；要将已经理解了的计划切分为可构建的 ticket，使用 [to-tickets](https://aihero.dev/skills-to-tickets)。Wayfinder 位于这两者的上游：当迷雾太重以至于无法直接制定规范时，你才运行它。

## 前置条件

地图及其 ticket 取决于仓库的问题追踪器，因此 wayfinder 需要 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 所建立的追踪器连接——它会在追踪器中嵌入一节"Wayfinding operations"，描述地图、子 ticket、阻塞关系和前沿查询在 GitHub、GitLab 或本地 Markdown 中的表达方式。缺少此文档时，wayfinder 默认使用本地 Markdown 地图。

## 地图即索引，迷雾即前沿

**地图**是一个单独的 `wayfinder:map` issue，其中的 ticket 是其子 issue——一个整个团队都能观察的共享 URL。它是一个**索引，而非仓库**：每个决策只存在于一个地方（它的 ticket），地图只做概括和链接，从不重复陈述。会话以低分辨率加载地图，按需放大查看单个 ticket。

在活跃的 ticket 之外是**战争迷雾**——你能感觉到即将来临但还无法确定的决策。判断某件事是 ticket 还是仍属迷雾的标准是：你是否能*现在就精确地陈述问题*，而不是你能否回答它。解决一个 ticket 会清除它前方的迷雾，将现在可以明确表达的内容**晋级**为新的 ticket。**前沿**是开放、未被阻塞、未被领取的 ticket——已知世界的边缘——追踪器原生的阻塞关系会将其可视化呈现，这样你无需打开地图就能看到哪些可以领取。迷雾只朝着**目的地**方向积聚；超出目的地的工作被视为**范围外**，直接关闭，永不晋级。

每个 ticket 要么是 **HITL**（人在回路中——深入访谈、原型验证），要么是 **AFK**（Agent 独立——调研）；HITL ticket 只能通过实时交互来解决，因此 Agent 永远不能自问自答。

## 有效的标志

- 命名**目的地**是第一步——在任何 ticket 存在之前——因为它确定了每个 ticket 所对照评估的范围。
- 一张地图就是一个 `wayfinder:map` issue；ticket 是其子 issue，通过**名称**引用，绝不只写一个裸的 `#42`。
- 一次会话至多解决一个 ticket，将答案记录为解决评论，关闭 ticket，并在*已做出的决策*中追加一行指引。
- 如果开场深入访谈发现**没有迷雾**，它会停下来告诉你这趟旅程小到不需要地图。

## 在系统中的位置

`wayfinder` 是一个面向大任务的**入口匝道**：一项规模太大、迷雾太重、无法一次会话制定规范的工作，先生成一张清理好的决策地图，然后汇入主构建流程。当迷雾被推向后方、路径已清晰时，交给 [to-spec](https://aihero.dev/skills-to-spec) 来调度多会话构建（或者，如果工作最终规模不大，直接实现）。它依赖 [grilling](https://aihero.dev/skills-grilling) 和 [domain-modeling](https://aihero.dev/skills-domain-modeling) 来解决单个 ticket，并依赖 [prototype](https://aihero.dev/skills-prototype) 和 [research](https://aihero.dev/skills-research) 来处理需要它们的 ticket 类型。当你不确定哪个技能或流程适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
