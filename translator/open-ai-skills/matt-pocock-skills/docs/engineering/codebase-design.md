## 功能说明

`codebase-design` 固定你设计模块时使用的词语：**module**（模块）、**interface**（接口）、**depth**（深度）、**seam**（接缝）、**adapter**（适配器）、**leverage**（杠杆率）、**locality**（局部性）。它精确地定义每一个词，禁用含糊的替代品（"component"、"service"、"API"、"boundary"），并陈述由它们推导出的少数几条原则。

它是一个参考，而非流程。没有要跑的循环、没有产出的工件、没有向你提问的检查点。其他所有涉及设计的 skill 都借用它的词汇；单独使用时，它把语言给你，然后停下。这是你在调用它之前需要知道的事——因为一个没有流程、没有停止规则的 skill，如果你把一场 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 指向它并说"开始"，它就会临时编造一个——见下面的问题。

## 何时使用

输入 `/codebase-design`，或在任务合适时 Agent 会自动调用它。

当你已经知道要重新设计哪段代码、需要思考它的形状时使用它：接缝放在哪里、接口能缩到多小、一次抽取是否在赚取它的存在价值。它也是你用来平息"某个词到底是什么意思"争论的工具。

有几个 skill 和它很接近。你想要哪个取决于实际的问题是什么：

