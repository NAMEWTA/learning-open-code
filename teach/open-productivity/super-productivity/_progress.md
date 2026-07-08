# super-productivity 教学进度

> 最后更新：2026-07-08T10:05:00+08:00

## 总体进度

完成：**30 / 83 goals（36.1%）**

> 本轮（Round 12）收口第三批 L2：Today/Project/Tag 归属、项目完成、远端 op apply、Planner/Schedule 通过审查；并新完成 Focus mode、日历 time block、Android 提醒、Android 分享/Widget 四条 L2 垂直切片。

## 按层级统计

| 层级 | 完成 | 总数 | 说明 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | 已通过审计与复查 |
| L1 模块总览 | 10 | 10 | L1 广度总览已收口 |
| L2 垂直切片 | 20 | 32 | 第四批 +4（iOS WebDAV / PWA / Android 离线 / 插件 Node grant） |
| L3 微观 API | 0 | 24 | 待 L2 主链路稳定后穿插执行 |
| L4 深度剖析 | 0 | 16 | 待 L2 暴露高复杂度主题后执行 |

## 最近完成（本轮）

| Goal | 标题 | 主入口 |
|------|------|--------|
| L2-today-project-tag-membership-flow | 任务进入 Today、Project 与 Tag 视图的归属判定全链路 | `slice-today-project-tag-membership-flow/lessons/0001-flow-map.html` |
| L2-project-completion-flow | 项目完成、任务归档与工作上下文收尾全链路 | `slice-project-completion-flow/lessons/0001-flow-map.html` |
| L2-remote-op-apply-flow | 远端操作下载、转换、应用与冲突边界全链路 | `slice-remote-op-apply-flow/lessons/0001-flow-map.html` |
| L2-planner-schedule-flow | 任务计划到日程渲染的 Planner 与 Schedule 投影全链路 | `slice-planner-schedule-flow/lessons/0001-flow-map.html` |
| L2-focus-mode-flow | Focus session、break、metric 与当前任务追踪联动全链路 | `slice-focus-mode-flow/lessons/0001-flow-map.html` |
| L2-calendar-time-block-sync-flow | 日历事件导入与插件 time block 写回全链路 | `slice-calendar-time-block-sync-flow/lessons/0001-flow-map.html` |
| L2-android-native-reminder-flow | Android 原生提醒调度、AlarmManager、Receiver 与通知 action 全链路 | `slice-android-native-reminder-flow/lessons/0001-flow-map.html` |
| L2-android-share-widget-flow | Android 分享 intent、Home Widget、native 队列与 Angular drain 全链路 | `slice-android-share-widget-flow/lessons/0001-flow-map.html` |

## 当前队列前 8 项

| Goal | 层级 | 标题 | 状态 |
|------|------|------|------|
| L2-ios-webdav-bridge-flow | L2 | iOS WebDAV Capacitor plugin 与同步 provider 全链路 | pending |
| L2-pwa-cache-update-flow | L2 | PWA service worker 缓存、更新检测与 native 注销全链路 | pending |
| L2-android-offline-startup-flow | L2 | Android 离线启动、legacy WebView 迁移与 Capacitor Activity 切换全链路 | pending |
| L2-plugin-node-execution-grant-flow | L2 | 插件 Node execution grant、native consent、IPC 与脚本执行安全边界全链路 | pending |
| L2-plugin-issue-provider-register-flow | L2 | 插件 issue provider 注册、adapter resolver 与 two-way sync 接入全链路 | pending |
| L2-plugin-upload-reload-flow | L2 | 上传插件 zip、manifest 校验、cache 持久化与 reload 全链路 | pending |
| L2-plugin-iframe-bridge-flow | L2 | iframe 插件资源加载、菜单/侧栏注册、消息桥与卸载回调全链路 | pending |
| L2-global-config-sync-flow | L2 | 全局配置 local-only 字段、同步合并、迁移与默认值落地全链路 | pending |

## 本轮说明

- **远端 op apply** 首轮审查因缺 mermaid 时序图不通过，修复后复审通过。
- **Today/Tag/Project**、**项目完成**、**Planner/Schedule** 为有条件通过：技术事实准确，但部分主题仍缺独立 mermaid 时序图或入口代码锚点，已记入 `review_issues`。
- **Focus mode** 新发现 Pomodoro break 监听 `incrementCycle`（非 `completeFocusSession`）等 L3 候选 goal。
- 全部 8 个主题均通过 `audit_topic.py` 与 `generate_snapshot.py`。
