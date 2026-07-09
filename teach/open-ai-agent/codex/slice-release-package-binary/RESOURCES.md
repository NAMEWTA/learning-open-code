# Rust 多平台二进制发布链路 资源

## 知识

- [GitHub Actions 官方文档 — Workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — GitHub Actions workflow 语法参考。适用于理解 job 依赖、matrix strategy、environment、concurrency 等配置项。
- [GitHub Actions 官方文档 — OIDC 信任发布](https://docs.github.com/en/actions/security-for-github-actions/using-openid-connect-for-reusable-workflows) — npm OIDC 发布基于此机制。适用于理解 publish-npm job 的无 token 认证方式。
- [npm Trusted Publishers 文档](https://docs.npmjs.com/trusted-publishers) — npm OIDC 可信发布机制说明。适用于理解为何 publish-npm 不需要 NODE_AUTH_TOKEN。
- [Azure Key Vault PKCS11 签名](https://learn.microsoft.com/en-us/azure/key-vault/keys/about-keys) — macOS 代码签名使用的 AKV 密钥管理。适用于理解 sign-macos-binaries job 的签名流程。
- [Apple 代码签名指南](https://developer.apple.com/documentation/security/code_signing_services) — macOS 二进制签名与公证机制。适用于理解 sign、notarize、staple 三步流程。
- [cosign 签名工具](https://github.com/sigstore/cosign) — Linux 二进制签名方案。适用于理解 Linux 平台的 Cosign 签名步骤。
- [softprops/action-gh-release](https://github.com/softprops/action-gh-release) — 本流水线使用的 GitHub Release 创建 Action。适用于理解 release job 的发布行为。
- [facebook/dotslash-publish-release](https://github.com/facebook/dotslash-publish-release) — DotSlash 可执行文件发布方案。适用于理解 publish-dotslash job 的作用。

## 智慧（社区）

- [GitHub Actions Community Forum](https://github.com/orgs/community/discussions/categories/actions) — 讨论 Actions 使用问题，适合遇到 CI 配置疑难时提问
- [OpenAI Codex GitHub Issues](https://github.com/openai/codex/issues) — 发布相关的 issue 可直接在此反馈

## 空白

- Homebrew formula 的具体维护流程（codex 的 Homebrew tap 细节未在源码中暴露）
- winget-pkgs PR 的审核周期与社区规范（仅通过 vedantmgoyal9/winget-releaser 自动化提交）
