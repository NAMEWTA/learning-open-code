# 使命：前台、后台与链式运行核心模块

## 为什么
学习者需要在不逐函数迷失的前提下，读懂 `pi-subagents` 的执行内核边界：一次 `subagent` 调用如何被分流到前台 single、parallel、chain，何时转为后台 async，以及后台结果如何被 status/wait 找回。掌握这个 L1 模块后，后续才能有把握地进入 L2 垂直切片调试。

## 成功的样子
- 能用一句话说明 runs 模块在整体架构中的职责。
- 能区分 `foreground`、`background`、`shared` 三层的输入、输出和依赖边界。
- 能从一次简单调用判断它会进入 single、parallel、chain 还是 async 路径。
- 能根据测试文件找到对应行为的佐证，而不是只凭源码猜测。

## 约束条件
- 本次只建立 L1 模块边界，不做逐函数穷尽。
- lesson 必须控制在 15 分钟内完成；长文件索引和子系统表放入 reference。
- 只写入 `teach/open-ai-agent/pi-subagents/module-runs-execution/`，不修改项目进度文件或其他主题目录。

## 不在范围内
- 不展开 Pi extension 注册入口、agent discovery、slash/RPC/intercom 的完整实现。
- 不逐行讲解 `subagent-executor.ts`、`subagent-runner.ts` 或每个 shared helper。
- 不在本课覆盖 scheduled runs、native supervisor、acceptance 细节和 worktree 深层实现。
