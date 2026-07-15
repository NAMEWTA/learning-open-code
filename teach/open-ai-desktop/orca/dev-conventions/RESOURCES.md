# 资源：Orca 开发规范

## 项目规范文件（核心来源）

| 资源 | 路径 | 说明 |
|------|------|------|
| AI Agent 编码规范 | `AGENTS.md` | 文件命名、代码注释、跨平台、工作区安全等 AI 协作约定 |
| Linter 配置 | `.oxlintrc.json` | oxlint 规则集：TypeScript、React、unicorn 插件 |
| Formatter 配置 | `.oxfmtrc.json` | oxfmt 格式：单引号、无分号、100 字符宽、无尾逗号 |
| TypeScript 配置 | `tsconfig.json` + `config/tsconfig.*.json` | 项目引用、路径别名、模块解析 |
| 设计系统 | `docs/STYLEGUIDE.md` | 颜色、字体、图标、组件、滚动条等视觉规范 |
| 贡献指南 | `.github/CONTRIBUTING.md` | 分支命名、PR 模板、开发环境搭建 |
| PR 模板 | `.github/pull_request_template.md` | PR 提交清单 |
| CI 工作流 | `.github/workflows/pr.yml` | PR 门禁：lint → typecheck → test → build |
| 组件配置 | `components.json` | shadcn/ui 配置 |

## 辅助资源

| 资源 | 路径 | 说明 |
|------|------|------|
| pre-commit hook | `.husky/pre-commit` | lint-staged：oxlint + oxfmt 在提交前自动运行 |
| React lint 专项 | `config/oxlint-react-doctor.json` | React 反模式检测 |
| Switch 穷举检查 | `config/oxlint-switch-exhaustiveness.json` | 类型感知的 switch 穷举 |
| 构建配置 | `electron.vite.config.ts` | 入口点、外部依赖、编译时常量 |
| 单元测试配置 | `config/vitest.config.ts` | vitest 运行环境与匹配模式 |
| E2E 测试配置 | `tests/playwright.config.ts` | Playwright E2E 测试配置 |

## 外部社区

Orca 暂无独立的外部开发者社区（项目仍处于快速迭代期）。规范讨论主要通过 GitHub Issues 和 PR Review 进行。
