快速开始：

```bash
npx skills add mattpocock/skills --skill=diagnosing-bugs
```

```bash
npx skills update diagnosing-bugs
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)

## 功能说明

`diagnosing-bugs` 为疑难 bug 和性能回归执行一套严谨的诊断循环——构建可复现用例、精简用例、排列假说优先级、插桩检测，然后修复并附带回归测试。

在拥有**紧密反馈循环**之前，它拒绝提出任何假设——即一个可运行的命令，已经在*此* bug 上显示红色/失败。在反馈命令存在之前就阅读代码来构建理论，正是此 skill 要防止的失败模式。没有可显示红色的循环，就没有诊断。

## 何时使用

输入 `/diagnosing-bugs`，或在任务合适时 Agent 会自动调用它——它会在"诊断"/"debug 这个"等关键词出现时触发，或当你报告某样东西出现故障、抛出异常、失败或运行缓慢时。

在棘手的问题上使用它：一眼看不出原因的 bug、间歇性的偶发故障、在两个已知良好状态之间悄然出现的回归。对于快速检验设计问题的轻量验证而非追踪缺陷，改用 [prototype](https://aihero.dev/skills-prototype)。

## 紧密循环就是核心

其他一切——二分查找、假说测试、插桩——一旦有了信号就都是机械操作。因此该 skill 在阶段 1 上投入了不成比例的努力：构建一个能驱动实际 bug 代码路径并断言用户所报确切症状的通过/失败命令，然后**收紧**它，直到它快速、确定且 Agent 可直接运行。一个 30 秒且不稳定的循环比没有好不了多少；一个 2 秒且确定的循环才是调试的超能力。

它提供了一套构建该循环的方法阶梯——失败测试、curl 脚本、CLI diff、无头浏览器、重放 trace、一次性辅助工具、模糊测试循环、`git bisect run`、差分运行——并且，仅作为最后手段，一个人工在环的 bash 脚本。对于非确定性 bug，目标不是干净的复现，而是**更高的复现率**：循环触发、并行化、增加压力，直到偶发故障变得可调试。

## 有效的标志

- 在提出理论*之前*先构建并运行一个复现命令——并粘贴该调用及其红色输出。
- 循环断言的是你实际报告的症状，而非邻近的失败。
- 假说以排序后、可证伪的列表形式呈现，并在测试任何假说之前展示给你。
- 调试插桩代码带有标记（`[DEBUG-...]`），并在声明完成前通过 grep 清理干净。

## 在系统中的位置

`diagnosing-bugs` 是一个随时可用的独立 skill——当发现东西坏了时你就投入其中，一旦修复和回归测试完成就退出。当事后复盘发现真正的问题是代码没有良好的接缝来锁定 bug——代码本身而非 bug 才是问题所在——它会移交给 [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture)。当你不确定该用哪个 skill 时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你导航。
