快速开始：

```bash
npx skills add mattpocock/skills --skill=resolving-merge-conflicts
```

```bash
npx skills update resolving-merge-conflicts
```

[Source](https://github.com/mattpocock/skills/tree/main/skills/engineering/resolving-merge-conflicts)

## 功能说明

`resolving-merge-conflicts` 逐个处理进行中的 git merge 或 rebase 冲突，逐块解决，并完成整个操作 —— 解决完毕、检查完毕、提交完毕。

它按**意图**而非文本来解决。在处理每个冲突块之前，它会将每一侧的变更追溯到**一手资料**—— commit message、PR、原始 issue —— 以理解变更的目的，然后在两者兼容的地方同时保留双方的意图。它绝不会为了掩盖冲突而发明新行为，也绝不会使用 `--abort`：merge 始终会完成。

## 何时使用

输入 `/resolving-merge-conflicts`，或者当任务适合时 Agent 会自动触发。

当你在 merge 或 rebase 过程中，git 因为无法自动解决的冲突而卡住时，使用它。它处理的是眼前的冲突 —— 不是规划 merge 或调试之后出现的问题行为。如果 merge 已经完成但某些东西现在出了问题且原因不明，请使用 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) 。

## 按意图解决

冲突处理中的一个陷阱是将其视为文本问题 —— 选择"ours"或"theirs"让冲突标记消失。本 skill 将其视为**意图**问题。每个冲突块的每一侧都存在，是因为有人想要达成某个目的；解决方案必须在可能的地方尊重双方的意图，而在确实无法兼容时，选择符合 merge 声明的目标的那一侧，并明确记录这个取舍。

这就是为什么一手资料如此重要。你无法保留自己没读过的意图，因此工作从历史中开始 —— commit、PR、ticket —— 而不是从 diff 开始。

## 有效的标志

- 每个已解决的冲突块保留了双方的行为，或者在无法保留时指明了取舍。
- 没有出现任何一个分支上都不存在的新行为。
- 项目自身的检查 —— 类型检查、测试、格式 —— 已在提交之前找到并全部通过。
- merge 或 rebase 一直执行到了完成提交，从未中断。

## 在系统中的位置

一个随时可用的独立工具：你在 merge 或 rebase 卡住的时刻调用它，它交还给你一个干净、已提交的树。它的天然邻居是 [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) ，因为一个干净解决但之后行为异常的 merge，是诊断问题而非冲突问题。当你拿不准哪个 skill 或流程合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 会为你导航。
