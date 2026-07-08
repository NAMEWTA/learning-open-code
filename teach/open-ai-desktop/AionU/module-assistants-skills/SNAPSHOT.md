# 课程快照：module-assistants-skills

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T17:54:52+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-desktop/AionU/packages/desktop/src/common/adapter/ipcBridge.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/components/settings/SettingsModal/contents/ToolsModalContent.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/assistant/useAssistantEditor.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/assistant/useAssistantList.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/mcp/` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/mcp/catalog.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/mcp/useMcpConnection.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/mcp/useMcpOAuth.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/mcp/useMcpServerCRUD.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/AssistantSettings/AssistantEditorSections.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/AssistantSettings/index.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/SkillsHubSettings.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/settings/ToolsSettings/index.tsx` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/features/settings/skills/batch-import.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/features/settings/skills/edge-cases.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/features/settings/skills/manual-import.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/features/settings/skills/refresh-empty-tabs.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/features/settings/skills/search.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/features/settings/skills/special-cases.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-conversation-defaults.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-crud.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-defaults.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-migration.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-permissions.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-prompts.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/assistant-settings-skills.e2e.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/ext-mcp.e2e.ts` | 课程分析引用 | 🟡 辅助 |

## 引用概念与协议

| 概念 / 协议 | 用途 |
|------------|------|
| `/api/assistants/*` | Assistant CRUD、导入与启停接口族 |
| `/api/skills/*` | Skills Hub、外部路径、导入历史与 assistant rule 接口族 |
| `/api/mcp/*` | MCP server、OAuth、agent configs 和连通性测试接口族 |
| `GET /api/assistants`、`POST /api/assistants`、`PUT /api/assistants/:id`、`DELETE /api/assistants/:id` | AssistantSettings 主 CRUD 示例 |
| `PATCH /api/assistants/:id/state`、`POST /api/assistants/import` | Assistant 状态与导入示例 |
| `GET /api/skills`、`POST /api/skills/import`、`POST /api/skills/materialize-for-agent` | Skills Hub 代表调用 |
| `POST /api/skills/assistant-rule/write`、`DELETE /api/skills/assistant-rule/:assistant_id` | Assistant 与 Skill 规则绑定示例 |
| `GET /api/mcp/servers`、`POST /api/mcp/servers`、`PUT /api/mcp/servers/:id`、`POST /api/mcp/servers/:id/toggle`、`DELETE /api/mcp/servers/:id` | MCP server 管理示例 |
| `POST /api/mcp/oauth/login`、`POST /api/mcp/oauth/check-status`、`POST /api/mcp/oauth/logout` | MCP OAuth 示例 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-assistants-skills-module-tour | `lessons/0001-assistants-skills-module-tour.html` | AionU 助手与技能模块 15 分钟导览 |

## 参考资料

- `reference/assistants-skills-overview.html` — AionU Assistants、Skills 与 Tools 参考总览

## 快照摘要
- 课程数：1
- 引用源文件数：27
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