| 问题 | skill |
|---|---|
| 单个模块的形状——它的接口、接缝、深度 | `codebase-design` |
| *领域的词语*——"account" 有三种含义，两个人对"cancellation" 的意思不同 | [domain-modeling](https://aihero.dev/skills-domain-modeling) |
| 你还不知道该重新设计*哪个*模块 | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture)——负责找候选的普查 |
| 你希望设计被辩论，而不只是被命名 | [grilling](https://aihero.dev/skills-grilling) |
| 有一个具体的行为要构建，你想要能在重构中存活的测试 | [tdd](https://aihero.dev/skills-tdd) |

## 词汇表

词汇表就是整个 skill。每个术语都相对于其他术语定义，每个词都带着它所替代的词。

| 术语 | 含义 | 不要再说 |
|---|---|---|
| **Module** | 任何拥有接口和实现的东西。刻意与规模无关——一个函数、一个类、一个包、一个横跨各层的切片都可以。 | unit、component、service |
| **Interface** | 调用者要正确使用它必须知道的一切：类型签名，加上不变量、顺序约束、错误模式、所需配置、性能特征。 | API、signature |
| **Depth** | 接口处的杠杆率——调用者或测试每学习一个单位接口能撬动多少行为。**深层**：小接口背后藏大量行为。**浅层**：接口几乎和实现一样复杂。 | — |
| **Seam** | Michael Feathers 的术语：一个不用在该处编辑就能改变行为的地方。它是接口的*位置*，把它放在哪里本身就是一个独立的决策，与接口背后放什么分开。 | boundary |
| **Adapter** | 在接缝处满足某个接口的具体事物。命名的是角色而非本质——一个内存 fake 和一个 Postgres 仓库都是适配器。 | — |
| **Leverage** | 调用者从深度中得到的东西：每学习一个单位接口，获得更多能力。 | — |
| **Locality** | 维护者从深度中得到的东西：变更、bug 和验证集中在一处。修一次，处处已修。 | — |

深度刻意*不*定义为实现行数与接口行数之比——那是 Ousterhout 自己的定义。那个度量会奖励注水的实现。这里改用"深度即杠杆率"。

## 四条原则

- **深度是接口的属性，而非实现的属性。** 一个深层模块内部可以由小型、可替换的部件构成，只要它们不浮现给调用者。一个模块可以拥有自己的测试所用的内部接缝，以及接口处的一个外部接缝。
- **删除测试。** 想象删除这个模块。如果复杂度随之消失，它是个传递层；如果复杂度在 N 个调用者中重新出现，那它一直在赚取自己的存在价值。
- **接口就是测试面。** 调用者和测试穿越同一道接缝。如果你想*越过*接口测试，这个模块的形状就错了。
- **一个适配器意味着假设的接缝；两个适配器意味着真正的接缝。** 在有东西真正跨接缝变化之前，不要切出接缝。单适配器的接缝只是间接层。

两份辅助文件更进一步，skill 按需读取而非提前加载。[DEEPENING.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/DEEPENING.md) 对候选模块的依赖进行分类——进程内、本地可替换、远程但自有、真正外部——因为类别决定了加深后的模块如何跨接缝测试。[DESIGN-IT-TWICE.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/DESIGN-IT-TWICE.md) 启动并行的 [子代理](https://www.aihero.dev/ai-coding-dictionary/subagent)，为同一个模块产出三个或更多截然不同的接口，然后在深度、局部性和接缝位置上比较它们。

## 常见问题

**我到底怎么在 TypeScript 里构建一个深层模块？**

这是关于本 skill 被问得最多的问题，而 skill 本身不回答它。它定义深层模块*是什么*；它不谈论如何阻止一个游荡的 import 越过接口。[Issue #458](https://github.com/mattpocock/skills/issues/458) 说得很直白："假设我们对接口满意，它隐藏了细节，等等。但我们怎么强制它？我觉得没有 lint 或清晰的护栏，人类和 LLM 都会随着时间把它搞乱。"Matt 在那条讨论串里的回答是三个选项：用 class 或 IIFE 包起来，接受 class 变得巨大；把它做成 monorepo 里的一个包，接受 monorepo 工具链；或者用 [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) 之类的 linter 禁止绕过接口的 import。他还单独说过 Effect 是最好的机制，dependency-cruiser 排第二。仓库的 `in-progress/` 分类里有一个 `setup-ts-deep-modules` skill，会铺下一套 `src/packages/<name>/index.ts` 约定，但它是一个没有文档页的 beta 渠道 skill，而且没有附带 lint 规则。

**我把它指向一场会话，它在重设计我从没提过的东西上烧掉了 10 万 [token](https://www.aihero.dev/ai-coding-dictionary/token)。**

已知问题，已归档为 [issue #449](https://github.com/mattpocock/skills/issues/449)。这个 skill 是模型调用的，自我介绍是词汇表，但里面没有任何东西硬性阻止 Agent 把它当成可运行的流程。一个 Agent 被指示"在 /codebase-design 里继续，推进未决决策"后，伸手去够它能找到的最具行动形状的内容——`DESIGN-IT-TWICE.md` 里的并行子代理——重新探索了之前的会话已经映射过的代码，跑了很远才开始提问。驱动型 skill 才有的护栏（检查点、一次只问一个问题、不自动推进）这里一样都没有，因为参考型 skill 本来就没有。变通办法是点名一个驱动型 skill，让这个垫在它下面：`/grill-with-docs`、`/improve-codebase-architecture` 或 `/tdd` 以 `codebase-design` 为词汇表。issue 仍是开放的。

**`design-an-interface` 去哪了？还有 `/interface-design` 这个 skill 吗？**

`design-an-interface` 被移除并吸收进本 skill。什么都没丢：它的"设计两次"技巧——并行子代理生成截然不同的设计，源自 Ousterhout——以 `DESIGN-IT-TWICE.md` 的形式随本 skill 发布。另外，有几个人问过要一个专门的 `/interface-design` skill 来承载深层模块/薄接口哲学；那个哲学已经在这里了，没有计划另立 skill。如果你是在找这两个名字中的任何一个，这一页就是你要找的。

**这难道不是一套文件结构约定——文件夹、barrel 文件、feature 切片？**

不是，而 skill 在反复的质疑下坚持这条线。[Issue #95](https://github.com/mattpocock/skills/issues/95) 提出把形式化的分形树文件结构作为深层模块的具体实现；答复是两者正交——"深层模块关乎接口的设计和通过严格接口访问，与文件系统长什么样无关。用这种方法完全可能做出浅层模块。"同样的事在 #458 里也出现过："我觉得你可能把模块概念和文件系统绑得太紧了。文件系统当然可以是模块形状的有用提示，但构造深层模块没有必要使用文件系统。"词汇表刻意把 **module** 定义为与规模无关。

**`tdd` 真的在用这套词汇吗？**

现在用了。很长时间里它没有。曾经内联在 `tdd` 里的深层模块笔记在 v1.0 中被移除，换成了这个共享 skill，但替换它们的指针从未被加上——所以 `tdd` 为自己定义 "seam"，什么都不引用。这个缺口现在补上了：指针已进入 skill，在接口的形状（而非测试）成为开放问题时被触达。`tdd` 仍然拥有 "seam" 作为你*测试*所针对的边界；本 skill 拥有它背后的模块形状。

**设计两次的模式在 Claude Code 之外能用吗？**

不能干净地用。`DESIGN-IT-TWICE.md` 写的是"使用 Agent 工具并行生成 3 个以上子代理"，那是 Claude Code 以自己的名字命名的 [工具](https://www.aihero.dev/ai-coding-dictionary/tool)。仓库为其他 [工具链](https://www.aihero.dev/ai-coding-dictionary/harness)（包括 Codex）发布了元数据，而那些工具链下可能没有同名的东西——所以并行设计阶段的可移植性不如 skill 的元数据所暗示的。跟踪于 [issue #564](https://github.com/mattpocock/skills/issues/564)，开放中。

**我能往词汇表里加自己的概念吗——connascence（耦合度）、module secrets（模块秘密）、[progressive disclosure](https://www.aihero.dev/ai-coding-dictionary/progressive-disclosure)（渐进式披露）？**

有人正是这么提议的。[Issue #180](https://github.com/mattpocock/skills/issues/180) 提议把 Parnas 的模块秘密和 Page-Jones 的 connascence 作为命名层，用来描述*什么*正跨接缝泄漏，并附了一份可用的 diff；[issue #303](https://github.com/mattpocock/skills/issues/303) 提议在实现内部使用渐进式披露，这样公共接口深处但底下不是一块无差别的石板。两者都开放、未合并。发布的词汇表刻意很小，它保持小的原因写在 skill 自己里面：一致的语言才是全部意义所在，一个没人一致使用的术语比没有术语更糟。

## 有效的标志

- 设计对话不再产出 "component"、"service" 和 "boundary"，开始产出 "module"、"interface" 和 "seam"。
- 有人能指着一次提议的抽取，毫不犹豫地说它是否通过删除测试。
- 一个提议的接缝附带第二个具名的适配器，而不只是第一个。
- 对接口的讨论涵盖不变量、顺序和错误模式——不只是类型签名。
- 调用它不会开启一场会话。如果 Agent 仅凭 `/codebase-design` 就开始读文件、提议重构，它就把参考误当成驱动了。

## 在系统中的位置

`codebase-design` 是**随时可取的独立 skill**，是工程类 skill 之下的词汇层，而非任何链条中的一步。它最近的邻居是 [domain-modeling](https://aihero.dev/skills-domain-modeling)——面向*问题领域*词语的平行参考，而不是模块的形状——两者通常需要一起用，因为把一个深层模块命名好需要两者。[improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) 是另一个：它普查代码库找加深候选，并全部用这套词汇书写，所以它负责找到模块，而本 skill 是你设计它时的工作台。拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
