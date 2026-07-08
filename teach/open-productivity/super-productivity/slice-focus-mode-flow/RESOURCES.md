# Focus session、break、metric 与当前任务追踪联动全链路资源

## 知识

- `src/app/features/focus-mode/focus-mode.model.ts`
  Focus timer、screen、mode 与 strategy 接口。适用于辨认 `timer.purpose`、`FocusScreen`、`FocusModeStrategy` 边界。
- `src/app/features/focus-mode/store/focus-mode.actions.ts`
  session / break / overlay 的 action 清单。适用于判断用户操作最终会 dispatch 什么。
- `src/app/features/focus-mode/store/focus-mode.reducer.ts`
  timer 状态机与 screen 切换。适用于确认 tick 停止、session 完成、break 开始/结束如何改 state。
- `src/app/features/focus-mode/store/focus-mode.effects.ts`
  focus 与 tracking 双向同步、break 自动启动、metric 写入、idle 暂停的主 effect 文件。
- `src/app/features/focus-mode/focus-mode-strategies.ts`
  Pomodoro / Flowtime / Countdown 策略差异。适用于判断 break 是否自动开始、下一 session 是否自动续上。
- `src/app/features/focus-mode/focus-mode-overlay/focus-mode-overlay.component.ts`
  专注 overlay 壳层入口。适用于区分 overlay UI 与 store 状态来源。
- `src/app/features/tasks/task.service.ts`
  `currentTaskId$` 与 wall-clock tick 入口。适用于追踪 play/pause 如何驱动 focus effects。
- `src/app/features/tasks/store/task.actions.ts`
  `setCurrentTask` / `unsetCurrentTask` 定义。适用于确认 current task 是本地 UI 状态、不带 persistent meta。
- `src/app/features/metric/metric.service.ts`
  `logFocusSession` 服务入口。适用于确认 session 完成后的 metric 写入门槛。
- `src/app/features/metric/store/metric.reducer.ts`
  `logFocusSession` reducer。适用于确认 focus session 如何追加到 `Metric.focusSessions`。
- `src/app/features/idle/store/idle.actions.ts`
  `openIdleDialog` action 形状。适用于确认 idle 弹窗携带 `wasFocusSessionRunning` 等上下文。
- `src/app/features/config/store/global-config.reducer.ts`
  `selectFocusModeConfig` 与 Pomodoro 配置。适用于读取 `autoStartFocusOnPlay`、`isPauseTrackingDuringBreak` 等开关。

## 智慧（社区）

- Super Productivity 上游 Issues（focus mode / pomodoro / idle 标签）
  适用于验证 break 与 tracking 竞态、overtime、Android 恢复等历史 bug 的真实用户场景。
- 本仓库相邻 L1 `teach/open-productivity/super-productivity/module-planning-time/`
  适用于回看 focus、idle、time-tracking、metric 在时间模块中的边界。
- 相关 L2 `teach/open-productivity/super-productivity/slice-time-tracking-flow/`
  适用于区分 current task 追踪与 persistent time-tracking op-log 写入。
- Super Productivity `docs/documentation-guide.md`
  适用于对照用户可见文案与 focus mode 设置项名称。

## 空白

- 未纳入 Android `FocusModeForegroundService` 与 WebView restore 的完整 native 协议；本主题只标出 `restoreFocusSessionFromNative` action 存在。
- 未纳入 tick 音效、白噪音、Electron taskbar progress 的实现细节。
- 未纳入 metric 图表与简单计数器统计；本主题只覆盖 `logFocusSession` 写入路径。
