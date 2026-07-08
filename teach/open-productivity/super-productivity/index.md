# super-productivity 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目整体架构总览 | `./00-overview/` | Angular/Electron/Capacitor 架构地图与学习路线 |
| Angular 应用装配与全局壳层 | `./module-angular-app-shell/` | bootstrap、路由、NgRx 注册与全局 UI 壳层 |
| 任务、项目、标签与工作上下文领域 | `./module-task-domain/` | 核心任务模型、工作上下文和 TODAY 虚拟标签 |
| Operation Log、本地持久化与同步架构 | `./module-op-log-sync/` | op-log、IndexedDB、sync providers 与 SuperSync 边界 |
| 计划排程、时间追踪与专注反馈 | `./module-planning-time/` | Planner、Schedule、time tracking、idle 与指标 |
| Issue Provider、日历集成与外部工作项 | `./module-issue-integrations/` | Jira/GitLab/OpenProject 等 provider 与双向同步 |
| Electron 桌面宿主、窗口、IPC 与系统集成 | `./module-electron-host/` | 主进程、窗口、托盘、IPC、协议与本地能力 |
| Capacitor 移动端与 PWA 宿主 | `./module-mobile-pwa-host/` | Android/iOS、service worker、移动平台桥接 |
| 插件系统、插件 API 与运行时加载 | `./module-plugin-system/` | plugin-api、运行时加载、OAuth 与 Node 执行 |
| UI 组件、配置、导入导出与本地备份 | `./module-ui-config-imex/` | UI shell、配置、i18n、导入导出与备份 |
| 测试、构建、发布与多平台工程化 | `./module-engineering-release/` | npm scripts、构建、CI、发布与平台包 |
| 应用启动与数据初始化全链路 | `./slice-app-startup-flow/` | bootstrap、StartupService、数据加载与初始化时序 |
| 新增任务与短语法解析全链路 | `./slice-task-create-flow/` | 输入入口、任务创建、归属判定与 op-log 捕获 |
| 开始追踪、空闲检测与时间记录全链路 | `./slice-time-tracking-flow/` | time tracking、idle、focus、metric 与任务耗时 |
| 本地操作捕获、持久化与同步上传下载全链路 | `./slice-op-log-sync-flow/` | action 捕获、op-log 持久化、flush 与同步 provider |
| 外部 Issue 拉取、映射与双向同步全链路 | `./slice-issue-import-sync-flow/` | provider 拉取、任务导入、baseline 与写回边界 |
| Electron 启动、窗口创建与关闭前同步全链路 | `./slice-electron-startup-close-flow/` | main process、窗口、preload IPC、APP_READY 与 before-close 保护 |
| 插件发现、初始化、OAuth 与运行时调用全链路 | `./slice-plugin-lifecycle-flow/` | manifest、StartupService、PluginBridge、OAuth、Node executor 与 issue provider |
| 移动端后台恢复、持久化刷新与同步补偿全链路 | `./slice-mobile-background-flush-flow/` | Android/iOS/PWA 生命周期、补时、flush、sync window 与 PWA cache 边界 |

| Focus 与追踪联动 | `./slice-focus-mode-flow/` | session、break、metric 与 current task 双向同步全链路 |

| 日历事件导入与 time block 写回全链路 | `./slice-calendar-time-block-sync-flow/` | iCal/插件读事件、导入任务与 scheduled task 写回日历 |

| Android 原生提醒全链路 | `./slice-android-native-reminder-flow/` | AlarmManager 调度、Receiver 触发与通知 action 回写 |

| Android 分享与 Widget 全链路 | `./slice-android-share-widget-flow/` | 分享 intent、桌面 Widget 快照与 native 队列 drain |

| iOS WebDAV 桥接与同步全链路 | `./slice-ios-webdav-bridge-flow/` | WebDavHttp 插件、URLSession no-cache 与 sync provider |

| Android 离线启动与 Activity 切换 | `./slice-android-offline-startup-flow/` | LaunchDecider 路由、legacy WebView 迁移与 Capacitor 冷启动 |

| 插件 Node execution grant 与脚本执行安全边界 | `./slice-plugin-node-execution-grant-flow/` | native consent、IPC grant、session token 与 vm/spawn 执行全链路 |

| PWA 缓存与更新全链路 | `./slice-pwa-cache-update-flow/` | ngsw 缓存、更新检测、API freshness 与 native 注销 |
