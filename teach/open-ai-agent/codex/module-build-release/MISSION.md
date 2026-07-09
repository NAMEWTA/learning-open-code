# 使命：Bazel、CI 与发布链路

## 为什么
理解 Codex 如何从 Rust/TypeScript/Python 源码构建为多平台二进制，经过 CI 验证后发布到 npm 和 Homebrew，是参与 codex 项目贡献、定制构建或排查发布问题的前置条件。

## 成功的样子
- 能说出 Codex 使用的 3 个构建工具（Bazel、Cargo、pnpm）各自的职责边界
- 能阅读 `.bazelrc` 中的 CI 配置并解释不同平台构建策略
- 能追踪一个 `rust-v*.*.*` tag 从 push 到 GitHub Release 的完整发布链路

## 约束条件
- L1 模块导览课，15 分钟内完成
- 只定位到文件/函数级别，不深入单个 Rust crate 的实现细节
- 覆盖 Bazel 构建体系、CI 流水线和发布脚本三条主线

## 不在范围内
- 单个 Rust crate 内部的 Cargo.toml 依赖解析细节
- SDK (Python/TypeScript) 的独立构建与发布流程
- Nix flake 的日常开发工作流深入分析
