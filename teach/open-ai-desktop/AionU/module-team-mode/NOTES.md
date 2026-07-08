# 教学笔记：Team Mode 模块总览

- 本轮只写 `teach/open-ai-desktop/AionU/module-team-mode/`，不更新项目级 `_progress.*`、`index.md`，不修改 `open-ai-desktop/AionU/` 源码。
- L1 lesson 采用一条主线：从 `/team/:id` 打开团队页，到 `TeamChatView` 把 Team 发送覆盖注入 ACP / aionrs Chat。
- 完整接口清单、事件清单、内部分层、测试矩阵放在 `reference/team-mode-overview.html`，避免 lesson 变成源码百科。
- `docs/prds/teams/README.md` 为空，Team Mode 设计依据主要来自源码和测试。
- 发现测试一致性风险：当前 `TeamCreateModal.tsx` 使用 `data-testid="team-create-agent-option-*"`；`tests/e2e/cases/teams/team-workspace-migration.e2e.ts` 仍查找 `team-create-agent-card-*` 和 `team-create-agent-selected-badge-*`。本轮只记录，不修源项目。
