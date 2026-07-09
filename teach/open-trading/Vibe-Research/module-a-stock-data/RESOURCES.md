# A股数据工具箱 资源

## 知识

- [SKILL.md：`open-trading/a-stock-data/SKILL.md`](../../../../open-trading/a-stock-data/SKILL.md)
  a-stock-data 的完整接口文档，十层数据架构、40 个端点、内嵌全部调用代码。这是本模块教学的权威来源，所有端点说明和代码示例均以此为准。
- [README.md：`open-trading/a-stock-data/README.md`](../../../../open-trading/a-stock-data/README.md)
  项目说明、架构图、端点清单、快速开始指南与版本亮点（V3.0-V3.3）。
- [CHANGELOG.md：`open-trading/a-stock-data/CHANGELOG.md`](../../../../open-trading/a-stock-data/CHANGELOG.md)
  版本变更记录（v1.0 → v3.3.0），记录了每次版本迭代中新增的端点、失效接口替换、Bug 修复与实测验证细节。是理解工具箱演进历史的最佳来源。
- [backend/astock.py：`open-trading/Vibe-Research/backend/astock.py`](../../../../open-trading/Vibe-Research/backend/astock.py)
  Vibe-Research 后端 A 股数据层，移植自 a-stock-data。809 行，展示了如何将 SKILL.md 中的独立代码片段整合为 FastAPI 服务端点。
- [上游仓库：simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data)
  a-stock-data 的 GitHub 主页，适用于获取最新版本、阅读 issue、提交反馈。本教学以本地子模块快照（v3.3.0）为准。

## 智慧（社区）

- [GitHub Issues：simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data/issues)
  适用于了解真实用户的使用问题、数据源失效反馈、功能需求讨论。
- [Vibe-Research GitHub Discussions](https://github.com/simonlin1212/Vibe-Research/discussions)
  适用于了解 a-stock-data 在 Vibe-Research 项目中的实际集成经验与使用心得。

## 空白

- 当前未找到针对 a-stock-data 的独立第三方教程或深度解读文章；社区内容以 GitHub issue 讨论为主。
- 东财各接口的底层 API 协议细节没有公开文档，SKILL.md 中的参数和字段均来自社区逆向与实测校准，部分接口可能在东财官网改版后失效。
