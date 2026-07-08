# 教学笔记：前台、后台与链式运行核心模块

- 用户要求所有教学输出使用中文，并严格遵守 `teach` skill 的短课合约。
- 本次只写入 `teach/open-ai-agent/pi-subagents/module-runs-execution/`，不得修改 `_progress.json`、`_progress.md`、`index.md` 或其他主题目录。
- 本 L1 只建立 runs 模块边界；`subagent-executor.ts`、`subagent-runner.ts` 等长文件的逐函数分析留给后续 L2。
- shell 命令需使用 `rtk` 前缀。
