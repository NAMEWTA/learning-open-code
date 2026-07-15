<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

# 面向实战工程师的技能集

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

我每天都在使用的 agent skill——用于真正的工程开发，而非 vibe coding。

开发真实应用是困难的。GSD、BMAD 和 Spec-Kit 等方法试图通过掌控流程来提供帮助。但在这样做的过程中，它们剥夺了你的控制权，并使流程中的 bug 难以解决。

这些 skill 的设计理念是：小巧、易于适配、可组合。它们适用于任何模型，基于数十年的工程经验。随意修改它们，让它们为你所用。享受吧。

如果你想及时了解这些 skill 的更新以及我创建的任何新 skill，可以加入我 newsletter 上的约 60,000 名开发者：

[订阅 Newsletter](https://www.aihero.dev/s/skills-newsletter)

## 快速开始（30 秒设置）

1. 运行 skills.sh 安装器：

```bash
npx skills@latest add mattpocock/skills
```

2. 选择你想要的 skill，以及想将它们安装到哪些编码 agent 上。**确保选择 `/setup-matt-pocock-skills`**。

3. 在你的 agent 中运行 `/setup-matt-pocock-skills`。它会：
   - 询问你想使用哪个 issue tracker（GitHub、Linear 或本地文件）
   - 询问你在分类票据时使用什么标签（`/triage` 使用标签）
   - 询问你想将我们创建的文档保存在哪里

4. 好了——你已经准备好了。

## 这些 Skill 为什么存在

我构建这些 skill 是为了修复我在 Claude Code、Codex 和其他编码 agent 中看到的常见失败模式。

### #1：Agent 没按我的想法做

> "没有人确切知道自己想要什么"
>
> David Thomas & Andrew Hunt，[《程序员修炼之道》](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**。软件开发中最常见的失败模式是对齐偏差。你以为开发者知道你想要什么，然后你看到他们构建的东西——才意识到它完全没理解你。

这在 AI 时代也是一样的。你和 agent 之间存在沟通鸿沟。解决方法是**问答式访谈（grilling session）**——让 agent 向你详细询问你正在构建什么。

**解决方案**是使用：

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) — 用于非编码场景
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) — 与 [`/grill-me`](./skills/productivity/grill-me/SKILL.md) 相同，但增加了更多好处（见下文）

这些是我最受欢迎的 skill。它们帮助你在开始之前与 agent 对齐，并深入思考你要做的变更。在你*每次*想要进行变更时使用它们。

### #2：Agent 过于啰嗦

