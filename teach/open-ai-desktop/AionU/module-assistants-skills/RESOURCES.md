# Assistants、Skills 与 Tools 配置模块资源

## 知识

- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/AssistantSettings/`
  助手管理页源码。适用于理解助手列表、编辑器、builtin/user/generated 权限差异、技能与 MCP 默认项如何进入保存请求。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/assistant/`
  助手列表与编辑状态机。适用于追踪 list/get/create/update/delete/setState、规则写入、技能导入和缓存刷新。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/SkillsHubSettings.tsx`
  Skills Hub 单页实现。适用于理解技能来源分组、搜索、导入、删除、导入历史和 URL highlight。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/ToolsSettings/`
  Tools 设置页外壳。适用于确认 Tools 已成为独立设置入口，并委托共享 ToolsModalContent 处理 MCP。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/components/settings/SettingsModal/contents/ToolsModalContent.tsx`
  MCP 管理和内置图像生成工具配置。适用于追踪 MCP server CRUD、连接测试、OAuth、图像生成模型同步。
- `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/mcp/`
  MCP server hooks。适用于理解 catalog 合并、CRUD、连接测试、OAuth 和扩展 server 的读取路径。
- `open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts`
  common adapter 总接口。适用于核对 assistants、skills、mcpService 的 HTTP endpoint 映射。
- `open-ai-desktop/AionU/packages/desktop/src/common/types/agent/assistantTypes.ts`
  assistant wire contract 镜像。适用于确认 `Assistant`、`AssistantDetail`、`CreateAssistantRequest`、`UpdateAssistantRequest` 的字段含义。
- `open-ai-desktop/AionU/tests/e2e/features/settings/skills/`
  Skills Hub E2E 测试。适用于确认技能导入、搜索、刷新、外部源、批量导入、highlight 参数等行为被测试锁定。
- `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-*.e2e.ts`
  AssistantSettings E2E 测试。适用于确认助手 CRUD、prompts、defaults、permissions、skills/MCP 默认项、迁移和会话默认值。
- `open-ai-desktop/AionU/tests/e2e/specs/ext-mcp.e2e.ts`
  Tools MCP 的端到端证据。适用于确认扩展 MCP 基本链路，同时识别 CRUD、OAuth、图像生成 toggle 的后续测试缺口。
- `teach/open-ai-desktop/AionU/00-overview/reference/00-overview.html`
  L0 项目地图。适用于回看 renderer、common adapter、backend 运行时在全局架构中的位置。
- `teach/open-ai-desktop/AionU/module-common-adapter/reference/common-adapter-overview.html`
  common adapter L1 参考。适用于对照本模块中的 HTTP/WS/IPC 边界。
- `teach/open-ai-desktop/AionU/module-renderer-core/reference/renderer-core-overview.html`
  renderer core L1 参考。适用于对照三条设置路由如何挂到 UI shell。

## 智慧（社区）

- [AionU GitHub Issues](https://github.com/iOfficeAI/AionUi/issues)
  适用于把课程中的源码判断拿到真实缺陷、功能请求和回归报告中验证。
- 本仓库后续 teach-goal review 轮次
  适用于由并行 worker 或审查 worker 复核本 L1 的模块边界、遗漏接口和测试证据。

## 空白

- `open-ai-desktop/AionU/docs/prds/assistants/README.md` 当前为空，不能提供 assistant 产品规则或历史决策依据。
- Tools MCP 目前缺少与 Skills Hub 同等粒度的设置页 E2E 套件，CRUD、OAuth、图像生成 toggle 仍可补强。
