# 教学笔记：远端操作下载、转换、应用与冲突边界全链路

- 责任目录限定为 `teach/open-productivity/super-productivity/slice-remote-op-apply-flow/`。
- 本主题只讲下载后的处理链路；本地捕获、上传、provider 总览链接到 `../slice-op-log-sync-flow/` 和 `../module-op-log-sync/`。
- 内容边界必须保持四条路径分开：普通 remote ops、incoming `SYNC_IMPORT` / `BACKUP_IMPORT` gate、force full-state download、`REPAIR` 校验修复路径。
- 新 L3/L4 候选：
  - L3：`remote-apply-crash-safety`，逐步拆解 `applyRemoteOperations()` 的 pending、applied、failed 状态机。
  - L3：`sync-import-clean-slate-filter`，专讲 full-state import 与 vector clock 过滤。
  - L3：`lww-conflict-resolution-path`，专讲 LWW 分区、本地胜出 update op 与远端胜出 apply。
  - L4：`lww-update-meta-reducer-task-relations`，深入 task/project/tag 关系在 LWW Update 中如何修复。
