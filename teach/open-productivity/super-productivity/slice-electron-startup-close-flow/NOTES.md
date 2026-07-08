# 教学笔记：Electron 启动、窗口创建与关闭前同步全链路

- 交互和教学文档使用简体中文；源码标识符保留英文。
- 本轮只写入 `slice-electron-startup-close-flow/` 主题目录，不修改项目级进度、索引或其他主题目录。
- lesson 聚焦 15 分钟内完成的链路判断能力；reference 承载长表格、排障清单和后续 L3/L4 线索。
- 必须强调 Electron main process 和 Angular renderer 的责任边界：`APP_READY` 是 renderer 向 main 回报就绪，不是 Electron 启动同步调用栈的一步。
