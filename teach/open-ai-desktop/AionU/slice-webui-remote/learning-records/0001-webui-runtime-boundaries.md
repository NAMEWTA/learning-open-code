# WebUI 运行时边界已确认

本主题确认 WebUI 有三条当前实现路径：Electron `--webui` 无窗口路径复用已启动 backend，普通桌面模式在窗口创建后按后端设置异步恢复 WebUI，独立 `aionui-web` CLI 则自己定位 static/backend/data 目录并启动 backend。后续学习可以直接从这些边界下钻，不再把旧 standalone server 文档当成权威实现。
