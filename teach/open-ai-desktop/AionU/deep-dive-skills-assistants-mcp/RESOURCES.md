# Skills / Assistants / MCP 映射设计资源

## 知识

- `packages/desktop/src/common/types/agent/assistantTypes.ts`
  Assistant 领域类型，定义 `AssistantDetail`、`AssistantDefaults`、`AssistantCapabilities`、`AssistantPreferences`，是区分定义、默认值和偏好的核心来源。
- `packages/desktop/src/common/config/storage.ts`
  会话 extra、MCP transport、`IMcpServer`、`ISessionMcpServer` 和 MCP status 的类型来源。适用于判断会话快照和工具配置边界。
- `packages/desktop/src/renderer/hooks/assistant/useAssistantEditor.ts`
  Assistant 编辑器状态与保存路径：加载详情、Skills、MCP catalog，导入 pending skills，写回 defaults。
- `packages/desktop/src/renderer/pages/settings/AssistantSettings/editor/DefaultsSection.tsx`
  默认模型、权限、Skills、MCP 的 auto/fixed UI 控制。适用于解释为何用户看到的是一个合并选择器。
- `packages/desktop/src/renderer/hooks/mcp/catalog.ts`
  后端用户 MCP 与本地 builtin MCP 的 catalog 合并、去重和 transport 归一化规则。
- `packages/desktop/src/renderer/pages/settings/ToolsSettings/McpManagement.tsx`
  Tools/MCP 设置页入口，串联 MCP catalog、CRUD、连接测试、OAuth 状态和 extension MCP 只读展示。
- `packages/desktop/src/common/adapter/ipcBridge.ts`
  前端到后端 API 面：`/api/assistants/*`、`/api/skills/*`、`/api/mcp/*`、`/api/extensions/*` 和会话创建请求类型。
- `packages/desktop/src/renderer/pages/guid/utils/assistantDefaults.ts`
  将 Assistant default 的 auto/fixed 模式解析为 Guid 页初始默认能力。
- `packages/desktop/src/renderer/pages/guid/hooks/useGuidSend.ts`
  创建会话时把 Assistant override、Skill ids、MCP ids、session MCP servers 发送给后端。
- `examples/hello-world-extension/aion-extension.json`
  扩展示例，展示一个 extension 可以同时贡献 assistants、agents、skills、mcpServers。
- `examples/e2e-full-extension/aion-extension.json`
  E2E 用扩展示例，包含 extension assistant、skills、MCP servers 和 agent，适合作为测试夹具理解。
- `tests/e2e/specs/ext-skills.e2e.ts`
  指定测试证据之一；当前主要证明扩展 Skills 相关页面可加载，没有深断言。
- `tests/e2e/specs/ext-mcp.e2e.ts`
  指定测试证据之一；当前主要证明 Tools/MCP 页可加载并出现开关。
- `tests/e2e/specs/assistant-settings-conversation-defaults.e2e.ts`
  强证据测试：通过 HTTP 与 SQLite 验证 fixed/auto 默认能力写入 conversation snapshot 与 preferences。

## 智慧（社区）

- 本地维护路径：AionU Assistants、Skills Hub、MCP Tools 和 E2E 维护者代码评审。
  适用于复核“默认能力应放在哪里持久化”和“测试应断 UI 还是断数据库快照”这类设计判断。

## 空白

- `docs/prds/assistants/README.md` 当前文件大小为 0 字节，本主题没有可引用的 Assistants PRD 正文。
- 本轮未引入外部社区或网页资料；课程结论全部来自指定源码、examples 和测试文件。
