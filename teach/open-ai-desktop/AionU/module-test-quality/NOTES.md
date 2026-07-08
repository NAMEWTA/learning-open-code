# 教学笔记：AionU 测试质量模块

- 本主题是 AionU teach-goal 第 5 轮 worker 的 L1 模块总览，只写 `module-test-quality/` 目录。
- lesson 只讲一条 15 分钟主线：先判断证据层，再选择测试命令；完整接口、矩阵和 CI 清单放 reference。
- 关键发现：`AGENTS.md` 和 testing skill 写明覆盖目标为 80%，但当前 `vitest.config.ts` thresholds 是 0，`codecov.yml` project/patch 状态为 informational，`pr-checks.yml` 中 coverage job 对命令失败也是 warning-only。
- E2E 关键约束：`playwright.config.ts` 强制 `workers: 1`，因为 Electron 测试共享 singleton app；`tests/e2e/README.md` 说明 E2E 依赖 `out/` 构建产物和 PATH 上的 `aioncore`。
- 业务证据交叉引用：Cron 有 `tests/unit/cron/` 与 `tests/e2e/specs/cron-crud.e2e.ts`；Team Mode 有 `tests/e2e/cases/teams/` 和 `tests/unit/renderer/team/`；Skills Hub 当前源码包含 10 个 `tests/e2e/features/settings/skills/*.e2e.ts`，比既有 `module-assistants-skills` reference 中列出的范围更多。
