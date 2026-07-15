快速开始：

```bash
npx skills add mattpocock/skills --skill=prototype
```

```bash
npx skills update prototype
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype)

## 功能说明

`prototype` 构建一个小型、可丢弃的程序，其唯一目的就是回答一个设计问题 —— 比如"这个状态模型感觉对吗？"或"这个 UI 应该长什么样？"。

代码从**第一天起就是可丢弃的**，并且会标注清楚。它不包含测试、除了能让程序跑起来之外没有错误处理、没有抽象、也没有持久化。重点是快速学到东西然后删除它 —— 因此，一旦你开始加固它，你就已经不是在 prototype 了。

## 何时使用

输入 `/prototype`，或者当任务适合时 Agent 会自动触发。

当你在纸上难以确定一个设计问题时使用它 —— 比如一个你无法在脑海中理清的分支状态机，或者一个在你看到几个版本并排对比之前无法想象的屏幕。如果某个已经构建好的东西行为异常，你需要找出原因，请使用 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) ；prototype 探索的是要构建什么，而不是为什么已构建的东西出了问题。

## 两种形态

问题决定了形态，有两种形态：

- **"这个逻辑 / 状态模型感觉对吗？"** —— 一个微小的交互式终端应用，将状态机推入各种棘手的情况，每次操作后打印完整状态，让你能看到什么发生了变化。
- **"这个应该长什么样？"** —— 在同一条路由上呈现几个截然不同的 UI 变体，通过浮动栏切换，让你比较真实的渲染效果而不是凭空想象。

选错了形态会浪费整个 prototype，所以问题必须放在第一位。两种形态都保持状态在内存中，通过一条命令运行，每一步都会展示完整状态。

## 答案才是产出物

代码是可丢弃的；**答案**才是唯一值得保留的东西。当 prototype 解答了它的问题后，将结论记录到某个持久的地方 —— 一条 commit message、一份 ADR、一个 issue，或者旁边的 `NOTES.md` —— 连同它回答的问题一起记录，然后删除或吸收代码。一个遗留在仓库中的 prototype 已经失去了它的用途。

## 在系统中的位置

`prototype` 是一个随时可用的独立工具：你用它来解决一个设计问题，然后退出。它的答案通常为下一步提供输入 —— 一个经过验证的状态模型或 UI 方向可以作为确定的输入，交给 [to-spec](https://aihero.dev/skills-to-spec) 来撰写，或者作为一个值得记录的架构决策，通过 [domain-modeling](https://aihero.dev/skills-domain-modeling) 来处理。当你拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
