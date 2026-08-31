## 功能说明

`domain-modeling` 在设计过程中构建并打磨项目的**通用语言**——质疑与词汇表冲突的术语、在你用了含糊词语的地方逼出一个精确的词、用具体场景对关系做压力测试，直到边界精确。

它是**主动**的训练，不是被动的。读 `CONTEXT.md` 借用其词汇是一行习惯，任何 skill 都会；本 skill 用于你正在*改变*模型的时候。这正是它会打断你的原因。它在术语定稿的那一刻、在对话进行中就把定稿的术语写进 `CONTEXT.md`，而不是在结束时交出一份整洁的词汇表——因为批量版是一场 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 的总结，而内联版才是会话真正的产出。

## 何时使用

输入 `/domain-modeling`，或在任务合适时 Agent 会自动调用它。实践中，自动调用是本 skill 最弱的一环：当 `grill-with-docs` 或 `wayfinder` 说要加载它时，[模型](https://www.aihero.dev/ai-coding-dictionary/model) 常常加载了 `grilling` 而跳过了它。如果一场 [质询](https://www.aihero.dev/ai-coding-dictionary/grilling) 会话跑完而 `CONTEXT.md` 末尾未动，那就是发生了这种事——和其他 skill 一起按名调用它。

当*词语*是问题时使用它：

| 情况 | 做法 |
| --- | --- |
| 两个人对 "cancellation" 的意思不同 | `domain-modeling`——选定规范术语，把另一个列在 `_Avoid_` 下 |
| "Account" 在三个文件里干三份活 | `domain-modeling`——把它拆成 Customer 和 User |
| 你刚做了一个难以撤销的架构选择 | `domain-modeling`——如果选择过了门槛，它会提供一个 ADR |
| 问题是模块的*形状*——接缝放哪、接口多深 | [codebase-design](https://aihero.dev/skills-codebase-design) |
| 你想在构建前让整个计划被盘问一遍 | [grill-with-docs](https://aihero.dev/skills-grill-with-docs)，它在底层驱动本 skill |
| 你想查一个术语，而不是改它 | 什么都不用。读 `CONTEXT.md`。它是一个文件。 |

## 前置条件

提前什么都不用准备。skill 写入两个位置，都是惰性创建的：

- **`CONTEXT.md`**，位于仓库根目录，由第一个定稿的术语创建。在根目录有 `CONTEXT-MAP.md` 的仓库里，术语写入地图指向的对应上下文的 `CONTEXT.md`。
- **`docs/adr/`**，由第一个过了门槛的 ADR 创建。

开始之前什么都不需要存在，也没有任何东西会被投机性地创建。

## 两份工件，两道门槛

词汇表和 ADR 被以不同标准对待，而把它们混为一谈正是本 skill 大部分麻烦的来源。

| | `CONTEXT.md` | `docs/adr/NNNN-slug.md` |
| --- | --- | --- |
| 保存 | 术语。一件事**是什么**，一两句话，被拒绝的同义词列在 `_Avoid_` 下 | 一个决策，一到三句话：背景、选择、理由 |
| 写入门槛 | 一个含糊术语变得规范 | **三条全部满足**：难以撤销、没有上下文会让人惊讶、源于真正的权衡 |
| 写入时机 | 内联，术语定稿的那一刻 | 提议，而非默认 |
| 绝不保存 | 实现细节、[规格](https://www.aihero.dev/ai-coding-dictionary/spec)、草稿纸、一般编程概念 | 本会话每个选择的流水账 |

ADR 三条测试缺任何一条，就没有 ADR。容易撤销的决策反正会被撤销；不让人惊讶的决策没人会问；没有真正替代方案的决策，只是记录你做了显而易见的事。

`CONTEXT.md` 那条规则才是真正要抓住的，因为它是实战中会崩的那条。**它只是词汇表，别无其他。**不受约束的话，模型会把"写入 `CONTEXT.md`"当成把你给出的每个答案都持久化的许可，文件就变成一份运行中的规格——这是本 skill 被报告最多的问题，横跨好几个模型。

## 交叉引用，及其边界

让 skill 产生效果的动作是：当你陈述某事如何运作时，它检查代码并浮出矛盾。*"你的代码取消整个 Order，但你刚才说部分取消是可能的——哪个是对的？"*语言和代码被强迫达成一致，而且是在两者任一被改动之前、公开地达成。

边界值得知道。它交叉引用的是**代码**和已提交的 `CONTEXT.md`/ADR，除此之外别无其他。它不搜索你的 issue 追踪器，所以一场几个月前在已关闭 issue 里辩论并刻意定论的命名冲突，会被当作新事浮出水面。有一个 [开放请求](https://github.com/mattpocock/skills/issues/717) 要修复它；在那之前，变通办法是把指令写进你自己的 `docs/agents/domain.md`——skill 们本来就会读它。

## 常见问题

**我的 `CONTEXT.md` 有 500 行。1000 行。3000 行。我该怎么办？**
规模是症状，不是病本身——文件吸收了从来不是词汇表素材的实现细节和决策。修复是一条直接指令：`/grill-with-docs make my CONTEXT.md more concise and remove any implementation details from it`。对一个臃肿的文件跑一遍，大部分内容会消失。只有在文件真正精简、且确实覆盖读者不想同时握在手里的两个领域时，才考虑 `CONTEXT-MAP.md` 拆分；拆一个臃肿的文件只是得到几个臃肿的文件。skill 在这方面的引导还不足以从源头阻止增长，跟踪这个问题的 issue 仍然开放。

**为什么叫 `CONTEXT.md` 而不是 `GLOSSARY.md`？**
这是整套 skill 里被争论最多的命名问题，没有定论。反对现名的理由很扎实：如果它"只是词汇表"，`GLOSSARY.md` 直接说明了这一点，而且——正如一位读者所说——"在 AI 代理的时代，一切都是 [context](https://www.aihero.dev/ai-coding-dictionary/context)"。支持现名的理由是地图：`CONTEXT-MAP.md` 指向多个 `CONTEXT.md` 读起来自然，`GLOSSARY-MAP.md` 就不是；而 `context` 是 DDD 里描述模型有界区域的通行词。至少有一个人维护本地 fork 纯粹是为了改这个文件名。你也可以这么做，但整套里每个其他 skill 都找 `CONTEXT.md`，改名意味着要打补丁改遍它们全部。

**`/ubiquitous-language` 去哪了？**
它被移除了，而且不是废弃。它的职责并入了 `domain-modeling`，后者持续维护整个模型，而不是从一场对话里倒出一份词汇表。词汇强制的承重变多了，而非变少——它现在运行在质询、triage 和制图之下，而不是一次你记得才做的单独操作。

**我怎么给一个没有词汇表的代码库弄一份词汇表？**
主动索要，而不是等它慢慢积累。`/grill-with-docs help me scaffold my existing repo with a CONTEXT.md` 是有据可查的路子；预期一场漫长的盘问——有位用户报告说问了 50 多个问题文件才成形。在棕地仓库上，顺带式使用构建词汇表的速度实在太慢。

**我能保留领域模型、同时用我自己的 ADR 格式吗？**
今天还做不到干净地。词汇表那一半和 ADR 那一半捆绑在一个 skill 里，所以一个已有 ADR 约定的团队——不同的模板、不同的位置、不同的命名——会收到与自家风格冲突的指令。当前选项是本地复制 skill 再编辑，或者在仓库自己的 agent 文档里覆盖 ADR 约定。把两者拆开是一个 [开放请求](https://github.com/mattpocock/skills/issues/557)。

**词汇表真的值回票价吗？它只是又多一件要审查的工件，而且会过时。**
有时它不值，值得诚实地谈谈哪里不值。DDD 越靠近实现就越没用——回报在上游，在命名和概念对齐上，不在聚合和分层仪式里。同义词控制只在命名边界上有意义：模块名、表名、状态枚举、issue 标题、CLI 命令。在普通散文里它意义小得多。还有一个活跃的反对意见：领域术语压缩的是*人与人之间*本来就共享的沟通，而 Agent 对平白英语的描述反应一样——按这种读法，词汇表的价值是让你和你的审查者与 Agent 在做什么保持对齐，而不是让 Agent 变得更好。一天的构建，跳过它。而一份无人审查、Agent 写的词汇表比没有更糟：它变成自信口吻的传说，之后的会话把它当真理。

**它能替我把含糊的提示词变成领域语言吗？**
不能，也没有计划做一个这样的 skill。一种你自己都不理解的领域语言，一旦写下来就成了无意义的胡话。本 skill 在你有了理解之后强制精确——它不制造你没有的词汇。相关的陷阱是用了领域词却不去建模：把对的名词放在错的概念结构上，会产出读起来正确、实则不对的输出。

## 有效的标志

- 它在你说到一半时打断，问你刚才指的是两件事中的哪一件，而不是选一个继续走。
- `CONTEXT.md` 在对话**进行中**变化，而不是结尾来一波。
- 它拒绝为你明天就能撤销的东西写 ADR——并说出三条测试里哪条没通过。
- 新条目用一两句话定义一件事*是什么*，并在 `_Avoid_` 下列出你放弃的词。
- 当你的代码和你的话打架时，它把你的代码引述回来。
- `CONTEXT.md` 变短的次数和变长的次数一样多。

## 在系统中的位置

`domain-modeling` 是一个**模型调用的参考**，它运行在*其他* skill 之下的次数比单独运行多。[grill-with-docs](https://aihero.dev/skills-grill-with-docs) 在质询会话中驱动它，[wayfinder](https://aihero.dev/skills-wayfinder) 在制图时加载它，[triage](https://aihero.dev/skills-triage) 用它让 [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) 使用项目自己的话，[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 在决策结晶时调用它。它最近的姊妹是 [codebase-design](https://aihero.dev/skills-codebase-design)：两者是其他一切之下的词汇层，这个管*领域*，那个管模块的*形状*。它也可以直接触达——当你想只要这门训练、而不承诺通常引入它的那个 skill 的步骤时。拿不准哪个 skill 合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
