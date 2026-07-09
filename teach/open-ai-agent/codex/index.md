# codex 教学索引

## 教学主题

| 主题 | 路径 | 描述 |
|------|------|------|
| 项目总览 | `./00-overview/` | Codex CLI 的定位、架构、技术栈与学习地图 |
| CLI 与 npm 包装层 | `./module-cli-packaging/` | npm 包装、Rust CLI 分发与子命令入口 |
| TUI 交互式终端界面 | `./module-tui/` | 终端交互、消息渲染、输入区与运行状态 |
| Core Thread/Turn 与模型上下文 | `./module-core-runtime/` | 会话、回合、上下文、模型流与任务调度 |
| App-server JSON-RPC 服务 | `./module-app-server/` | Thread/Turn/Item 协议、传输与请求处理 |
| 工具定义与执行抽象 | `./module-tools-execution/` | Tool schema、执行器、shell 与 patch 边界 |
| Sandbox、权限与配置系统 | `./module-sandbox-config/` | 沙箱策略、审批配置、权限 profile 与运行时决策 |
| Skills、Plugins、MCP 与 Hooks 扩展系统 | `./module-extensions-skills-mcp/` | Skills 发现、插件清单、MCP 连接与 hooks |
| Python 与 TypeScript SDK | `./module-sdk/` | SDK 客户端、线程/回合 API 与流式事件 |
| Bazel、CI 与发布链路 | `./module-build-release/` | Bazel、Cargo、pnpm、脚本与 GitHub Actions 发布路径 |
| 状态、模型提供商与后端通信 | `./module-state-model-backend/` | 状态存储、认证、模型目录、后端客户端与 cloud config |
| npm 到 Rust exec 启动链路 | `./slice-npm-to-rust-exec/` | 追踪 codex exec 从 npm bin 到 Rust 进程的完整调用链 |
| 交互 Turn 垂直切片 | `./slice-interactive-turn/` | 追踪 TUI 用户输入→模型调用→流式响应→UI 渲染完整闭环 |
| App-server thread/turn JSON-RPC 链路 | `./slice-app-server-turn/` | 追踪 thread/start→turn/start 七层调用链和时序图 |
| 工具调用执行垂直切片 | `./slice-tool-call-execution/` | 追踪模型 tool_use→审批→沙箱执行→结果回写的 7 步闭环 |
| Sandbox 权限决策链路 | `./slice-sandbox-permission-decision/` | 追踪工具调用→execpolicy→权限编译→沙箱选择→平台创建的完整决策链路 |
| Skill 发现、读取与上下文注入 | `./slice-skill-activation/` | 追踪 SKILL.md 文件发现→解析→快照→渲染→系统提示词注入全链路 |
| MCP Server 配置与连接管理 | `./slice-mcp-server-management/` | 追踪 CLI mcp add→配置写入→连接建立→工具发现的完整 6 层链路 |
| SDK Thread/Run 事件消费链路 | `./slice-sdk-thread-run/` | 追踪 SDK startThread→run→app-server/exec 子进程→流式事件→用户回调全链路 |
| Rust 多平台二进制发布链路 | `./slice-release-package-binary/` | 追踪 git tag→CI多平台构建→代码签名→npm/Homebrew/GitHub Release 完整发布链路 |
| 会话 Resume/Fork/Archive 持久化 | `./slice-session-resume-fork/` | 追踪会话创建→JSONL rollout→SQLite backfill→resume恢复→fork分支→archive归档全链路 |

| Rollout JSONL 反向扫描重建 | `./deep-dive-rollout-reconstruction/` | JSONL 倒序扫描、三条件提前终止与 SQLite backfill 状态机 |

| Skill 上下文预算模型 | `./deep-dive-skill-budget-model/` | 2% 上下文窗口预算、三级降级策略与逐字符轮转分配算法 |
