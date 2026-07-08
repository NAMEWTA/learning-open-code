# 工作笔记

- 批量生成模式；用户指定 goal_id `L2-ios-webdav-bridge-flow`。
- `ios-interface.ts` 在本切片中作为「恢复前台 → flush → 可能触发同步」的邻接入口引用，非 WebDAV HTTP 直连层。
- #7144 是理解 iOS no-cache 三层防线的关键 issue 编号，课程与参考中均已标注。
