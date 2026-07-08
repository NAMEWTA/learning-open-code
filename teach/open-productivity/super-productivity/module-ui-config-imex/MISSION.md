# 使命：UI 组件、配置、导入导出与本地备份

## 为什么
读者需要在 super-productivity 中快速判断一个问题应该从共享 UI、Angular 壳层、全局配置、导入导出、op-log 备份恢复，还是 Electron 本地能力入口开始读。目标不是背目录，而是在排查设置页、主题/i18n、文件导入、同步恢复和本地备份问题时少走错层。

## 成功的样子
- 能把设置页表单、配置持久化、副作用应用和 Electron 设置通知分到正确文件。
- 能说明文件导入、SuperSync 恢复和本地自动备份为什么最终要经过 op-log backup/import 入口。
- 能区分 `src/app/ui/`、`src/app/core-ui/`、`src/styles/`、`src/assets/i18n/` 的职责边界。

## 约束条件
- 本主题是 L1 短课，只建立入口地图和边界判断，不展开每个表单字段或完整同步算法。
- 必须和 L0、Angular L1、op-log L1、Electron L1 对齐，避免重复讲应用启动、同步协议和主进程安全细节。

## 不在范围内
- 不讲具体业务 feature 的设置语义，例如任务、番茄钟、计划页的字段含义。
- 不讲 SuperSync 服务端协议细节、vector clock 冲突算法或 Electron IPC 安全全景。
