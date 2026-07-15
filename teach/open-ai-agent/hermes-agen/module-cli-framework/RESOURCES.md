# CLI 框架 资源

## 知识

### 源码入口（核心）
- [hermes_cli/main.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/main.py) -- CLI 主入口 (565KB, 14177 行)，argparse 树构建、cmd_* 分发、--oneshot 模式
- [hermes_cli/_parser.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/_parser.py) -- 顶级 argparse 解析器构建 (15KB)，chat 子解析器 + 全局标志定义
- [hermes_cli/subcommands/](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/subcommands/) -- 40+ 子命令插件 (200KB)，每个子命令独立 parser builder 模块

### 源码入口（支撑）
- [hermes_cli/__init__.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/__init__.py) -- 包初始化，UTF-8 强制编码 (3.7KB)，`_ensure_utf8()` 保护所有子命令
- [hermes_cli/config.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/config.py) -- 配置管理系统 (374KB)，YAML 解析、损坏备份、Keychain 集成
- [hermes_cli/completion.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/completion.py) -- Shell 自动补全生成 (11KB)，支持 bash/zsh/fish，实时遍历 argparse 树
- [hermes_cli/console_engine.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/console_engine.py) -- 安全控制台命令引擎 (63KB)，`hermes console` 的命令适配器
- [hermes_cli/env_loader.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_cli/env_loader.py) -- 环境变量加载 (16KB)，`.env` 解析与配置融合

### 官方文档与标准
- [argparse 官方文档](https://docs.python.org/3/library/argparse.html) -- Python 标准库命令行解析器，hermes_cli 的子命令系统构建基础
- [Hermes Agent GitHub](https://github.com/NousResearch/hermes-agent) -- 项目仓库，含安装说明与基本用法
- [pyproject.toml 入口点定义](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/pyproject.toml) -- `console_scripts` 条目映射 `hermes` 命令到 `hermes_cli.main:main`

## 智慧（社区）

- [Nous Research Discord](https://discord.gg/nousresearch) -- Nous Research 官方社区，Hermes Agent 开发者活跃于此
- [Hermes Agent GitHub Issues](https://github.com/NousResearch/hermes-agent/issues) -- 问题追踪，可观察 CLI 相关 bug 和需求讨论

## 空白

- hermes_cli 的 god-file 分解计划（从 main.py 的 14177 行逐步抽离到 subcommands/ 目录）尚无公开设计文档详细记录迁移阶段与策略
- console_engine.py 的 ConsoleCommand 注册与适配器模式在官方文档中未独立说明
- 尚无第三方教程系统讲解 Hermes CLI 子命令开发流程——目前知识来源主要依赖源码阅读
