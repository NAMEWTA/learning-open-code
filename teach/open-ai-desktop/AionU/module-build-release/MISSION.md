# 使命：构建与发布模块

## 为什么
AionU 的构建发布链同时覆盖 Electron 桌面包、WebCLI tarball、aioncore runtime、Homebrew 模板和发布资产校验。学习这个模块的目标是让读者能判断一次发布从源码编译到可分发产物之间经过哪些闸门，以及出问题时应该先查哪个脚本。

## 成功的样子
- 能从 `package.json` 的构建脚本追到 `electron-vite`、`electron-builder`、aioncore 准备和发布资产整理。
- 能说清桌面包、WebCLI 包、Homebrew 模板、Dockerfile 各自的职责边界。
- 能用测试文件解释 aioncore bundle、Windows 快速构建和安装脚本的关键断言。

## 约束条件
- 本主题是 L1 模块总览，只建立模块边界、接口、依赖和调用示例；长清单放入 reference。
- lesson 控制在 15 分钟内，只讲一条构建发布主线。
- 以当前源项目源码为准，不假设远端 CI 配置或发布流程未读文件中的行为。

## 不在范围内
- 不展开 Electron 主入口生命周期；需要时跳转到 `module-main-entry`。
- 不展开 WebHost/WebCLI 运行时内部行为；需要时跳转到 `module-web-runtime`。
- 不讲 GitHub Actions 工作流实现细节，除非后续 L2/L4 专门覆盖发布流水线。
