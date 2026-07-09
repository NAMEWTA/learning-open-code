# 使命：Rust 多平台二进制发布链路

## 为什么
学习 codex 的完整发布流水线，掌握从 git tag 推送到最终用户下载多平台二进制包的全过程。当需要为类似项目搭建 CI/CD 发布体系，或排查 codex 发布失败问题时，能够快速定位到具体 job 和步骤，理解每层的职责边界与异常处理机制。

## 成功的样子
- 能画出从 git tag 推送到 GitHub Release + npm publish 的完整时序图，说出 10 个关键 job 的职责
- 能解释 macOS 签名链路（unsigned → AKV PKCS11 签名 → notarize → staple）与 Linux cosign 的区别
- 能在发布失败时根据错误信息定位到具体 job 和步骤，提出修复方向

## 约束条件
- 具备 CI/CD 基础概念（GitHub Actions workflow、job、artifact），不要求深入 Rust 编译知识
- 学习时间：约 30 分钟（两节课）

## 不在范围内
- Bazel/Cargo/pnpm 构建细节（已在 L1-module-build-release 中讲解）
- npm 包内部结构设计（已在 L1-module-cli-packaging 中讲解）
- codex 内部 Rust 代码架构
- Homebrew formula 维护细节
