## 功能说明

`resolving-merge-conflicts` 逐块处理进行中的 git merge 或 rebase，然后运行项目自己的检查，以一次提交完成整个操作。

它拒绝把冲突当文本问题处理。在碰任何一个块之前，它把每一侧追溯到它的 **[一手来源](https://www.aihero.dev/ai-coding-dictionary/primary-source)**——提交信息、PR、原始 issue——所以它是在两个意图之间选择，而不是在两块文本之间选择；只要兼容，它就把两者都保留。两者确实不兼容时，它选符合 merge 声明目标的那一侧，并把取舍说出口。它不会发明新行为来掩盖冲突，`--abort` 也不在它的选项里：merge 总是被带到一个完成的提交。

## 何时使用

输入 `/resolving-merge-conflicts`，或在任务合适时 [Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 会自动调用它。

当 git 已经在它自己解决不了的冲突上停下时使用它。它限定在你眼前的冲突上，不碰它任何一侧之外的东西：

| 你的情况 | skill |
| --- | --- |
| merge 或 rebase 中途，树里有冲突标记 | 这一个 |
| merge 已完成，现在有东西行为异常，原因你看不见 | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |
| 规划如何切分工作让分支少碰撞 | 都不是——见下方的并行工作问题 |

## 一手来源优先于 `ours` 和 `theirs`

它存在要杀死的失败模式是按旗标解决：`--ours`、`--theirs`、或手删那个看起来不那么重要的块，让标记消失、构建通过。那种解决在语法上可以完美，仍会悄悄丢掉某个人有意做的改动。

你无法保留一个你没读过的意图。所以工作从历史开始——提交、PR、[ticket](https://www.aihero.dev/ai-coding-dictionary/ticket)——然后才轮到 diff。循环里还有一步出于同样的原因存在：skill 找到仓库自己的 [自动化检查](https://www.aihero.dev/ai-coding-dictionary/automated-check) 并在提交前运行它们，因为 merge 是 git 里最容易产出"两边都满足、两边的测试都不通过"的代码的地方。

## 常见问题

**Claude Code 自己解决冲突已经相当不错了。为什么这还需要一个 skill？**

增值在于"找一手来源"和"跑反馈循环"这两步，否则每次都得手写提示。一个没被提示的 Agent 通常只凭 diff 就能产出说得过去的解决，然后停在那里。skill 的价值是它不让 Agent 跳过的两步——读每一侧为什么存在，之后跑检查。相对于一个好 [模型](https://www.aihero.dev/ai-coding-dictionary/model)，这是薄薄的一层余量，而且它就该是：至少有一位读者预测过，随着模型变好，这整个 skill 会变成一个空操作。

**我该让并行 Agent 避开同一批文件，从源头避免冲突吗？**

大体上不用。在并行任务之间给文件分区，省下的不如花掉的多，因为 Agent 对合并冲突已经足够好，那个权衡不像看起来那么残酷。唯一值得保留的一条纪律是先做大重构。一个大型重命名在十个分支从它分叉之后落地，那才是永远昂贵的情况。

一条来自并行 worktree 用户报告的告诫：当兄弟 [会话](https://www.aihero.dev/ai-coding-dictionary/session) 各自在自己的树里构建一个 ticket 时，合并回去最好由写那个改动的会话来做，因为它才是已经知道意图的那个。把所有人的冲突最后批量堆给一个 Agent，恰好扔掉本 skill 第 2 步不得不去重建的那份 [上下文](https://www.aihero.dev/ai-coding-dictionary/context)。

**为什么永不 `--abort`？**

Abort 扔掉解决工作，下次尝试时把你送回同一个、原样未动的冲突。skill 是为"merge 将要发生"的情况写的。如果你已经决定它不该发生，那是一个调用之前要做的决定，不是循环内部的一个分支。

## 有效的标志

- 解决过程中 Agent 向你引述提交信息、PR 或 issue，而不只是 diff 块。
- 每个块最后都保留两侧的行为，或带一条点明丢了什么、为什么的显式说明。
- 结果里没有出现在任何一侧分支上的东西。
- 类型检查、测试和格式在提交*之前*被找到并跑绿，而不是等你发现坏了之后。
- 你结束在一个干净的树、操作完成——包括多提交 rebase 里剩余的每一个提交。

## 在系统中的位置

一个随时可取的独立工具，不依赖任何其他 skill：git 卡住时它开始，树干净且已提交时它结束。它唯一真正的邻居是 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs)——在"merge 干净地解决了但合并后的代码行为异常"这个点上接手——那是诊断问题，不是冲突问题。它完全站在从想法到交付的主流程之外，所以 [ask-matt](https://aihero.dev/skills-ask-matt) 是它前后该跑什么的地图。
