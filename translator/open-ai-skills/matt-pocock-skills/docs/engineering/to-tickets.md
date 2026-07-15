快速开始：

```bash
npx skills add mattpocock/skills --skill=to-tickets
```

```bash
npx skills update to-tickets
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets)

## 功能说明

`to-tickets` 将计划、规范或当前对话拆分为一组 **ticket**——每个都是一个曳光弹式的垂直切片——并发布到你配置的追踪器中，每个 ticket 都会声明阻塞它的那些 ticket。

每个 ticket 都是一个**曳光弹**——一个贯穿所有集成层的薄*垂直*切片（schema、API、UI、测试），永远不是一个只触及单层的水平切片。一个已完成的切片可以独立演示或验证，这使得每个 ticket 都可以安全地交给一个 Agent 处理。

## 何时使用

输入 `/to-tickets` 来调用它——Agent 不会自己触发它。

当你已经有了共识的计划或已写成的规范，并希望将其拆分为 ticket 时使用它。将对话内容指向它，或者传入规范或 issue 引用，它会先抓取正文和评论。如果该变更还没有写成规范，先产出一份规范——此时应使用 [to-spec](https://aihero.dev/skills-to-spec)。

## 前置条件

`to-tickets` 会发布到你的问题追踪器，因此 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) 必须先为当前仓库配置好追踪器及其分类标签词汇。在真实追踪器上，它在发布时会应用 `ready-for-agent` 标签。

## 一份产物，两种读法

阻塞关系是核心所在。它们让同一组 ticket 根据追踪器的不同有两种理解方式：

- **本地文件** → 仓库根目录下一个单一的 `tickets.md`，阻塞关系以文本形式写出。你从上到下手工推进，全程保持参与。
- **真实追踪器（GitHub、Linear）** → 每个 ticket 一个 issue，阻塞关系以原生阻塞链接（或子 issue）表达。任何阻塞项已全部完成的 ticket 处于**前沿**位置，可以被领取——因此可以同时运行多个 Agent。

阻塞边关系在 ticket 中是固定的，无论什么介质；介质只决定是否有人并行地基于它们自动行动。`to-tickets` 产出的是这份产物——你如何运行它（手工顺序推进，或并行舰队）由你决定。

## 垂直切片，而非水平切片

整个技能围绕一个核心区别展开。**水平**切片交付变更的一层——所有 schema，或所有 API——在所有层落地之前，什么都不能工作。**垂直**切片，即曳光弹，一次性交付一条贯穿*所有*层的窄路径，完成的那一刻即可演示。

在拆分之前，`to-tickets` 会寻找预重构——"先让变更变得容易，再做容易的变更"——并将这项工作排在最前面。然后，在发布任何内容之前，它会就拆分方案询问你（粒度、阻塞边、什么该合并或拆分），并在发布时优先发布阻塞项，以便每个 ticket 的"被阻塞于"能引用真实的 ticket。

## 宽幅重构的例外

有一种形态突破了曳光弹规则：**宽幅重构**——一次机械性的变更（重命名列、重定义共享符号），其**爆炸半径**波及整个代码库，以至于单次编辑会同时破坏成千上万的调用点，没有任何垂直切片能独自变绿。`to-tickets` 将其以**扩展-收缩**方式拆分：扩展（在旧形态旁边添加新形态，确保不破坏任何东西），迁移（按爆炸半径分批迁移调用点，每批一个 ticket，全程 CI 保持绿色，因为旧形态依然存在），然后收缩（在没有任何调用者后删除旧形态）。当即使是批次也无法独立保持绿色时，它们共享一个集成分支，所有批次都阻塞最后一个"集成并验证"的 ticket，并仅在那里承诺绿色通过。

## 在系统中的位置

`to-tickets` 是主构建链中的一个步骤：

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review
```

它位于 [to-spec](https://aihero.dev/skills-to-spec)（提供带有用户故事的已确定规范供其拆分）和 [implement](https://aihero.dev/skills-implement)（构建每个 ticket，在内部驱动 [tdd](https://aihero.dev/skills-tdd) 以测试优先方式编写测试，并在其后进行 [code-review](https://aihero.dev/skills-code-review) 审查）之间。在前沿之上，一次一个 ticket，在之间清空上下文。当你不确定哪个技能或流程适合时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
