# Bazel、CI 与发布链路 资源

## 知识

- [Bazel 官方文档](https://bazel.build/docs) — Bazel 构建系统的权威参考，涵盖 BUILD 文件语法、模块扩展、平台与工具链
- [rules_rust 文档](https://bazelbuild.github.io/rules_rust/) — Bazel 中 Rust 构建规则集，Codex 核心构建基础设施
- [rules_rs 仓库](https://github.com/bazel-contrib/rules_rs) — rules_rust 的下一代实验性重写，Codex 已迁移至此
- [BuildBuddy 文档](https://www.buildbuddy.io/docs/) — 远程构建执行与缓存服务，Codex CI 使用 BuildBuddy 加速
- [GitHub Actions 文档](https://docs.github.com/en/actions) — CI 流水线平台参考
- [Cargo Book](https://doc.rust-lang.org/cargo/) — Rust 包管理与构建系统，Codex 本地开发使用 Cargo
- [pnpm Workspace 文档](https://pnpm.io/workspaces) — pnpm monorepo 工作区配置
- [Just 命令运行器](https://github.com/casey/just) — Codex 本地开发任务入口
- [Zig 作为 C/C++ 交叉编译工具链](https://ziglang.org/) — Codex musl 构建使用 Zig cc

## 源码入口（本地快照）

| 文件 | 职责 |
|------|------|
| `BUILD.bazel` | 顶层 Bazel 构建文件，定义平台、工具链与别名 |
| `MODULE.bazel` | Bazel 模块定义，外部依赖与 patch 声明 |
| `defs.bzl` | 自定义 Bazel 宏 `codex_rust_crate` 和测试规则 |
| `.bazelrc` | Bazel 全局配置（缓存、平台、CI config、clippy） |
| `.bazelversion` | 锁定 Bazel 版本为 9.0.0 |
| `rbe.bzl` | 远程构建执行平台定义 |
| `codex-rs/Cargo.toml` | Rust workspace 成员与依赖声明 |
| `package.json` | 顶层 npm workspace 配置 |
| `pnpm-workspace.yaml` | pnpm monorepo 工作区定义 |
| `justfile` | 本地开发任务（构建/测试/格式化/lint） |
| `scripts/build_codex_package.py` | 核心构建打包脚本入口 |
| `scripts/stage_npm_packages.py` | npm 发布准备脚本 |
| `.github/workflows/rust-release.yml` | Rust 多平台发布流水线 |
| `.github/workflows/rust-release-windows.yml` | Windows 平台发布流水线 |
| `.github/workflows/rust-release-prepare.yml` | 发布准备流水线 |
| `flake.nix` / `flake.lock` | Nix 开发环境定义 |
| `patches/` | 第三方依赖补丁目录 |

## 智慧（社区）

- [Bazel Slack](https://bazelbuild.slack.com/) — Bazel 用户与开发者社区
- [rules_rust GitHub Discussions](https://github.com/bazelbuild/rules_rust/discussions) — Rust + Bazel 集成的社区交流

## 空白

- 未找到 Codex 项目专属的构建/发布公开文档。构建知识主要从 `.bazelrc`、`MODULE.bazel`、CI workflow 文件和 `defs.bzl` 注释中提取。
- Homebrew formula 发布流程未找到公开版本——可能位于私有仓库或通过 GitHub Release 自动化触发。
