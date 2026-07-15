# Agent 入口层 资源

## 知识

### 源码入口（核心）
- [cli.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/cli.py) -- CLI 主入口 (726KB, 16184行)，Fire 框架注册 200+ 命令，交互式 REPL 实现
- [run_agent.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/run_agent.py) -- Agent 主运行循环 (263KB, 6013行)，AIAgent 类定义及 run_conversation() 入口
- [hermes_state.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_state.py) -- 核心状态管理 (269KB, 6322行)，SQLite FTS5 会话存储与全文搜索

### 源码入口（支撑）
- [hermes_bootstrap.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_bootstrap.py) -- 启动引导，Windows UTF-8 修复与 sys.path 加固
- [hermes_constants.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_constants.py) -- 全局常量 (37KB)，零依赖的配置路径解析与平台检测
- [hermes_logging.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_logging.py) -- 日志系统配置 (30KB)，旋转文件处理器与会话上下文注入
- [hermes_time.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/hermes_time.py) -- 时区感知的统一时间获取 now() 函数

### 源码入口（扩展）
- [mcp_serve.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/mcp_serve.py) -- MCP 协议服务入口 (35KB)，FastMCP 服务端暴露消息会话工具
- [model_tools.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/model_tools.py) -- 模型工具编排层 (61KB)，工具定义获取与函数调用分发
- [toolsets.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/toolsets.py) -- 工具集注册 (34KB)，命名工具别名的组合与解析
- [batch_runner.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/batch_runner.py) -- 批量轨迹生成器 (56KB)，多进程并行 + 检查点容错
- [trajectory_compressor.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/trajectory_compressor.py) -- 轨迹压缩器 (67KB)，训练数据 token 预算内压缩
- [utils.py](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/utils.py) -- 通用工具函数 (20KB)，真值解析、原子文件写、URL 处理

### 官方文档
- [Hermes Agent GitHub](https://github.com/NousResearch/hermes-agent) -- 项目仓库，含 README、安装说明与基本用法
- [pyproject.toml 依赖定义](/Users/wta/Documents/01-Code/myCode/github-opensource/learning-open-code/open-ai-agent/hermes-agen/pyproject.toml) -- 所有 Python 依赖精确版本和构建配置
- [Google Fire 文档](https://github.com/google/python-fire) -- CLI 框架使用指南，cli.py 和 run_agent.py 的命令注册依赖于此
- [SQLite FTS5 文档](https://www.sqlite.org/fts5.html) -- FTS5 全文搜索引擎，hermes_state.py 的搜索能力基础

## 智慧（社区）

- [Nous Research Discord](https://discord.gg/nousresearch) -- Nous Research 官方社区，Hermes Agent 开发者活跃于此
- [Hermes Agent GitHub Issues](https://github.com/NousResearch/hermes-agent/issues) -- 问题追踪，可观察真实使用场景和 bug 讨论

## 空白

- 暂无第三方教程或博客文章系统讲解 Hermes Agent 入口层架构——目前知识来源主要是源码阅读和 GitHub 仓库文档
- hermes_bootstrap.py 的 Windows UTF-8 修复机制在官方文档中未详细说明
- trajectory_compressor.py 的设计思路与压缩策略尚无公开设计文档
