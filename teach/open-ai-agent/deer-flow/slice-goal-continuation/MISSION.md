# 使命：run goal 自动续跑

## 为什么
我在 deer-flow 里用 `/goal` 让 agent 朝一个长期目标持续工作，但一次可见回合结束后系统有时还会悄悄再跑几轮。需要弄清 worker 如何在 run 结束时检测 goal 状态、何时触发隐藏续跑、何时 stand down，才能排查「目标没达成却不续跑」或「空转续跑」。

## 成功的样子
- 能按顺序画出：可见回合结束 → 读 checkpoint goal → evaluator 判定 → 写回 `last_evaluation` → 可选隐藏 `HumanMessage` 续跑
- 能解释 `goal_not_met_yet` 与 `needs_user_input` 等 blocker 对续跑决策的差异
- 能指出 `continuation_count` 与 `no_progress_count` 两道熔断各自防什么

## 约束条件
- L2 垂直切片：只跟 worker 内的 goal continuation 主链路
- 单节短课 15 分钟内，细节查参考页

## 不在范围内
- 前端 `/goal` 输入框与 `input-box-helpers.ts` 的 UI 实现
- TUI、IM channel 上 `/goal` 命令的交互细节
- evaluator 所用模型的选型与 prompt 调参
