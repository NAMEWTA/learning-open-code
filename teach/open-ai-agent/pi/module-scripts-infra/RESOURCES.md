# 构建脚本与基础设施 资源

## 知识

- [package.json scripts 段](https://github.com/earendil-works/pi/blob/main/package.json)
  所有 npm scripts 的唯一定义处（check、release、version、publish 等）。适用于：快速定位脚本入口和调用关系。

- [源码：scripts/check-pinned-deps.mjs](https://github.com/earendil-works/pi/blob/main/scripts/check-pinned-deps.mjs)
  扫描所有 package.json 确保外部依赖使用精确版本。适用于：理解 monorepo 的版本锁定策略。

- [源码：scripts/check-ts-relative-imports.mjs](https://github.com/earendil-works/pi/blob/main/scripts/check-ts-relative-imports.mjs)
  使用 TypeScript AST 检查 .ts 文件中不允许出现相对 .js 导入。适用于：理解 ESM 导入规范。

- [源码：scripts/release.mjs](https://github.com/earendil-works/pi/blob/main/scripts/release.mjs)
  完整发布编排脚本（9 步）。适用于：理解 lockstep 版本发布流程。

- [源码：scripts/local-release.mjs](https://github.com/earendil-works/pi/blob/main/scripts/local-release.mjs)
  本地发布测试脚本，构建 tarball 并安装到隔离目录验证。适用于：理解发布前的本地验证流程。

- [源码：scripts/publish.mjs](https://github.com/earendil-works/pi/blob/main/scripts/publish.mjs)
  npm 发布脚本，含幂等检查、版本校验、build output 验证。适用于：理解安全发布的最佳实践。

- [源码：scripts/sync-versions.js](https://github.com/earendil-works/pi/blob/main/scripts/sync-versions.js)
  同步所有 workspace 包间依赖版本，确保 lockstep 一致性。适用于：理解 monorepo 内部版本管理。

- [源码：scripts/generate-coding-agent-shrinkwrap.mjs](https://github.com/earendil-works/pi/blob/main/scripts/generate-coding-agent-shrinkwrap.mjs)
  从 root lockfile 生成 coding-agent 的 npm-shrinkwrap.json。适用于：理解发布包依赖锁定机制。

- [源码：scripts/generate-coding-agent-install-lock.mjs](https://github.com/earendil-works/pi/blob/main/scripts/generate-coding-agent-install-lock.mjs)
  生成安装器使用的 lockfile，供 Pi 安装器/更新器在用户机器上复现依赖树。适用于：理解安装器设计。

- [源码：scripts/build-binaries.sh](https://github.com/earendil-works/pi/blob/main/scripts/build-binaries.sh)
  跨平台二进制构建脚本，使用 Bun compile 生成 6 平台可执行文件。适用于：理解二进制发布流程。

- [源码：scripts/check-lockfile-commit.mjs](https://github.com/earendil-works/pi/blob/main/scripts/check-lockfile-commit.mjs)
  pre-commit 中的 lockfile 变更审查，防止意外提交依赖变更。适用于：理解依赖审计机制。

- [源码：.husky/pre-commit](https://github.com/earendil-works/pi/blob/main/.husky/pre-commit)
  Git pre-commit hook：lockfile 审查 → npm run check → 条件性 browser smoke。适用于：理解本地质量门禁。

- [源码：.github/workflows/ci.yml](https://github.com/earendil-works/pi/blob/main/.github/workflows/ci.yml)
  CI 流水线：checkout → build → check → test。适用于：理解 CI 最小验证流程。

- [源码：.github/workflows/build-binaries.yml](https://github.com/earendil-works/pi/blob/main/.github/workflows/build-binaries.yml)
  多 job 发布流水线：构建二进制 → 草稿 Release → npm 发布 → 正式发布。适用于：理解完整发布 pipeline。

- [npm workspaces 文档](https://docs.npmjs.com/cli/v10/using-npm/workspaces)
  npm workspaces 官方文档。适用于：理解 monorepo 的 workspaces 工作机制。

## 智慧（社区）

- [Pi GitHub Issues](https://github.com/earendil-works/pi/issues)
  问题跟踪，包含构建脚本和 CI 相关讨论。

- [Pi Discord](https://discord.gg/pi)
  官方社区，可与维护者讨论构建与发布实践。

## 空白

- 缺少 CI/CD 工作流的独立架构文档（目前 YAML 即文档）。
- 缺少脚本间的调用关系图和依赖分析。
- 缺少 build-binaries.sh 中 Bun cross-compile 的详细原理文档。
