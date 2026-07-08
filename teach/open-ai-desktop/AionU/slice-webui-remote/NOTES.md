# 主题笔记：slice-webui-remote

- 交互语言、文档说明和注释统一使用简体中文。
- 本主题是 L2 垂直切片，只写入 `teach/open-ai-desktop/AionU/slice-webui-remote/`。
- 课程主入口固定为 `lessons/0001-flow-map.html`，参考文档固定为 `reference/webui-remote-flow-map.html`。
- 关键漂移：`docs/guides/webui.md` 顶部和排障段仍出现 `3000`，但当前实现默认端口为生产 `25808`、开发 `25809`、多实例开发 `25810`。
- 不把旧 standalone server 方案当作当前实现；当前链路以 Electron `--webui`、桌面设置恢复、`@aionui/web-host` 和 `aionui-web` CLI 为准。
