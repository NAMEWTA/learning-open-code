## 功能说明

`grill-with-docs` 就一个方案或设计对你进行访谈，直到你和 [Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 对它拥有一致的理解，并在访谈过程中把词汇和艰难决策写进你的仓库。它跑的是与 [grill-me](https://aihero.dev/skills-grill-me) 相同的访谈——一轮问题，然后等待，再下一轮——只不过指向一个代码库。

它是 **[有状态的](https://www.aihero.dev/ai-coding-dictionary/stateful)**。其他所有质询类 skill 都把 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 留在你脑子里；这一个在磁盘上留下文件。一个术语解决，它就在解决的那一刻落入 `CONTEXT.md`，而不是结尾批量处理。一个决策过了三道闸门，它就以 ADR 落地。这就是全部区别，也是人们对这个 skill 大多数麻烦的来源：产物是真实仓库里的真实文件，所以你期待它们出现时它们可能缺席，而当不止一人在写它们时它们会漂移。

## 何时使用

输入 `/grill-with-docs` 来调用它——Agent 不会自行调用。

在一个变更的开头、在一个仓库里、当方案仍然模糊、事物的措辞尚未定稿时使用它。它是单会话工具。你要哪个质询 skill 取决于眼前有什么：

| 你拥有什么 | 使用 |
| --- | --- |
| 你根本不在任何工作目录里 | [grill-me](https://aihero.dev/skills-grill-me) |
| 一个仓库，和一个你能在单次会话里定案的变更 | `grill-with-docs` |
| 一项大得装不进单次会话的工作——绿地构建、大功能 | [wayfinder](https://aihero.dev/skills-wayfinder) |
| 一个完全没有任何领域文档的仓库，也没有具体功能在脑子里 | `grill-with-docs`，目标是整个仓库而非某个变更 |
| 一个被卡住的决策，知识在别人脑子里 | [to-questionnaire](https://aihero.dev/skills-to-questionnaire) |

wayfinder 的分流归结为会话数量：`/grill-with-docs` 用于单会话规划，`/wayfinder` 用于多会话规划。

## 前置条件

skill 会写进你的仓库，所以你需要待在一个写东西安全的地方。已解决的术语进入根目录的 `CONTEXT.md` 词汇表——或者，如果根目录的 `CONTEXT-MAP.md` 把仓库标记为多上下文，则进入对应上下文的 `CONTEXT.md`。决策进入 `docs/adr/`。两者都是惰性创建的；在第一个术语或决策结晶之前什么都不存在，所以没有需要提前搭建的东西。

它还需要另外两个 skill 在场，因为它自己的 `SKILL.md` 只有一行，把活委托给它们：[grilling](https://aihero.dev/skills-grilling) 提供访谈，[domain-modeling](https://aihero.dev/skills-domain-modeling) 提供书写。只装 `grill-with-docs`，你得到的是一个不工作的 skill。

## 书面痕迹

一场会话产出三样东西，它们并不对等。

| 什么解决了 | 落在哪里 |
| --- | --- |
| 一个术语——项目自己对某事物的叫法 | `CONTEXT.md`，内联，解决的那一刻 |
| 一个难以撤销、没有上下文会让人惊讶、且是真正权衡的决策 | `docs/adr/` 下的一个 ADR |
| 你决定的其他一切 | 对话里，此外无处可去 |

第三行正是坑人的地方。`CONTEXT.md` 是词汇表，刻意保持为词汇表——没有实现细节、没有 [规格](https://www.aihero.dev/ai-coding-dictionary/spec)、没有草稿笔记。ADR 要三个条件同时满足才触发，所以大多数决策不合格，大多数会话产不出任何 ADR。一场产出更锐利的词汇表、零个 ADR 的会话是设计内的正常运作，但这意味着你达成共识的大部分只存在于你达成它的那个 [上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window) 里。把这场对话交给 [to-spec](https://aihero.dev/skills-to-spec)，而不是 [清掉](https://www.aihero.dev/ai-coding-dictionary/clearing) 它。

词汇表才是重点。领域语言是这个 skill 真正在构建的东西——项目自己的话，一次说定，让你、Agent 和同事不再花钱重新推导。值得说明的是，并非所有人都同意这能买来 Agent 的性能：最尖锐的公开反驳是，一个术语和它的平白英语展开从 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 那里得到相同结果，而词汇真正压缩的是共享它的人之间的沟通。按那种读法，词汇表依然有价值；只是价值被挪了位置。

## 它假设只有一位写者

有状态的产出假设只有一个人在策展它们。一个双人团队在一个仓库里跑了四个月，报告称在约 20% 的抽样已合并 PR 上出现了状态漂移，ADR 引用和 README 声明是漂移最严重的表面——经过深思、人工策展的文档比 Agent 记忆漂移得更厉害。修剪过期文档没有效果；同样的一次清扫几天内又过期了。真正有效的是彻底删除影子状态，并在 CI 里加一个确定性的引用与链接 linter。

相关地：在一个仓库里跨无关变更反复运行此 skill，容易积累混合主题的文档，因为没有任何东西把一场会话的产出和另一场分开。这两点今天在 skill 里都未修复。

## 常见问题

**我该用这个还是 `/wayfinder`？**
范围决定。任何你能在单次会话里定案的用它；当工作太大、装不进单次会话时用 [wayfinder](https://aihero.dev/skills-wayfinder)，它先把工作绘制成一张决策 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 地图。Wayfinder 更慢、更密，在一个边界清晰的功能上够它是最常见的错误。它不取代本 skill——它可以落入一场质询会话，处理地图中适合单会话的部分。

**它跑了，但没有 `CONTEXT.md` 也没有 ADR 出现。**
两个已知原因。平常的那个：没有东西合格。ADR 需要三道闸门全过，而一场没有任何新词汇的变更会话确实没东西可写。真正的 bug：当 skill 在另一个编排层内部运行——一个规范驱动开发的包装、一个多代理框架、一条把它当步骤调进别人流水线的规则——文件写入那一半被报告为悄悄不发生，而访谈照跑。这已归档、未修复。如果你处于那种设置，先检查工作目录再相信会话的输出。

**它一口气问完所有问题，没有推荐，也从没提过 `CONTEXT.md`。**
那是 skill 没能加载它的两个依赖。因为 `SKILL.md` 是一行委托，一个没拾起 [grilling](https://aihero.dev/skills-grilling) 和 [domain-modeling](https://aihero.dev/skills-domain-modeling) 的 Agent 会猜质询是什么意思，于是你得到一场无差别的问题倾倒。部分加载是更令人困惑的情况——`grilling` 加载了，`domain-modeling` 没有——你得到一场好访谈却没有任何书面痕迹。它与模型和 [effort](https://www.aihero.dev/ai-coding-dictionary/effort) 级别相关，是本 skill 被报告最多的问题。如果你怀疑它，直接问 Agent 加载了哪些 skill。

**我其他所有决策去哪了？**
只进了对话。这是关于本 skill 最有分量的公开抱怨：词汇表不是规格，大多数答案挣不到 ADR，也没有一本账把每个已解决的答案连到规格、ticket 和测试。精确的答案——顺序保证、否定需求、数值默认值——在下游被弱化成含混的散文，结果可能看起来完整，却缺了你真正决定的东西。今天可用的缓解是保住会话，直接把它喂给 [to-spec](https://aihero.dev/skills-to-spec)，并拿你自己的答案重新对照规格，而不是假设它抓住了它们。

**我能把它指向一个完全没有任何文档的现有仓库吗？**
能。这正是没有 ADR、没有领域语言、没有设计原则的代码库该用的 skill——调用它说"帮我记录我的仓库"。社区模式把它和 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 搭配，用来构建或修复 `CONTEXT.md`。预期要引导它：它会读代码并就它发现的东西问你，而由你说出代码库里已有的哪些词才是正确的词。

**会话结束时我该做什么？**
skill 的收尾信息往往开放结尾，这是一个已知的粗糙边缘。在主流程中，答案是同一场对话里的 [to-spec](https://aihero.dev/skills-to-spec)。如果变更小到可以立即构建，直接去 [implement](https://aihero.dev/skills-implement) 也行。

**为什么叫这个名字？**
没人对这个名字满意。有一个开放建议把它改名为 `grill-domain-model`，那更诚实地描述了行为。还没有任何进展。如果改名落地，文档页跟着移动，URL 也会变。

## 有效的标志

- `CONTEXT.md` 在会话*进行中*逐术语变化，而不是结尾一大坨出现。
- 词汇表读起来是纯粹的词汇——你项目的话配紧致的定义——不含任何实现细节或规格式散文。
- 代码库能回答的问题由读代码库来回答，而不是拿来问你。
- 你得到很少或没有 ADR，而得到的那几个，是你宁可不想重新争论的决策。
- 它会质疑你用过的某个词，因为你现有的词汇表对它的定义不同。

## 在系统中的位置

`grill-with-docs` 是主构建链的起点：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

它排在一切被写成规格之前——它产出 [to-spec](https://aihero.dev/skills-to-spec) 随后无需再访谈你就能综合的共享理解和定稿词汇。它近的邻居是 [grill-me](https://aihero.dev/skills-grill-me)——同一场访谈，但没有仓库、没有文件——以及 [domain-modeling](https://aihero.dev/skills-domain-modeling)，它驱动的词汇表与 ADR 训练；两者都站在 [grilling](https://aihero.dev/skills-grilling) 原语之上。在它上游，[wayfinder](https://aihero.dev/skills-wayfinder) 绘制大得装不进单次会话的工作，可以把地图的一部分交还给它。拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