> 有了统一语言，开发者之间的对话和代码的表达都源自同一个领域模型。
>
> Eric Evans，[《领域驱动设计》](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**问题**：在项目开始时，开发者和软件的最终用户（领域专家）通常说着不同的语言。

我在使用 agent 时也感受到了同样的张力。Agent 通常被直接放入一个项目，被要求在使用过程中自行摸索行话。于是它们用 20 个词来表达 1 个词就能说清的事。

**解决方案**是共享语言。它是一份文档，帮助 agent 解码项目中使用的行话。

<details>
<summary>
示例
</summary>

这是一个来自我的 `course-video-manager` 仓库的 [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) 示例。哪个更容易阅读？

- **之前**："当课程中某个章节内的课程被设为 'real'（即在文件系统中获得一个位置）时会出现问题"
- **之后**："物化级联存在问题"

这种简洁性在每次会话中都会带来回报。

</details>

这一功能已内置于 [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) 中。它是一个问答式访谈会话，但能帮助你与 AI 建立共享语言，并将难以解释的决策记录在 ADR 中。

很难解释这有多强大。它可能是这个仓库中最酷的单个技术。试一试就知道了。

> [!TIP]
> 共享语言除了减少啰嗦之外还有许多其他好处：
>
> - **变量、函数和文件使用共享语言一致命名**
> - 因此，**代码库对 agent 来说更易于导航**
> - Agent 还**在思考上花费更少的 token**，因为它可以使用更简洁的语言

### #3：代码不能正常工作

> "始终采取小步、有意图的步骤。反馈的速度就是你的速度极限。永远不要承担太大的任务。"
>
> David Thomas & Andrew Hunt，[《程序员修炼之道》](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**问题**：假设你和 agent 就构建什么达成了一致。当 agent *仍然*产出糟糕代码时会发生什么？

是时候审视你的反馈循环了。如果没有关于其产出的代码实际运行情况的反馈，agent 将如同盲飞。

**解决方案**：你需要通常的反馈循环组合：静态类型、浏览器访问和自动化测试。

对于自动化测试，红-绿-重构循环至关重要。这是 agent 先编写一个失败的测试，然后修复测试的过程。这有助于给 agent 提供持续水平的反馈，从而产生好得多的代码。

我构建了一个 **[`/tdd`](./skills/engineering/tdd/SKILL.md) skill**，你可以插入到任何项目中。它鼓励红-绿-重构循环，并为 agent 提供了大量关于什么构成好的测试和坏的测试的指导。

对于调试，我还构建了一个 **[`/diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md)** skill，将最佳调试实践包装成一个简单的循环。

### #4：我们构建了一个泥球

> "每天都投资于系统的设计。"
>
> Kent Beck，[《解析极限编程》](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "最好的模块是深层的。它们允许通过简单的接口访问大量功能。"
>
> John Ousterhout，[《软件设计的哲学》](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**问题**：大多数使用 agent 构建的应用复杂且难以修改。因为 agent 可以极大地加速编码，它们也加速了软件熵。代码库以前所未有的速度变得更加复杂。

**解决方案**是采用一种全新的 AI 驱动开发方法：关心代码的设计。

这已内置于这些 skill 的每一层中：

- [`/to-spec`](./skills/engineering/to-spec/SKILL.md) 在创建 spec 之前询问你将涉及哪些模块

关键的是，[`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) 帮助你拯救已经变成泥球的代码库。我建议每隔几天在你的代码库上运行一次。

### 总结

软件工程基本原理比以往任何时候都更加重要。这些 skill 是我将这些基本原理浓缩为可重复实践的最佳努力，帮助你交付职业生涯中最好的应用。享受吧。

## 参考

这些 skill 沿一个维度划分——谁能调用它们。**用户调用** skill 只能由你输入来访问（如 `/grill-me`）；它们的工作是编排。**模型调用** skill 可以由你调用*或*在任务匹配时由 agent 自动使用；它们承载着可复用的准则。用户调用 skill 可以调用模型调用 skill，但绝不能调用另一个用户调用 skill。

### 工程

我日常编码工作中使用的 skill。

**用户调用**

- **[ask-matt](./skills/engineering/ask-matt/SKILL.md)** — 询问哪个 skill 或工作流适合你的情况。本仓库中用户调用 skill 的路由器。
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — 在问答式访谈会话中同时构建项目的领域模型，打磨术语并内联更新 `CONTEXT.md` 和 ADR。
- **[triage](./skills/engineering/triage/SKILL.md)** — 通过分类角色状态机处理 issues。
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — 扫描代码库寻找深化机会，以可视化 HTML 报告呈现，然后深入讨论你选择的任何一个。
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — 为工程 skill 配置此仓库（issue tracker、分类标签、领域文档布局）。在使用其他工程 skill 之前每个仓库运行一次。
- **[to-spec](./skills/engineering/to-spec/SKILL.md)** — 将当前对话转化为 spec 并发布到 issue tracker。无需访谈——只是综合你已经讨论过的内容。
- **[to-tickets](./skills/engineering/to-tickets/SKILL.md)** — 将任何计划、spec 或对话分解为一组 tracer-bullet 票据，每个声明其阻塞边界——作为本地文件中的文本写入，或作为真实 tracker 上的原生阻塞链接。
- **[implement](./skills/engineering/implement/SKILL.md)** — 构建 spec 或票据集描述的工作，在预先约定的 seam 处驱动 `/tdd`，并在提交前以 `/code-review` 收尾。
- **[wayfinder](./skills/engineering/wayfinder/SKILL.md)** — 规划一大块工作，超过一个 agent 会话所能容纳的量，作为 issue tracker 上的共享调查票据地图——一次解决一个，直到通往目的地的路径清晰。

**模型调用**

- **[prototype](./skills/engineering/prototype/SKILL.md)** — 构建一次性原型来回答设计问题——用于状态/逻辑问题的可运行终端应用，或多种可从同一路由切换的截然不同的 UI 变体。
- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)** — 用于困难 bug 和性能回归的规范化诊断循环：重现 → 最小化 → 假设 → 插桩 → 修复 → 回归测试。
- **[research](./skills/engineering/research/SKILL.md)** — 针对高可信度的主要来源调查问题，并将发现捕获为仓库中的带引用 Markdown 文件，作为后台 agent 运行。
- **[tdd](./skills/engineering/tdd/SKILL.md)** — 使用红-绿-重构循环的测试驱动开发。一次一个垂直切片地构建功能或修复 bug。
- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)** — 主动构建和打磨项目的领域模型——对照词汇表挑战术语、用边界场景压力测试、内联更新 `CONTEXT.md` 和 ADR。
- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)** — 设计深层模块的共享准则和词汇：大量行为放在小接口背后，置于清晰的 seam 处，通过该接口可测试。
- **[code-review](./skills/engineering/code-review/SKILL.md)** — 从固定点开始的 diff 双轴审查：**标准**（是否遵循仓库的编码标准，加上 Fowler 气味基线？）和 **Spec**（是否忠实实现了原始 issue/PRD？），作为并行子 agent 运行，互不污染。

### 生产力

通用工作流工具，不限于编码。

**用户调用**

- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — 接受对计划或设计 relentless 的访谈，直到决策树的每个分支都被解决。
- **[handoff](./skills/productivity/handoff/SKILL.md)** — 将当前对话压缩为交接文档，以便另一个 agent 可以继续工作。
- **[teach](./skills/productivity/teach/SKILL.md)** — 在多个会话中向用户教授新 skill 或概念，使用当前目录作为有状态的教学工作区。
- **[writing-great-skills](./skills/productivity/writing-great-skills/SKILL.md)** — 编写和编辑 skill 的参考：使 skill 可预测的词汇和原则。

**模型调用**

- **[grilling](./skills/productivity/grilling/SKILL.md)** — relentlessly 访谈用户关于计划或设计，直到决策树的每个分支都被解决。`grill-me` 和 `grill-with-docs` 背后的可复用循环。
