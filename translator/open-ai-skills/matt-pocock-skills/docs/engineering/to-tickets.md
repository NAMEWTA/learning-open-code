## 功能说明

`to-tickets` 把一个计划、一份 [规格](https://www.aihero.dev/ai-coding-dictionary/spec) 或你正在进行的对话拆成你 issue 追踪器上的一组 **[ticket](https://www.aihero.dev/ai-coding-dictionary/ticket)**。每个 ticket 声明它的**阻塞边**——它开始之前必须完成的那些其他 ticket。

每个 ticket 都是一颗**曳光弹**：一条穿过变更每一层——schema、API、UI、测试——的狭窄但完整的路径，落地那一刻就能独立演示。正是这个约束让它与显而易见的拆活方式——一次切一层、最后集成——行为不同。它还把每个 ticket 切成恰好塞进一个全新 [上下文窗口](https://www.aihero.dev/ai-coding-dictionary/context-window) 的大小，因为拾起 ticket 的将是一场从没见过你规格的 [会话](https://www.aihero.dev/ai-coding-dictionary/session)。

## 何时使用

输入 `/to-tickets` 来调用它——[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 不会自行调用。

| 你在哪里 | 跑什么 |
| --- | --- |
| 你有一份规格 issue，构建横跨多次会话 | `/to-tickets`，或 `/to-tickets #<spec_issue>` |
| 计划只存在于对话里，从没写过 | `/to-tickets` 直接读线程——不需要规格 |
| 整个变更装得进一个上下文窗口 | [implement](https://aihero.dev/skills-implement)——跳过 tickets |
| 什么都没决定 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，然后 [to-spec](https://aihero.dev/skills-to-spec) |
| 一张 [wayfinder](https://aihero.dev/skills-wayfinder) 地图已清空 | 先 [to-spec](https://aihero.dev/skills-to-spec) 把地图塌缩，再 `/to-tickets` |

`to-tickets` 产出的 tickets 天生就是 Agent 就绪的。不要对它们跑 [triage](https://aihero.dev/skills-triage)——triage 是给从别人那里来的工作用的。

## 前置条件

`to-tickets` 发布进一个追踪器，所以 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须为这个仓库配置了一个，连同 triage 标签词汇。两种都行：GitHub 或 Linear 这样的真实追踪器，或 `.scratch/` 下的本地 markdown 文件——后者开箱即用。

## 曳光弹，而非层

**水平**切片交付变更的一层。在每一层都落地之前什么都不能工作，而每个 ticket 的验收标准不得不伸手去够另一个 ticket 拥有的工作。**垂直**切片——曳光弹——一次性交付一条穿过所有层的窄路径，所以它可以单独验证，并拥有它评分的一切。

这是人们破坏得最频繁的规则，后果有据可查。一个团队跑了一个按层切片——语料、生产者、聚合器、选择器——的 26 个 ticket 堆栈，每个已关闭 ticket 大约花了二十次 Agent 运行，其中约四分之三是返工。他们自己的事后复盘把每一个失败类别都追溯回水平切片，而不是实现。

发布任何东西之前会发生两件事。`to-tickets` 寻找预重构——"让变更变容易，再做容易的变更"——并把那项工作排在最先。然后它把拆解作为编号列表呈现并就它考你：粒度对吗、阻塞边真实吗、有什么该合并或拆分。在你批准之前，没有东西到达追踪器，而那次考问正是推回去的地方。

## 阻塞边

边是这份工件的核心。它们随追踪器不同有两种读法：

| 追踪器 | 边住在哪里 | 你怎么推进它们 |
| --- | --- | --- |
| 本地 markdown | `.scratch/<feature>/issues/<NN>-<slug>.md` 下每个 ticket 一个文件里的文本，阻塞项优先编号 | 从上到下，手工 |
| 真实追踪器（GitHub、Linear） | 原生阻塞链接，或追踪器支持时的子 issue | 任何阻塞项都完成的 ticket 位于**前沿**，可以被领取 |

无论哪种方式，边都住在 ticket 里。介质只决定是否有东西能并行地基于它们行动。`to-tickets` 产出工件；运行它——一次一个会话，或一支舰队——是你的工作，不是 skill 的。

## 宽幅重构的例外

有一种形状打破曳光弹规则。**宽幅重构**是一个单一的机械变更——重命名一列、改一个共享符号的类型——它的**爆炸半径**横扫整个代码库，所以一次编辑破坏成千上万的调用点，没有垂直切片能绿色落地。

`to-tickets` 把它按**扩展–收缩**排序：

- **扩展**——在旧形态旁边添加新形态，什么都不破坏。
- **迁移**——按爆炸半径（按包、按目录）分批把调用点搬过去，每批一个 ticket，每个都被扩展阻塞。CI 保持绿色，因为旧形态还在。
- **收缩**——一旦没有调用者留下，删除旧形态，用一个被每个迁移批次阻塞的 ticket。

当连批次都无法单独保持绿色时，它们共享一个集成分支，全部阻塞一个最终的集成并验证 ticket。绿色只在那个地方承诺。

## 常见问题

**它为一个三行变更产出了十二个 ticket。**
过度分解是本 skill 被报告最多的摩擦点，跨实践者一致： [模型](https://www.aihero.dev/ai-coding-dictionary/model) 默认原子单位，丢掉会让它们有意义的归组。考问步骤正是为此存在——让它合并，它会合并。更深的答案是 tickets 有地板：如果整个变更装得进一个上下文窗口，你根本不需要这个 skill。直奔 [implement](https://aihero.dev/skills-implement)。

**tickets 出来是一层一个——所有 schema 在一个里，所有 API 在另一个里。**
这正是垂直切片规则写来要防的失败，skill 有时还是产出它。在考问步骤抓住它：对每个 ticket 问一个问题——这个完成后我能演示什么？答不上的 ticket 就是水平切片。有人因此给每个 ticket 加一行"演示路径"，报告说这会把模型推向垂直分解。

**在 GitHub 上 tickets 没被创建为规格 issue 的子 issue。**
已知且未修复。它在十几次运行和好几个模型上被报告过，[最完整地记录在 issue #554](https://github.com/mattpocock/skills/issues/554)，而且在 Codex 上比在 Claude 上更糟。`gh` 自 v2.94 起原生支持这个：`gh issue create --parent <n>`，事后用 `gh issue edit <parent> --add-sub-issue <n>`。在追踪器模板优先用它们之前，跑完一次后自己接父链接是可靠的做法。

**"Blocked by" 被写进 issue 正文，而不是真正的阻塞链接。**
同一类问题，[报告在 issue #513](https://github.com/mattpocock/skills/issues/513)，那里的 Agent 甚至断言 GitHub 根本没有原生阻塞关系。它有——`gh issue create --blocked-by 12,15`。因为阻塞项先发布，它们的编号在创建时总是可用的。正文文本是为了没有原生边的追踪器准备的回退，不是默认。

**本地 tickets 去哪了？v1.1 的说明说有一个根级 `tickets.md`。**
确实有过，而那是个 bug——当并行 Agent 写它时，单个共享文件还会竞态。本地模式现在在 `.scratch/<feature-slug>/issues/<NN>-<slug>.md` 下按依赖顺序写，每个 ticket 一个文件，匹配本地追踪器模板已经描述的布局。`NN` 前缀是真实的 ticket ID，所以 `/implement 03` 能用，不必重打一长串标题。

**它读我的规格时一直截断。**
非常大的规格可能超出追踪器 issue 能干净回传的范围，又没有本地副本可回退——Agent 然后烧 [工具调用](https://www.aihero.dev/ai-coding-dictionary/tool-call) 重新抓取块，永远到不了结尾。不要在 `/to-spec` 和 `/to-tickets` 之间 [清掉](https://www.aihero.dev/ai-coding-dictionary/clearing) 或 [压缩](https://www.aihero.dev/ai-coding-dictionary/compaction)。在同一个上下文窗口里跑它们，规格就根本不必再被取回。

**验收标准什么都没评分——有些在任何工作做完之前就通过了。**
模板要标准却没说它们能不能失败，所以这会发生。三种形状反复出现：一个在基础提交时已经为真的标准、一个只能被另一个 ticket 拥有的工作满足的标准、以及一个复述请求而非从工件推导的标准。垂直切片防掉大部分——一个交付先前不存在行为的切片，在基础提交时按构造就是红的——但这个检查值得手工做。对每条标准，说出会证明它为假的观察，并确认它在实现者起跑的那个提交上确实失败。

**tickets 已发布。我到底怎么跑它们？**
skill 停在工件处，没有自动派发模式。派发是手工的：看板，数没有未关闭阻塞项的 tickets，开那么多场 Agent 会话。一个全新上下文一个 ticket，之间清掉。注意 [implement](https://aihero.dev/skills-implement) 完成后不会可靠地关闭或勾掉 ticket——GitHub 上或本地 markdown 里都不行——所以 ticket 的状态要你自己更新。

## 有效的标志

- 每个 ticket 都能回答"这个完成后我能演示什么？"——而答案是一个行为，不是一层。
- 在发布任何东西之前，列表以编号形式回到你手里，每个带一行 "Blocked by"。
- 顶部的 ticket 没有阻塞项，可以立即开始。
- ticket 正文里没有文件路径或行号，除非是原型产出的片段。
- 每个 ticket 读起来像一场新会话能在你不在场的情况下完成的东西。
- 预重构——如果有找到任何——排在顺序最前，而不是混进功能 tickets。

## 在系统中的位置

`to-tickets` 是主构建链中的一步：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

上游是 [to-spec](https://aihero.dev/skills-to-spec)，递给它一份定稿的规格来切片——把两者都留在同一个不断裂的上下文窗口里。下游是 [implement](https://aihero.dev/skills-implement)，每个全新会话构建一个 ticket，驱动 [tdd](https://aihero.dev/skills-tdd) 写测试、以 [code-review](https://aihero.dev/skills-code-review) 收尾。拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
