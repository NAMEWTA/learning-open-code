## 功能说明

`tdd` 以测试优先的方式构建功能或修复 bug：一个失败的测试，然后刚好够让它通过的代码，接着下一个行为。它承载着让那个循环产出值得留存的测试的标准——好测试是什么、测试放哪里、mock 是干什么的、以及悄悄毁掉一套测试的三个反模式。

它不会在你没有先同意的接缝上写任何测试。在任何测试存在之前，它点名打算测试的公共边界，然后停下等你确认——因为测试精力是有限的，而你正把它花在关键路径上，而不是每个边界情况上。另一件要知道的事是：`tdd` 是**参考**，不是驱动器。它持有循环的规则，而别的东西（你，或 [implement](https://aihero.dev/skills-implement)）运行应用这些规则的 [会话](https://www.aihero.dev/ai-coding-dictionary/session)。

## 何时使用

输入 `/tdd`，或在任务合适时 [Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 会自动调用它——以测试优先的方式构建功能或修复 bug，或当你说"red-green-refactor"时。

当有一个具体行为要构建、带输入和可观察的输出、而你想要能在重构中存活的测试时使用它。

| 你的情况 | 去哪里 |
| --- | --- |
| 一个有定义输入输出的行为——业务逻辑、请求/响应契约、变换、校验 | `tdd` |
| 行为还没被钉死 | [to-spec](https://aihero.dev/skills-to-spec)，它也会在写任何代码之前约定测试接缝 |
| 问题其实是接口的形状，不是测试 | [codebase-design](https://aihero.dev/skills-codebase-design) |
| 你有一份 [规格](https://www.aihero.dev/ai-coding-dictionary/spec) 或 [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket)，想要整个构建替你跑完 | [implement](https://aihero.dev/skills-implement)，它按 ticket 驱动 `tdd` |
| 配置、接线、胶水、类型注解、纯 CRUD 委托 | 这里没什么合适——见下方的开放缺口 |

最后一行是一个真实的洞，不是风格偏好。skill 决定接缝*放在哪里*；里面没有任何东西决定一个变更*是否*值得这个循环。把它跑在一个没有独立真值来源可断言的变更上，你会得到一个复述实现的测试——skill 自己警告的同义反复反模式，从另一个方向到达。它是 [issue #746](https://github.com/mattpocock/skills/issues/746)，开放中。在它关闭之前，那个判断是你或你的 `CLAUDE.md` 的。

## 前置条件

需要安装 [codebase-design](https://aihero.dev/skills-codebase-design)。`tdd` 以前自带自己的深层模块和接口设计笔记；v1.0 里那些被删除，换成共享 skill，`tdd` 现在靠它提供接口设计词汇。其他什么都不需要——skill 是 [无状态的](https://www.aihero.dev/ai-coding-dictionary/stateless)，不写任何自己的文件。

## 循环，以及它运行的接缝

三个词承载这个 skill。

**红绿。** 写失败的测试，然后只写刚好够通过的代码。不要预想下一个之后的测试。没有重构阶段：它在 2026 年 6 月被砍掉，因为 Agent 实际上从不去做它，也因为审查和实现作为分开的会话工作得更好。重构属于 [code-review](https://aihero.dev/skills-code-review)。

**垂直切片。** 一个接缝、一个测试、一个最小实现，然后重复——第一个循环是证明单一路径端到端的**曳光弹**。反面是水平切片：先全部测试，再全部代码。批量测试验证的是*想象中*的行为，它们检查东西的形状而不是用户做什么，而且让你在理解实现之前就承诺了一套测试结构。

**预先约定的接缝。** 接缝是你不用伸进内部就能观察行为的公共边界。规则是绝对的：不在未确认的接缝上写测试。在完整链条里，接缝更早、在 [to-spec](https://aihero.dev/skills-to-spec) 期间就约定好了——"`/tdd` 被告知只在预先约定的测试接缝工作，`/code-review` 检查是否只用过约定的测试接缝"。单独调用时，`tdd` 直接问你。

它写来要防止的三个反模式：

| 反模式 | 征兆 |
| --- | --- |
| 实现耦合 | 重命名内部函数时测试坏了，尽管行为没变。mock 内部协作者、断言调用次数、用数据库查询来验证而不是用接口。 |
| 同义反复 | 期望值按代码计算它的方式计算，所以测试靠构造通过。期望值必须来自别处——已知正确的字面量、手工演算的例子、规格。 |
| 水平切片 | 任何实现之前先落下一批测试。 |

Mock 只用于系统边界——外部 API、时间、随机性，有时是文件系统或数据库。不用来包自己的模块。

## 常见问题

**它为什么不重构？描述写着"red-green-refactor"。**

因为重构步骤被移除了，而描述没有。移除是刻意的：Agent 实际上从不去做它，而且把实现和审查放在分开的会话里工作得更好。结果还算不算书上的 TDD，不如循环是否产出更好的代码重要。触发短语和正文之间的错位被归档为 [issue #589](https://github.com/mattpocock/skills/issues/589)，仍然开放，所以 "red-green-refactor" 继续作为触发 skill 的短语工作。你得到的是红 → 绿，重构在 [code-review](https://aihero.dev/skills-code-review) 里。

**它让我选测试接缝，而我完全不知道选哪个。**

这是与本 skill 摩擦最多的报告（[issue #607](https://github.com/mattpocock/skills/issues/607)）。提示只按名列出候选接缝，不说明每个接缝能抓住什么、会漏掉什么，所以你在标签之间做选择。还没有发布修复。实际的变通办法是先让 Agent 说清取舍再回答——组件级接缝会漏掉什么集成级接缝能抓住的，以及它慢多少。这也是链条在 `to-spec` 里提前约定接缝的原因，那时你面前是完整功能而不是一条提示。

**它先写了实现后写测试，尽管 skill 说红在先。**

确实会发生。一位用户拿 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 追问，得到了一份异常诚实的回答："我知道 skill 说'一次一个测试，看它为正确的原因失败'——我读到了。我只是默认了我的日常习惯。"skill 就是为与这件事共存而写的。没有指令能让 Agent 100% 服从，而更用力地强制这个点会以很小收益限制 Agent 的创造力——即使不被严格遵守，循环也值得跑，因为结果总体上仍然更好。如果某一片严格服从很重要，盯紧运行，而不是指望 skill 强制它。

**它应该先写浏览器或端到端测试吗？**

通常不应该，而 skill 也不会拦住它。有位用户报告 Agent 先写了一个 Playwright 测试，然后烧了很长一个循环重跑它，对一个还不存在的功能下了"测试坏了"的结论。在你的 `CLAUDE.md` 里配置这一点。浏览器测试慢到红绿反馈循环不再值回票价；在你的仓库 `CLAUDE.md` 里声明它们在行为工作之后才写。

**`/tdd` 取代 `/implement` 或课程的 `/do-work` 吗？**

不。`/tdd` 记录方法论；`/implement` 是一个非常简单的工作→反馈→提交循环，是 `/do-work` 的直接替代。课程里单一的 `/do-work` 步骤现在分跨 `/implement`、`/tdd` 和 `/code-review`。如果你在问对一个 ticket 该跑哪个，答案几乎总是 `/implement`。

**深度模块和接口设计指引去哪了？**

v1.0 里进了 [codebase-design](https://aihero.dev/skills-codebase-design)，被泛化，让几个 skill 共享一套词汇。`refactoring.md` 同时离开；重构现在是 [code-review](https://aihero.dev/skills-code-review) 的职责，那个 skill 带着 Fowler 坏味道基线。

**它知道我其他 tickets 吗？**

不知道。对着一个 ticket 跑，它会乐意提议属于兄弟 ticket 的工作，因为它看不到 issue 图的其他部分（[issue #129](https://github.com/mattpocock/skills/issues/129)）。Matt 的立场是这不是 `tdd` 的职责。把规格和 ticket 一起传有帮助；一开始就把 tickets 切到合适大小帮助更大。

## 有效的标志

- 在任何测试文件存在之前，它停下、点名打算测试的接缝、然后等待。
- 出现一个测试，变红，得到刚好够的代码通过，然后才出现下一个测试——不是一批测试跟着一批代码。
- 测试名读起来是能力（"user can checkout with valid cart"），而不是内部实现（"checkout calls paymentService.process"）。
- 断言里的期望值是你能追溯到规格的字面量，不是按代码计算方式重算出来的值。
- 重命名一个内部函数不破坏套件里的任何东西。
- Mock 只出现在外部边界——支付 API、时钟——绝不包着自己的模块。

## 在系统中的位置

`tdd` 是主链构建步骤内部的引擎，而不是自己的步骤：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

[to-spec](https://aihero.dev/skills-to-spec) 提前约定测试接缝，[implement](https://aihero.dev/skills-implement) 按 ticket 驱动 `tdd`，[code-review](https://aihero.dev/skills-code-review) 事后检查只用过约定的接缝——并拥有 `tdd` 不再做的重构。它另一个邻居是 [codebase-design](https://aihero.dev/skills-codebase-design)，`tdd` 所说的接缝和深层模块词汇的共享来源。你也可以单独够它，任何时候有一个具体行为要建、又没有完整规格在场。拿不准哪个 skill 适合你的情况时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
