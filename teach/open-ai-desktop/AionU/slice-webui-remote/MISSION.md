# 使命：WebUI 启动与远程访问全链路

## 为什么
本主题面向需要维护 AionU WebUI 启动、远程访问和独立部署路径的读者。学习完成后，读者应能从用户启动命令一路追到 Electron main、配置解析、WebHost 静态服务、WebCLI 密码自举和 E2E 证据，并能识别文档与实现不一致的地方。

## 成功的样子
- 能指出 `--webui`、`--remote`、端口配置、环境变量和 `webui.config.json` 分别在哪里被解析。
- 能说明 Electron WebUI 与 `aionui-web` CLI 在 backend 生命周期上的差异。
- 能定位远程访问只在显式允许时绑定 `0.0.0.0`，并解释首启密码和 resetpass 边界。
- 能用 docs 和 E2E 判断当前实现是否漂移，而不是照旧 standalone server 文档推断。

## 约束条件
- 源项目 `open-ai-desktop/AionU/` 只读。
- 本主题只写入 `teach/open-ai-desktop/AionU/slice-webui-remote/`。
- 短课保持 15 分钟内可完成，长表格和完整链路放入参考文档。

## 不在范围内
- 不讲 renderer 设置页的完整 UI 组件实现。
- 不展开 aioncore 认证后端内部实现。
- 不修正文档或源码，只记录当前版本的实现事实和漂移。
