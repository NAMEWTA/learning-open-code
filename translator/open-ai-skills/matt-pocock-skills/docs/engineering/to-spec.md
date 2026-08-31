## 功能说明

`to-spec` 把你刚刚进行过的对话变成一份 [规格](https://www.aihero.dev/ai-coding-dictionary/spec)，并作为单个 issue 发布到你的 issue 追踪器。

它不访谈你。到你用它的时候，决策已经做完了，所以它综合已知的东西——从对话线程、从代码库、从你的 `CONTEXT.md` 和 ADR——而不是开一轮新问题。规格是已做决策的记录，不是做出新决策的地方。

## 何时使用

输入 `/to-spec` 来调用它——[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 不会自行调用。

当构建太大、装不进一个 Agent [会话](https://www.aihero.dev/ai-coding-dictionary/session)、必须靠拆成多个才能存活时使用它。这就是全部触发条件：

| 你在哪里 | 跑什么 |
| --- | --- |
| 你还没决定任何事 | 先 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |
| 已决定，工作装得进一个 [上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window) | [implement](https://aihero.dev/skills-implement)——跳过规格 |
| 已决定，工作横跨多次会话 | `/to-spec`，然后 [to-tickets](https://aihero.dev/skills-to-tickets) |
| 一张 [wayfinder](https://aihero.dev/skills-wayfinder) 地图已清空 | `/to-spec #<map_issue>` |

## 前置条件

`to-spec` 把规格作为 issue 发布，所以 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须先为这个仓库配置好追踪器和 triage 标签词汇。两种都行：GitHub 这样的真实追踪器，或 `.scratch/` 下的本地 markdown 文件——后者开箱即用。

## 规格是一份决策记录

规格存在是因为上下文窗口会结束。你在 [质询](https://www.aihero.dev/ai-coding-dictionary/grilling) 时定案的一切——解决方案的形状、你辩论过的选择、你刻意拒绝的东西——都在一场即将被清掉的对话里。规格就是从那里存活下来的东西。

所以它不验证任何东西，也不决定任何东西。它捕获已决定的内容，用你项目自己的词汇，让一场新会话能拾起工作而不必你重新解释。规格里任何你从没真正说过的东西都是缺陷。

## 接缝先于散文

在写任何一个字之前，`to-spec` 先草拟功能将被测试的**接缝**，并和你核对。它优先用已有的接缝而非新建的，并取它能取到的最高的接缝——跨一个变更的理想数量是一个。

这些约定好的接缝随后四处旅行。[tdd](https://aihero.dev/skills-tdd) 只在预先约定的接缝工作，[code-review](https://aihero.dev/skills-code-review) 对照规格审查 diff，所以一个没人同意的接缝会以审查发现的形式出现。绑定是间接的——它穿行于这份文档——这正是接缝对话值得在这里认真对待、而不是推迟到实现的原因。

## 常见问题

**`/to-prd` 去哪了？**
它就是本 skill，v1.1 改名。"Spec" 现在是唯一的贯穿术语，旧的 `to-prd` slug 已死——用新名字重新安装。取代旧词汇的一对是 *spec* 和 *tickets*：规格是目的地和固定它的决策，[ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 是抵达那里的执行步骤。如果你转向，删掉未完成的 tickets、保留规格。

**为什么规格要贴 `ready-for-agent` 标签？我不想要 Agent 照着它实现。**
那个标签的意思是"无需进一步 triage"——文档完整到 Agent 可以据此工作。它是输入标识，不是工单。但如果你运行轮询 `ready-for-agent` 的 [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) Agent，那个区别对它们不可见，它们会乐意在一次运行里构建整个规格，而不是拾起 ticket 切片。这是本 skill 被报告最多的粗糙边缘。在它改变之前，在你的 AFK Agent 提示词里显式排除父规格，或者等 `/to-tickets` 跑完就把标签剥掉。

**为什么不从 grilling 直奔 `/to-tickets` 跳过规格？**
常常就该跳过——规格只在多会话工作上赚到它的步骤。它值钱的地方在于 tickets 是可丢弃的、规格不是：每个 ticket 为一个全新上下文窗口而切尺寸、会被删或关，而规格留下来，作为它们背后推理的唯一住处。在单会话变更上这什么也买不到，你还付了一次 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 可能漂移的额外综合步骤。走 grilling → `/implement`。

**我刚完成一张 wayfinder 地图。我喂它什么？**
主地图 issue——`/to-spec #<map_issue>`，不是单个决策 tickets。[wayfinder](https://aihero.dev/skills-wayfinder) 产出的是决策而非可交付物，散落在一张地图上；`to-spec` 是把它们塌缩成一份可构建文档的步骤。把地图直接循环进 `/implement` 会丢掉那次塌缩。

**规格是给我审查的，还是只给 Agent 的？**
主要是给 Agent 的，读起来也是那样——完整、密集、引用多。值得你过目的部分是接缝和范围外小节，因为那是错误决策最容易便宜抓到、也最贵以后发现的两个地方。从头到尾通读是一份人们真实拥有的抱怨，没有摘要模式：诚实的回答是，如果规格让你惊讶，是质询太浅，不是规格太长。

**tickets 开始后我是让规格保持冻结，还是让 Agent 改写它？**
没有东西让它保持同步，所以实践中它是你当时所知的快照，第一次实现教你点东西时就过期了。工作上线后把它当可丢弃的。注定比它活得更久的工件是你的 `CONTEXT.md` 和 ADR——如果实现期间学到的东西值得留存，它属于那里，不属于一份被编辑过的规格。

**我的工作是重构或模块边界，不是功能。模板合适吗？**
不太合适，这是一个已知限制。模板重度依赖用户故事，那对架构工作是个错误的形状——你最终会围绕真正关于接口和不变量的决策，写出没人要的故事。改用实现决策和测试决策小节，并让持久的架构调用通过 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 以 ADR 落地，而不是试图让规格扛着它们。

**它会检查追踪器里的相关工作，或引用它尊重的 ADR 吗？**
两个都不会。它读并尊重覆盖它触及区域的 ADR，但不会链接它们，也不会在起草前搜索追踪器里的重叠 issue——所以一份规格可以悄悄重复某人已提交的工作。如果那个区域很忙，自己先搜追踪器。

**`/to-tickets` 读不了我的规格——它一直在截断。**
非常大的规格可能超出追踪器 issue 能干净回传的范围，又没有本地副本可回退。修复是上下文卫生：不要在 `/to-spec` 和 `/to-tickets` 之间 [清掉](https://www.aihero.dev/ai-coding-dictionary/clearing) 或 [压缩](https://www.aihero.dev/ai-coding-dictionary/compaction)。在同一个窗口里跑它们，规格就根本不必重新抓取。

## 有效的标志

- 它开始写，而不是问你一轮新问题。
- 它在写之前把接缝摆给你，并尽量少提接缝。
- 它用你项目的名词回来，而不是通用的产品管理套话。
- 里面每个决策都是你记得自己做过的那种。没有东西为填满某一节而被发明。
- 范围外小节有真实的内容——你拒绝的东西通常是页面上最有用的几行。

## 在系统中的位置

`to-spec` 是主构建链中的一步，而且只在它的多会话分支上：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

它上游的邻居是 [grill-with-docs](https://aihero.dev/skills-grill-with-docs)——做这个 skill 只记录的决策——以及 [wayfinder](https://aihero.dev/skills-wayfinder)，它完工的地图恰好在这里汇入链条。下游，[to-tickets](https://aihero.dev/skills-to-tickets) 把规格切成曳光弹 tickets 供 [implement](https://aihero.dev/skills-implement) 构建。拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
