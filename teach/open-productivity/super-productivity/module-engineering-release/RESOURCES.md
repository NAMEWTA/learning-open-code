# 测试、构建、发布与多平台工程化资源

## 知识

- [项目脚本入口：`package.json`](../../../../open-productivity/super-productivity/package.json)
  npm scripts、workspace、Electron main、依赖和发布 provider 的单一入口。适用于追踪开发、测试、构建、打包和 release 命令。
- [Angular 构建配置：`angular.json`](../../../../open-productivity/super-productivity/angular.json)
  定义 `sp2` 应用、输出目录、assets、service worker、Karma 和 lint target。适用于判断 Web/PWA 与 Electron renderer 的前端产物边界。
- [Electron Builder 配置：`electron-builder.yaml`](../../../../open-productivity/super-productivity/electron-builder.yaml)
  定义 `.tmp/app-builds`、asar 文件白名单/排除、Windows/Linux/macOS/Snap 目标、Flatpak 配置段和 `afterPack`；当前 Linux targets 不包含 Flatpak。适用于桌面发布产物阅读。
- [Capacitor 配置：`capacitor.config.ts`](../../../../open-productivity/super-productivity/capacitor.config.ts)
  定义 `webDir: dist/browser`、Android 插件白名单和 iOS WebView 行为。适用于移动端构建链路。
- [包与内置插件构建：`packages/build-packages.js`](../../../../open-productivity/super-productivity/packages/build-packages.js)
  串行构建 `sync-core`、`sync-providers`、`shared-schema`、`plugin-api`、`vite-plugin` 和 `plugin-dev` 插件，并复制 bundled plugins 到 `src/assets`。
- [Playwright E2E 配置：`e2e/playwright.config.ts`](../../../../open-productivity/super-productivity/e2e/playwright.config.ts)
  定义 E2E 目录、global setup、workers、reporter、baseURL、webServer 和 artifacts。适用于测试链路判断。
- [GitHub Actions 工作流目录：`.github/workflows/`](../../../../open-productivity/super-productivity/.github/workflows)
  PR 守门、Electron smoke、插件测试、桌面 release、Web 发布、Android/iOS 商店发布、Snap/AUR/Store 辅助发布都在这里分流。
- [发布元数据与商店脚本：`fastlane/`](../../../../open-productivity/super-productivity/fastlane)
  App Store Connect 上传 lane、Android metadata 和 release notes 目录。适用于区分“构建产物”和“商店元信息”。

## 智慧（社区）

- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues)
  适用于验证打包、平台兼容、Snap/Wayland、App Store、Play Store 等真实用户反馈。
- [Super Productivity GitHub Actions](https://github.com/super-productivity/super-productivity/actions)
  适用于观察 workflow 的实际失败形态、artifact 产物和 release 节奏。

## 空白

- 本课未查外部商店后台配置，因为 Google Play、App Store Connect、Microsoft Partner Center 和 Snap Store 的项目私有配置不在仓库中。
- `module-mobile-pwa-host` 与 `module-plugin-system` 已生成 lesson/reference；本主题正文已补相邻 L1 的交叉链接。
