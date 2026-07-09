# 全球股票数据工具箱 资源

## 知识

- [global-stock-data/SKILL.md](../../../../../open-trading/Vibe-Research/global-stock-data/SKILL.md) — 完整接口文档：八层数据架构、18 个端点、全部内嵌 Python 调用代码。这是本课程的核心知识来源。
- [global-stock-data/README.md](../../../../../open-trading/Vibe-Research/global-stock-data/README.md) — 项目说明、快速开始、18 端点能力清单、FAQ。适合快速了解项目定位。
- [global-stock-data/CHANGELOG.md](../../../../../open-trading/Vibe-Research/global-stock-data/CHANGELOG.md) — 版本变更记录（v1.0 → v1.0.1）。理解工具包的演进路径和已知问题修复。
- [backend/gstock.py](../../../../../open-trading/Vibe-Research/backend/gstock.py) — Vibe-Research 后端对 global-stock-data 的移植实现。展示从完整工具包到域内合规子集的裁剪策略。
- [东财 push2 接口文档](https://www.eastmoney.com/) — 东方财富行情推送接口（非官方文档，社区逆向总结）。适用于理解 secid 前缀和字段映射。

## 智慧（社区）

- [global-stock-data GitHub Issues](https://github.com/simonlin1212/global-stock-data/issues) — 项目 Issue 区。适用于了解常见问题、向作者提问。
- 作者抖音「Simon林」/ 公众号「硅基世纪」 — 作者个人频道，发布工具更新和使用技巧。

## 空白

- 东财 push2/datacenter 接口无官方公开文档，所有字段映射依赖社区逆向和实测积累，字段含义可能有遗漏或偏差。
- 新浪财经和腾讯财经的行情接口无官方文档，字段映射来自 SKILL.md 作者的标注。
- 目前没有专门针对 global-stock-data 的第三方教程或中文书籍。
