# 课程快照：module-build-release

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T17:54:54+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-desktop/AionU/Dockerfile` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/homebrew/aionui.rb.example` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/package.json` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/electron-builder.yml` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/electron.vite.config.ts` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/shared-scripts/src/prepare-aioncore.js` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/shared-scripts/src/verify-bundled-aioncore-resources.js` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/scripts/afterSign.js` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/build-with-builder.js` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/scripts/install-web.sh` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/pack-web-cli.js` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/prepare-release-assets.sh` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/verify-release-assets.sh` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/prepareHubResources.js` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/rebuildNativeModules.js` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/resolveAioncoreVersion.js` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/smoke-test-install-web.sh` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/scripts/afterPack.js` | 课程分析引用 | 🔴 核心 |
| `open-ai-desktop/AionU/tests/unit/assets/prepareAioncoreActionsArtifact.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/assets/verifyBundledAioncoreResources.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/build-scripts/windows-fast-build-script.test.ts` | 课程分析引用 | 🟡 辅助 |

## 引用概念与产物

| 概念 / 产物 | 用途 |
|------------|------|
| `node scripts/pack-web-cli.js` | Web CLI 打包命令示例 |
| `latest*.yml` | electron-builder 生成的更新元数据产物模式 |
| `release-assets/` | 发布资源产物目录 |
| `resources/hub/manifest.json` | Hub 资源 manifest 逻辑路径，课程正文用于说明资源校验对象 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-build-release-module-tour | `lessons/0001-build-release-module-tour.html` | AionU 构建与发布模块导览 |

## 参考资料

- `reference/build-release-overview.html` — AionU 构建与发布模块参考

## 快照摘要
- 课程数：1
- 引用源文件数：21
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
