# AionU 测试质量模块资源

## 知识

- [`open-ai-desktop/AionU/vitest.config.ts`](../../../../open-ai-desktop/AionU/vitest.config.ts)
  Vitest 4 的 node / jsdom projects、include / exclude、setup files、coverage provider 与 thresholds。适用于判断单元、DOM、集成、回归测试如何被发现和运行。
- [`open-ai-desktop/AionU/playwright.config.ts`](../../../../open-ai-desktop/AionU/playwright.config.ts)
  Playwright Electron E2E 的 testDir、串行 worker、重试、report、trace、video 和 artifact 目录。适用于判断端到端测试运行边界。
- [`open-ai-desktop/AionU/tests/`](../../../../open-ai-desktop/AionU/tests/)
  单元、集成、E2E、fixtures 和 helpers 的实际测试资产。适用于追踪某个功能已有测试证据。
- [`open-ai-desktop/AionU/tests/e2e/README.md`](../../../../open-ai-desktop/AionU/tests/e2e/README.md)
  E2E 启动模式、构建要求、aioncore PATH 前置条件、helper 约束和排障说明。
- [`open-ai-desktop/AionU/tests/e2e/fixtures.ts`](../../../../open-ai-desktop/AionU/tests/e2e/fixtures.ts)
  Electron app singleton fixture、dev / packaged launch、失败截图和清理策略。适用于理解为什么 E2E 串行运行。
- [`open-ai-desktop/AionU/tests/e2e/helpers/bridge/`](../../../../open-ai-desktop/AionU/tests/e2e/helpers/bridge/)
  `invokeBridge`、HTTP route mapping 和 response mapper。适用于理解 E2E 如何同时验证 UI 与 backend 状态。
- [`open-ai-desktop/AionU/AGENTS.md`](../../../../open-ai-desktop/AionU/AGENTS.md)
  项目级质量要求：测试覆盖目标、硬阻断项、开发命令、PR 前检查和 no-push 规则。
- [`open-ai-desktop/AionU/.claude/skills/testing/SKILL.md`](../../../../open-ai-desktop/AionU/.claude/skills/testing/SKILL.md)
  AionU 自带 testing skill。适用于理解写测试时的风险优先、失败路径和行为导向规则。
- [`open-ai-desktop/AionU/package.json`](../../../../open-ai-desktop/AionU/package.json)
  `test`、`test:coverage`、`test:e2e`、`test:e2e:team`、integration、contract、bench 等脚本入口。
- [`open-ai-desktop/AionU/justfile`](../../../../open-ai-desktop/AionU/justfile)
  本地质量命令组合，特别是 `push` gate 与 `e2e-test` 的先构建再 Playwright。
- [`open-ai-desktop/AionU/.github/workflows/pr-checks.yml`](../../../../open-ai-desktop/AionU/.github/workflows/pr-checks.yml)
  PR code quality、跨平台 unit tests、coverage、i18n、构建烟测和 release script test。
- [`open-ai-desktop/AionU/.github/workflows/pr-e2e-artifacts.yml`](../../../../open-ai-desktop/AionU/.github/workflows/pr-e2e-artifacts.yml)
  手动 E2E artifacts workflow。适用于查看 Linux + xvfb + screenshots 的报告归档链路。
- [`open-ai-desktop/AionU/codecov.yml`](../../../../open-ai-desktop/AionU/codecov.yml)
  Codecov project / patch informational 状态和 ignore 规则。适用于区分覆盖率报告与硬闸门。
- [`open-ai-desktop/AionU/docs/contributing/file-structure.md`](../../../../open-ai-desktop/AionU/docs/contributing/file-structure.md)
  测试文件映射、目录规模和依赖注入可测性建议。
- [`teach/open-ai-desktop/AionU/00-overview/reference/00-overview.html`](../00-overview/reference/00-overview.html)
  L0 项目总览。适用于把测试质量放回 AionU 整体工程结构。
- [`teach/open-ai-desktop/AionU/module-cron/reference/cron-overview.html`](../module-cron/reference/cron-overview.html)
  Cron 模块测试证据。适用于观察单元 hook 测试与 AI 对话 E2E 如何互补。
- [`teach/open-ai-desktop/AionU/module-team-mode/reference/team-mode-overview.html`](../module-team-mode/reference/team-mode-overview.html)
  Team Mode 测试证据。适用于观察 UI-first E2E、helper 规则和 bridge 断言。
- [`teach/open-ai-desktop/AionU/module-assistants-skills/reference/assistants-skills-overview.html`](../module-assistants-skills/reference/assistants-skills-overview.html)
  Assistants / Skills 测试证据。适用于观察 Settings、Skills Hub、MCP 相关测试覆盖。

## 智慧（社区）

- 本轮未引入外部社区资源。该主题是源码课程生成，可信依据优先来自本地测试配置、测试文件、CI workflow、已有 L1 课程和项目自带规范。

## 空白

- 未读取上游 GitHub Actions 最近一次真实运行结果；本主题只根据 workflow 配置判断质量链路。
- 未读取上游 issue、discussion 或 PR 评审记录；后续若要分析测试策略演进，需要补充这些社区上下文。
- 未执行 AionU 全量测试，因此不声明当前测试套件在本机全部通过。
