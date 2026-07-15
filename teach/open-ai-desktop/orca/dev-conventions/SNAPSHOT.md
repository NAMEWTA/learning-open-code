# 课程快照：Orca 开发规范、目录规范与命名规范

## 源项目信息
- **仓库路径**：`open-ai-desktop/orca`
- **Git Commit**：`61bd98db6faacb8baffa0de369b187c0e40d662a`
- **短 Commit**：`61bd98d`
- **分支**：`main`
- **快照时间**：2026-07-09T18:00:00+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `AGENTS.md` | AI Agent 编码规范主文档（文件命名、注释、跨平台、禁用词） | 🔴 核心 |
| `.oxlintrc.json` | oxlint 规则全集（TS/React/unicorn 插件） | 🔴 核心 |
| `.oxfmtrc.json` | oxfmt 格式化规则（引号、分号、行宽、尾逗号） | 🔴 核心 |
| `tsconfig.json` | 根 TypeScript 配置与项目引用 | 🟡 辅助 |
| `config/tsconfig.node.json` | 主进程 TypeScript 配置 | 🟡 辅助 |
| `config/tsconfig.web.json` | 渲染进程 TypeScript 配置 | 🟡 辅助 |
| `config/tsconfig.cli.json` | CLI TypeScript 配置 | 🟡 辅助 |
| `config/oxlint-react-doctor.json` | React 反模式专项规则 | 🟡 辅助 |
| `config/oxlint-switch-exhaustiveness.json` | Switch 穷举检查配置 | 🟡 辅助 |
| `.husky/pre-commit` | pre-commit hook（lint-staged） | 🟡 辅助 |
| `package.json` | scripts、lint-staged 配置、依赖声明 | 🟡 辅助 |
| `electron.vite.config.ts` | 构建入口点与外部依赖定义 | 🟡 辅助 |
| `docs/STYLEGUIDE.md` | 设计系统规范 | 🟡 辅助 |
| `.github/CONTRIBUTING.md` | 贡献指南与分支命名 | 🟡 辅助 |
| `.github/pull_request_template.md` | PR 提交检查清单 | 🟡 辅助 |
| `.github/workflows/pr.yml` | PR CI 门禁流程 | 🟡 辅助 |
| `config/vitest.config.ts` | 单元测试配置 | 🟡 辅助 |
| `src/renderer/src/assets/main.css` | 设计 token（规范唯一来源） | 🟡 辅助 |
| `src/main/ipc/pty.ts` | IPC handler 扁平组织范式示例 | 🟢 参考 |
| `src/renderer/src/store/index.ts` | Zustand store 组合模式示例 | 🟢 参考 |
| `src/main/runtime/rpc/methods/index.ts` | 聚合注册型 barrel 文件示例 | 🟢 参考 |
| `src/shared/network/` | shared 下唯一的嵌套子目录 | 🟢 参考 |
| `src/main/agent-hooks/` | 典型领域目录结构示例（21 文件） | 🟢 参考 |
| `src/main/dock/` | 极简领域目录示例（2 文件） | 🟢 参考 |
| `src/renderer/src/components/UpdateCard.tsx` | React 组件 Why 注释 & 子组件共置范式示例 | 🟢 参考 |
| `src/main/win32-utils.ts` | 跨平台领域文件分离 + Why 注释示例 | 🟢 参考 |
| `src/shared/errors/` (不存在) | 错误处理"去中心化"范式（反例验证） | 🟢 参考 |
| `.github/pull_request_template.md` | PR checklist + AI review + security audit 要求 | 🟡 辅助 |
| `src/renderer/src/store/types.ts` | AppState 交叉类型组合模式 | 🟢 参考 |
| `config/vitest.config.ts` | 测试超时、别名、worker 配置 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01 | `lessons/0001-dev-conventions.html` | Orca 三层规范体系：工具链、目录分层、命名约定 |
| 02 | `lessons/0002-directory-conventions.html` | 目录结构五条铁律：扁平领域、测试同居、barrel 四场景、组件两分层、shared 文件池 |
| 03 | `lessons/0003-code-quality-conventions.html` | 代码质量三支柱：Why 注释、Error 类模板、跨平台三策略 |

## 已生成参考

| 文件 | 描述 |
|------|------|
| `reference/dev-conventions-reference.html` | 完整规则速查手册：50+ lint 规则、目录职责表、命名对照表、CI 门禁清单 + 代码质量/React/状态/测试/PR 规范 |
| `reference/directory-map.html` | 目录结构速查手册：src/ 七分区、72 主进程领域目录、IPC handler 清单、Zustand slice 清单 |

## 快照摘要
- 课程数：3
- 参考文档数：2
- 引用源文件数：31
- 学习记录数：0
