# UI 组件、配置、导入导出与本地备份资源

## 知识

- [源码：配置页入口](../../../../open-productivity/super-productivity/src/app/pages/config-page/config-page.component.ts)
  设置页 tab、Formly section、同步按钮、自动备份 section 注入和 `saveGlobalCfg()` 的主入口。
- [源码：全局配置模型与 store](../../../../open-productivity/super-productivity/src/app/features/config/global-config.model.ts)
  配置 section 类型、sync/localBackup/localization/misc 等边界；配合 `store/global-config.actions.ts`、`store/global-config.reducer.ts`、`store/global-config.effects.ts` 阅读。
- [源码：Formly 与配置表单注册](../../../../open-productivity/super-productivity/src/app/ui/formly-config.module.ts)
  根级 Formly 类型注册；用于判断表单控件问题属于共享 UI 还是配置 schema。
- [源码：导入导出 UI](../../../../open-productivity/super-productivity/src/app/imex/file-imex/file-imex.component.ts)
  文件导入、URL 导入、手动备份下载和隐私导出的用户入口。
- [源码：op-log 备份服务](../../../../open-productivity/super-productivity/src/app/op-log/backup/backup.service.ts)
  `loadCompleteBackup()` 与 `importCompleteBackup()` 的一致性入口；恢复导入会生成 `BACKUP_IMPORT` 并重置 sync seq。
- [源码：状态快照服务](../../../../open-productivity/super-productivity/src/app/op-log/backup/state-snapshot.service.ts)
  备份和 snapshot 上传使用的 NgRx selector 清单；archives 需要异步读取 IndexedDB。
- [源码：本地自动备份服务](../../../../open-productivity/super-productivity/src/app/imex/local-backup/local-backup.service.ts)
  Electron、Android、iOS 三类本地备份路径和恢复保护逻辑。
- [源码：Electron backup adapter](../../../../open-productivity/super-productivity/electron/backup.ts)
  桌面端备份文件夹、IPC handler、路径 guard 和旧备份清理。
- [源码：主题与 i18n](../../../../open-productivity/super-productivity/src/app/core/theme/global-theme.service.ts)
  全局 body class、Material CSS vars、图标、主题和背景图 watcher；配合 `core/language/language.service.ts`、`src/main.ts`、`src/assets/i18n/*.json` 阅读。
- [相邻课程：L0 全局地图](../00-overview/lessons/0001-project-map.html)
  用于确认本主题在 renderer、op-log、Electron 宿主之间的位置。
- [相邻课程：Angular L1](../module-angular-app-shell/lessons/0001-angular-app-shell-module-tour.html)
  用于确认 Angular bootstrap、router、root shell 与本主题的边界。
- [相邻课程：op-log L1](../module-op-log-sync/lessons/0001-op-log-sync-module-tour.html)
  用于确认配置 action、backup import、sync provider 与 operation log 的关系。
- [相邻课程：Electron L1](../module-electron-host/lessons/0001-electron-host-module-tour.html)
  用于确认 `window.ea`、IPC、本地文件能力和主进程边界。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/johannesjo/super-productivity/issues)
  适用于检验设置、备份恢复、同步和桌面端问题是否已有真实 bug 报告或维护者解释。

## 空白

- 暂未为本 L1 引入外部文章。此主题的可信依据主要是当前源码与相邻课程；后续 L2 若深入主题 CSS contract、备份数据损坏案例或 SuperSync 恢复策略，再补充专门资源。
