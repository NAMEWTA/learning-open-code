# 使命：测试、构建、发布与多平台工程化

## 为什么
用户需要把 super-productivity 的工程化链路读成一张可追踪地图：从 `package.json` 的 npm scripts 出发，判断一次改动应该触发 Angular、Electron、Capacitor、插件包、E2E、CI 或发布元数据中的哪一段，而不是把 CI/CD 当成黑盒。

## 成功的样子
- 能把一个命令归类为开发、测试、构建、打包或发布元数据维护。
- 能从 `npm run dist`、`npm run dist:android:prod`、`npm run plugins:build` 追到真实产物目录和关键配置。
- 能判断 `.github/workflows/` 中哪些 workflow 是 PR 守门，哪些是 release/tag 发布。
- 能说清 `build/`、`fastlane/`、`snap/`、`tools/`、`scripts/`、`eslint-local-rules/` 各自的边界。

## 约束条件
- 本主题是 L1 模块总览，lesson 控制在 15 分钟内完成，长清单放入 reference。
- 只基于当前仓库源码、脚本和 workflow，不泛泛讲 CI/CD。
- 本轮只写入 `teach/open-productivity/super-productivity/module-engineering-release/`，不修改源项目、索引或进度台账。

## 不在范围内
- 不深入讲 Electron IPC 安全细节；详见相邻 Electron L1。
- 不展开移动端原生代码实现；Mobile/PWA L1 是相邻主题。
- 不展开插件运行时 API 细节；Plugin L1 是相邻主题。
- 不覆盖具体同步算法、业务 feature 或 UI 交互细节。
