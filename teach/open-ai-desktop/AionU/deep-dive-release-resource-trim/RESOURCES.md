# electron-builder 资源裁剪与发布资源校验资源

## 知识

- `open-ai-desktop/AionU/packages/desktop/electron-builder.yml`
  AionU 桌面发布包的资源包含、排除、extraResources、asarUnpack、平台目标和 afterPack/afterSign 配置。适用于判断“哪些文件进入 app.asar，哪些文件放在 Resources 外层”。
- `open-ai-desktop/AionU/packages/shared-scripts/src/prepare-aioncore.js`
  bundled-aioncore 准备入口。适用于理解完整本地 bundle、Actions artifact、release asset、本地 binary 的来源优先级，以及 managed-resources 生成和 manifest 写入。
- `open-ai-desktop/AionU/scripts/afterPack.js`
  electron-builder 打包后校验 hook。适用于理解为什么课程强调“源目录存在”不等于“最终 app resources 中存在”。
- `open-ai-desktop/AionU/scripts/prepare-release-assets.sh`
  CI 多平台构建产物进入 `release-assets/` 前的整理和硬校验脚本。适用于理解发布资产命名、去重、updater metadata 和 WebCLI tarball 校验。
- `open-ai-desktop/AionU/scripts/verify-release-assets.sh`
  发布资产目录的独立校验入口。适用于理解 PR mock release test 当前检查了哪些 canonical metadata、架构 metadata、桌面包和 WebCLI 资产。
- `open-ai-desktop/AionU/packages/shared-scripts/src/verify-bundled-aioncore-resources.js`
  bundled-aioncore 资源校验核心逻辑。适用于判断 aioncore binary、manifest、managed node、ACP manifest/entrypoint 和 node_modules 的缺失边界。
- `open-ai-desktop/AionU/tests/unit/assets/verifyBundledAioncoreResources.test.ts`
  bundled-aioncore 校验器的单元证据。适用于确认测试覆盖的是存在性、平台架构 mismatch、Windows 与非 Windows Node 布局、ACP manifest/entrypoint。
- `open-ai-desktop/AionU/tests/unit/releasePackagingConfig.test.ts`
  发布配置与 release asset preparation 的单元证据。适用于确认 mac zip 必须存在、Windows zip 不应生成、CI 上传 glob 不应漂移。
- `teach/open-ai-desktop/AionU/module-build-release/reference/build-release-overview.html`
  L1 构建发布模块速查。适用于回看 dist 入口、aioncore 资源、electron-builder 和发布资产总览。

## 智慧（社区）

- AionU / AionUi 仓库的 PR review 与 release issue
  最适合检验资源裁剪改动是否会影响真实平台包、自动更新 metadata、安装脚本和用户升级路径。
- Electron Builder 维护社区与 issue 讨论
  适合验证 `files`、`asarUnpack`、`extraResources`、macOS signing/notarization 等跨平台打包行为是否符合工具当前实现。

## 空白

- 当前没有本主题专属的真实 release postmortem。课程只能根据源码、测试和 workflow 推断风险，无法证明历史线上事故频率。
- 当前没有完整真实安装包的跨平台资源清单快照。`verify-release-assets.sh` 使用 mock 资产时能锁脚本契约，但不能替代真实产物抽检。
