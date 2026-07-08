# 构建与发布模块资源

## 知识

- [AionU 根 `package.json`](../../../../open-ai-desktop/AionU/package.json)
  构建发布入口清单。适用于查找 `package`、`dist:*`、`build-*`、`webui:*`、`postinstall` 等命令的真实指向。
- [Electron Builder 配置](../../../../open-ai-desktop/AionU/packages/desktop/electron-builder.yml)
  桌面分发配置。适用于核对文件白名单、`extraResources`、`asarUnpack`、平台 target、签名钩子和 GitHub publish 元数据。
- [构建协调脚本 `build-with-builder.js`](../../../../open-ai-desktop/AionU/scripts/build-with-builder.js)
  桌面打包主控脚本。适用于理解增量构建、MCP bundle、aioncore 准备、Hub 资源、NSIS patch、DMG retry 和 `electron-builder` 调用。
- [共享 aioncore 准备脚本](../../../../open-ai-desktop/AionU/packages/shared-scripts/src/prepare-aioncore.js)
  runtime 资源获取与 manifest 写入逻辑。适用于理解 Actions artifact、release asset、本地 bundle、本地 binary 四种来源。
- [共享 bundle 校验脚本](../../../../open-ai-desktop/AionU/packages/shared-scripts/src/verify-bundled-aioncore-resources.js)
  aioncore、managed node、ACP 工具入口的结构校验。适用于判断 afterPack 为什么会失败。
- [WebCLI 打包脚本](../../../../open-ai-desktop/AionU/scripts/pack-web-cli.js)
  独立 WebUI CLI tarball 生成逻辑。适用于理解 Bun 编译、静态文件复制、bundle 复制和 SHA256 产物。
- [发布资产整理脚本](../../../../open-ai-desktop/AionU/scripts/prepare-release-assets.sh)
  多平台构建产物汇总与硬校验。适用于核对 updater metadata、桌面包、WebCLI tarball 和 `install-web.sh` 是否齐全。
- [构建脚本单元测试](../../../../open-ai-desktop/AionU/tests/unit/build-scripts/)
  Windows 快速构建和版本覆盖的行为佐证。适用于验证脚本入口不只是文档约定。
- [资源校验单元测试](../../../../open-ai-desktop/AionU/tests/unit/assets/)
  aioncore bundle 与 managed ACP 资源断言。适用于定位打包后资源缺失。

## 智慧（社区）

- [Electron Builder 文档](https://www.electron.build/)
  用于核对 `electron-builder.yml` 中 target、files、extraResources、asarUnpack、afterPack、afterSign 的语义。
- [Electron Vite 文档](https://electron-vite.org/)
  用于理解 AionU 为什么先输出 `out/main`、`out/preload`、`out/renderer`，再交给 electron-builder。
- [Homebrew Cask 文档](https://docs.brew.sh/Cask-Cookbook)
  用于评估 `homebrew/aionui.rb.example` 与真实 cask 更新流程的边界。

## 空白

- 当前未读取远端 `.github/workflows/`，因此本主题不声称 CI 触发条件和发布 job 拓扑。
- `Dockerfile` 引用了当前 `package.json` 中不存在的 `build:renderer:web` 和源码中未检出的 `scripts/build-server.mjs`，需要后续单独确认是否为遗留路径。
