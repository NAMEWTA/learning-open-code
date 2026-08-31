## 功能说明

`wayfinder` 接下一个大得装不进一个 Agent [会话](https://www.aihero.dev/ai-coding-dictionary/session) 的工作——一个你叫得出其**目的地**的名字、却还看不见其路线的想法——把它绘制成你 issue 追踪器上一张由**决策 tickets** 组成的共享**地图**，然后逐个解决，直到道路清晰。

它做规划，不做执行。每个 ticket 装着一个问题，其解决是一个决策，而不是一段要执行的构建切片；当在有人去构建之前不再有任何要决定的事时，地图就完成了。那一条规则正是区分 wayfinder ticket 与普通实现 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 的东西，也是 Agent 破坏得最频繁的规则。地图清空时，wayfinder 交接；它不继续走进代码。

## 何时使用

输入 `/wayfinder` 来调用它——[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 不会自行调用。

它是整套里最重、最密的流程，所以触发条件很窄：工作必须真的比一个 Agent 会话能装的大，通往目的地的路线必须迷雾重重。分界是干净的一条：`/grill-with-docs` 用于单会话规划，`/wayfinder` 用于多会话规划。

| 你面前有什么 | 跑什么 |
| --- | --- |
| 一个你能一坐定案的边界清晰功能 | [grill-me](https://aihero.dev/skills-grill-me)，有代码库时用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 一个绿地项目，或横跨多次会话的构建，路线仍然不明 | `/wayfinder` |
| 一条决策已做完的线程 | [to-spec](https://aihero.dev/skills-to-spec)——径直跳过地图 |
| 一张已清空的 wayfinder 地图 | [to-spec](https://aihero.dev/skills-to-spec)，然后 [to-tickets](https://aihero.dev/skills-to-tickets) 和 [implement](https://aihero.dev/skills-implement) |
| 一场已经长太大的现有会话 | 说"hand off to `/wayfinder`"——[handoff](https://aihero.dev/skills-handoff) 既能桥进地图也能桥出地图 |

绿地不是要求。Wayfinder 常规用在遗留和半建成的代码库上，而且在那里可以说更锐利，因为很多迷雾是"这里已经为真的是什么"，而不是"我们该做什么"。

## 前置条件

地图和它的 tickets 住在仓库的 issue 追踪器上，所以 wayfinder 需要 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 铺下的追踪器接线。那一步会写一节"Wayfinding operations"，描述地图、它的子 tickets、阻塞边和前沿查询在 GitHub、GitLab 或本地 markdown 里怎么表达。Wayfinder 通过你 `CLAUDE.md` / `AGENTS.md` 里的指针解析那份文档，而不是固定路径；完全没有配置追踪器时，它回退到本地 markdown 文件。

追踪器不是装饰。阻塞关系正是让前沿在追踪器自己的 UI 里可视化呈现的东西，而一个没有原生依赖链接的追踪器——比如自托管的 Gitea——会把 wayfinder 降级为从地图文本推断阻塞项，能用但需要更近的监督。

## 地图、迷雾和前沿

**地图**是一个贴着 `wayfinder:map` 标签的单一 issue；它的 tickets 是它的子 issues。它是**索引，不是仓库**——一个决策恰好存在于一个地方，它的 ticket，地图只做概括和链接。会话以低分辨率加载地图，按需放大进单个 tickets，这正是让地图能继续长大、而不必每个会话为它的全部历史买单的东西。

四样东西住在上面：

- **目的地**——到达这张地图终点是什么样。命名它是制图的第一个动作，在任何 ticket 存在之前，因为目的地固定了每个 ticket 被对照衡量的范围。
- **已做决策**——每个已关闭 ticket 一行，各自链接到细节真正所在的地方。
- **尚未规格化**——**战争迷雾**。你预感会来、但还无法精确表述的决策。迷雾对 ticket 的检验标准是你能不能*现在*就精确陈述问题，而不是你能不能回答它。解决一个 ticket 会清掉它前方的迷雾，把现在可规格化的东西**晋级**成新 tickets。
- **范围外**——被裁定超出目的地的工作。迷雾只朝*目的地*方向积聚，所以范围外的工作被关闭、永不晋级。

**前沿**是开放、未被阻塞、未被领取的 tickets——已知世界的边缘。会话在做任何工作之前先把 ticket 分配给自己来领取，所以受派人*就是*领取本身，并发会话会跳过它。tickets 全程按名引用，绝不写裸 `#42`；一面 issue 数字墙在叙述里没法读。

## 四种决策 ticket 类型

每个 ticket 带一个 `wayfinder:<type>` 标签，要么是 **[HITL](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop)**——和一个为自己说话的人一起做——要么是 **[AFK](https://www.aihero.dev/ai-coding-dictionary/afk)**，由 Agent 独自驱动。一个 HITL ticket 只通过实时交流解决；一个回答自己 [质询](https://www.aihero.dev/ai-coding-dictionary/grilling) 问题的 Agent 已经把它弄坏了。

| 类型 | 模式 | 何时用它 | 由什么解决 |
| --- | --- | --- | --- |
| `grilling` | HITL | 默认。问题可以靠谈透解决。 | [grilling](https://aihero.dev/skills-grilling) 加 [domain-modeling](https://aihero.dev/skills-domain-modeling)，在一场新会话里 |
| `prototype` | HITL | "这该长什么样"或"这该怎么表现"——谈话解决不了的问题。 | [prototype](https://aihero.dev/skills-prototype)，建好的工件作为资产从 ticket 链接 |
| `research` | AFK | 工作目录之外的一个事实阻塞了决策。 | 一个 [research](https://aihero.dev/skills-research) [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent)，制图时开火，在 `research/<name>` 分支上并行烧完 |
| `task` | 两者皆可 | 没什么要决定，但手工工作阻塞了决策——配访问权限、注册服务、移动数据让形状可见。 | Agent 能做的自己来，否则给人类一份精确清单 |

`task` 是唯一*做*事而非做决策的类型，它靠解除决策的阻塞来挣得位置——从不靠交付一段目的地。这是实践中出错最多的类型：Agent 把它当成实现步骤，开始在地图里写产品代码。

Research 是*一会话一个 ticket* 的唯一例外。

## 常见问题

**这和 `/grill-with-docs` 有什么不同？我该先开始哪个？**
会话数量，不是项目规模。`/grill-with-docs` 是单会话规划；wayfinder 是多会话规划。如果你能把整个东西握在一场对话里，grilling 是更便宜、更好的工具，而对那种情况 wayfinder 确实更慢更密。社区沉淀出的简写是：wayfinder 只有当工作装不进单次会话时才说得通。这遥遥领先是 wayfinder 被问得最多的问题，它一直被问，因为描述没有告诉你自己的任务落在那条线的哪里——你得自己判断会话数量。

**它问"目的地"时，是指本会话的终点还是一切的终点？**
整张地图——整张地图的目的地，不只是初始会话。那个问题读起来含糊，因为 wayfinder 按定义是多会话工具，所以按会话范围作答从来讲不通。典型目的地是：一份要交接的 [规格](https://www.aihero.dev/ai-coding-dictionary/spec)、规划开始前要锁定的决策、一个概念验证、或一次原地改动如数据迁移。

**地图清空了。为什么我还需要 `/to-spec` 和 `/to-tickets`——wayfinder 不是已经写了规格、做了 tickets 吗？**
没有。Wayfinder 的 tickets 是决策 tickets，地图关闭时它们也全都关了。剩下的是满满一张链接决策的地图，那不是构建计划。[to-spec](https://aihero.dev/skills-to-spec) 把这些链接决策塌缩成一份规格——`/to-spec #<map_issue>`——[to-tickets](https://aihero.dev/skills-to-tickets) 把它切成曳光弹实现 tickets。把地图直接循环进 [implement](https://aihero.dev/skills-implement) 跳过塌缩，把链接细节扔掉了。只有当工作结果确实很小时才直奔实现。人们确实跑精简版流水线并报告有效；多出的两步买来的是一份审查者或同事能读的显式规格工件，你越不单打独斗它越重要。

**我的 Agent 在 wayfinder 会话中途开始写生产代码。**
本 skill 被报告最多的失败，背后有一个真实的洞。Wayfinder 的"规划、别做"默认可以在地图的 **Notes** 里被覆盖——但 Notes 是 Agent 写的，所以约束和它的豁免住在同一个文件里，而那个文件归被约束方所有。一位用户看着 Agent 把"this map carries execution"写进自己的 Notes，然后在之后的会话里把它读回来当成自己的执照，在一个线上服务器上继续建。skill 内部没有硬性的"我的意思是默认"的停止。在那之前：读任何不是你亲自制图的地图的 Notes，把实现留在它自己的会话里，并把任何看起来像构建切片的 `wayfinder:task` 当作类型标错。

**我绘制了 27 个 tickets，等我走到第十三个时，其余的都不再有意义了。**
真实且反复被报告的结果，照录自一份现场报告。Wayfinder 的默认本能是全面规划，而一张靠前面 tickets 证伪的假设支撑后面 tickets 的地图，正是 skill 被指控的瀑布陷阱。两件事反击它。把地图限定在一个有界目的地，而不是整个产品——实践者一致报告，限定在一个定义好的 epic 的地图比一张铺开的"implement V1"表现好，而且一开始规划非常大就不是目标——小步交付才是。还有，激进地 [prototype](https://www.aihero.dev/ai-coding-dictionary/prototyping)：路线保持常新的全部原因，就是不确定性在实现依赖它之前被便宜的实在工件冲掉。Wayfinder 是"prototypemaxxing"，不是"planmaxxing"。

**我能并行处理几个 tickets 吗？**
前沿就是建来给你看什么可领取的，阻塞边让并行工作纸面上安全。实践中一次一个才是更安全的默认。同时做两个 grilling tickets 的用户会在一个会话里被问到一个他刚在另一个会话里回答过的问题，因为会话之间不共享 [上下文](https://www.aihero.dev/ai-coding-dictionary/context)。还有一个已知的 prototype tickets 缺口：有报告说 Agent 建了三个 UI 变体、自己选了一个、然后关了 ticket——选择权是你的，而 skill 目前没有足够大声地说出来。如果你确实要并行跑，先自己审查一遍依赖图。

**我必须用 GitHub Issues 吗？**
不用——任何 issue 追踪器都行。GitHub 是支持最好的路径，因为它的原生子 issue 和阻塞关系让前沿不用打开地图就可见；GitLab、Linear、Jira 和本地 markdown 都有人用。两个诚实的告诫。一个没有原生阻塞的追踪器意味着依赖图从文本推断，需要手工修正。而本地 markdown 把工件放进你的仓库，这不推荐：把这类材料存在仓库里容易导致意外持久化。开源维护者撞上相反的问题——公开追踪器被 Agent 生成的规划 tickets 填满——而往往还是选本地 markdown。

**质询令人精疲力竭。每个问题都有三段长。**
这是对 wayfinder 最尖锐的现役抱怨，而且没解决。一位用户给出的分解：冗长本身导致决策疲劳，长度把*为什么*问这个问题剥掉了，所以地图越长你越失去决策到决策的链条。冗长看起来是当前这代 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 的属性而非 skill 的，没有修复落地。流传中的实践者缓解：跑更低的 [reasoning effort](https://www.aihero.dev/ai-coding-dictionary/effort)，并在你的全局 `CLAUDE.md` 里放一条平白语言指令。无论如何预期要在这里花真思考——wayfinder 要求你想多少不是缺陷，那几乎是它存在的全部意义。

**我关掉的一个决策结果是错的。我该编辑旧 ticket 还是开个新的？**
没有官方指引，而 Agent 的本能帮倒忙：它倾向绕开坏决策设计，而不是挑战它，所以你不得不手动掌舵。真正有效的是把变化平白告诉 wayfinder——它更新地图、修订受影响的 tickets、并在已关闭的上评论。地图中途的范围变化是可恢复的。一张你*设计成*会变化的地图是范围界定有问题的信号。

**`decision-mapping` 去哪了？**
它就是本 skill，v1.1 改名为 `wayfinder`，以 `/wayfinder` 调用。"Decision map" 是行话，而且也不准确，因为四种 ticket 类型里只有一种真是一个决策。重构给 skill 一套连贯词汇——目的地、战争迷雾、前沿、地图——而不是在顶上叠一个发明的术语。单位保留了"决策"这个词：一个 **decision ticket** 是 wayfinder ticket 的叫法，正是为了阻止人们把它读成实现 ticket。

## 有效的标志

- 在单个 ticket 存在之前，目的地被写下并达成一致。
- 每个开放 ticket 读起来是一个问题。任何读成"建出 X"的 ticket 要么类型标错，要么属于地图下游。
- 你不用打开地图就能在追踪器上看到哪些 tickets 可领取——那是前沿借原生阻塞自己渲染出来。
- 一个会话解决一个 ticket，把答案作为解决评论发布，关闭它，在地图的*已做决策*上留一行。然后它停下。
- **尚未规格化**随时间缩小。一片晋级成 ticket 的迷雾从那一节消失，而不是同时活在两个地方。
- 开场广度优先的质询完全没发现迷雾时，skill 停下，告诉你这项工作小到可以跳过地图。
- 完成地图的会话把你引向一份规格，而不是一个 pull request。

## 在系统中的位置

`wayfinder` 是一条**情境式入口通道**，不是默认前门。grill 主导的想法 → 交付链仍然是大多数工作开始的地方；wayfinder 是当想法大得装不进单次会话时你爬上去的东西，它在 [to-spec](https://aihero.dev/skills-to-spec) 处汇回那条链，因为一张清空的地图交接而不是构建。

底下，它大多是穿着 wayfinder 调度外衣的其他 skills：[grilling](https://aihero.dev/skills-grilling) 和 [domain-modeling](https://aihero.dev/skills-domain-modeling) 解决默认 ticket 类型，[prototype](https://aihero.dev/skills-prototype) 解决谈话解决不了的 tickets，[research](https://aihero.dev/skills-research) 作为子代理运行，让它的阅读从不落进你的会话。[handoff](https://aihero.dev/skills-handoff) 是进出的桥——从一场长过头的对话进地图，从中途冒出的支线任务出去。其他一切，[ask-matt](https://aihero.dev/skills-ask-matt) 在整套之上路由。
