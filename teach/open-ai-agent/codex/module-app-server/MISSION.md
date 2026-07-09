# 使命：App-server JSON-RPC 服务

## 为什么
用户希望从 0 到 1 精通 Codex CLI 的架构与实现细节，尤其是 app-server 如何把 Rust core 能力暴露给 IDE、桌面应用和 SDK 等富客户端。掌握这一层后，用户应能判断一个新功能应该落在协议、请求处理器、transport 还是 core runtime，而不是把所有复杂度混在一起。

## 成功的样子
- 能画出 `codex app-server` 从启动、握手、请求分发到事件回写的主链路。
- 能按方法前缀识别 Thread、Turn、FS、Config、MCP、Plugin、Account 等 API 所属处理器。
- 能解释 app-server 与 `codex-core`、`codex-app-server-protocol`、`codex-app-server-transport` 的依赖边界。
- 能为后续 L2 垂直切片定位最小源码入口。

## 约束条件
- 本主题是 L1 模块导览，不展开完整 API 百科；长表格进入 `reference/`。
- 每节 lesson 保持 15 分钟内完成，单课只训练一个判断能力。
- 只写入 `teach/open-ai-agent/codex/module-app-server/`，不修改源项目与全局进度文件。

## 不在范围内
- 不讲 TUI 渲染、CLI packaging、core runtime 内部执行循环的完整细节。
- 不逐一解释所有 JSON Schema 字段。
- 不替代后续 L2 的 `app-server turn` 垂直链路和 L3 API 参考。
