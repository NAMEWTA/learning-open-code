# 使命：codex mcp add/login/list 的配置与连接链路

## 为什么
理解 Codex 如何将一条 `codex mcp add` CLI 命令转化为一个实际可用的 MCP 远程工具。掌握这条链路后，就能定位 MCP 集成中任何环节的问题——无论是配置格式错误导致加载失败、OAuth 登录令牌过期、连接握手超时，还是工具过滤规则导致模型看不到某个工具。

## 成功的样子
- 能画出从 CLI `mcp add` → config.toml 写入 → McpConnectionManager 加载 → rmcp-client 连接 → 工具发现 → turn 中可用的完整 6 层时序图
- 能说出 stdio 和 streamable_http 两种 transport 在配置写入和连接建立时的差异
- 能解释 OAuth 登录流程中 scope 发现、token 存储、连接时的 bearer token 解析三重机制
- 能分析连接失败重试（Codex Apps reconnect）、配置格式错误（非法 server name / inline bearer_token）、启动超时三条异常路径的代码位置

## 约束条件
- 学习者已通过 L1-module-extensions-skills-mcp 了解 MCP server 的注册机制和 rmcp-client 基础
- 学习者已通过 L1-module-cli-packaging 了解 CLI 子命令分发机制
- 单节课不超过 15 分钟阅读量

## 不在范围内
- MCP 协议规范本身的细节（initialize 握手、tools/list 等协议消息格式）
- TUI 端的 MCP 审批 UI 渲染
- MCP 工具调用的沙箱执行细节（属于 tool-call-execution 切片）
- Codex Apps 内置 MCP 服务器的完整插件系统
