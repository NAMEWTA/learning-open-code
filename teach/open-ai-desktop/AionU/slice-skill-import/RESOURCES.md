# 助手或 Skill 导入全链路资源

## 知识

- [L0：AionU 项目总览](../00-overview/reference/00-overview.html)
  用于确认本切片在项目全局中的位置，尤其是 renderer、common adapter 和 aioncore 后端边界。
- [L1：Assistants、Skills 与 Tools 配置模块参考](../module-assistants-skills/reference/assistants-skills-overview.html)
  用于确认 AssistantSettings、SkillsHubSettings、hooks 和 `/api/skills/*` 的模块职责。
- [L1：Common adapter 与 API 映射参考](../module-common-adapter/reference/common-adapter-overview.html)
  用于确认 `ipcBridge` 的 HTTP provider 形状，以及 `/api/assistants/*`、`/api/skills/*` 的边界。
- [L1：测试质量模块参考](../module-test-quality/reference/test-quality-overview.html)
  用于确认 Skills / Assistants 改动应优先连接哪些 E2E、helper 和 DOM 测试。
- 源码：`packages/desktop/src/renderer/pages/settings/SkillsHubSettings.tsx`
  Skills Hub 手动导入、导入结果提示、导入历史与列表刷新主入口。
- 源码：`packages/desktop/src/renderer/pages/settings/skillImportMessages.ts`
  Skill 导入错误码、部分成功、全失败和大小限制细节的统一文案转换。
- 源码：`packages/desktop/src/renderer/hooks/assistant/useAssistantEditor.ts`
  Assistant 编辑状态机、pending skill 保存前导入、assistant create/update 和 cache 刷新。
- 源码：`packages/desktop/src/common/adapter/ipcBridge.ts`
  renderer 调用到 `/api/skills/import`、`/api/skills`、`/api/assistants` 的 contract 映射。
- 测试：`tests/e2e/features/settings/skills/manual-import.e2e.ts`
  当前导入主路径的 E2E 证据：mock dialog、点击导入、验证 success message 和 custom skill。
- 测试：`tests/e2e/specs/assistant-settings-skills.e2e.ts`
  Assistant 默认 skill 选择持久化的 E2E 证据。

## 智慧（社区）

- 本主题是仓库内源码教学任务，当前不依赖外部社区资料。后续如果要验证 aioncore 后端实现，应补充 AionCore 源码或维护者讨论记录，而不是依赖前端仓库推断。

## 空白

- 未读取 aioncore 中 `/api/skills/import` 与 `/api/assistants` 的后端路由实现；本主题只覆盖 AionU 前端、common adapter contract 和 E2E 可观察状态。
- 未运行 Playwright E2E；本主题只阅读测试源码作为证据。
