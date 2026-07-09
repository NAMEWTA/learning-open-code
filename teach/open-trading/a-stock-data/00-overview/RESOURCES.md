# a-stock-data 项目总览 资源

## 知识

- [SKILL.md（项目主文件）](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  109KB 自包含 Skill 文件，内含全部 Python 代码（~60 个函数）+ 10 层架构文档。适用于：所有端点的代码实现参考、数据源参数细节。

- [README.md（项目说明）](https://github.com/simonlin1212/a-stock-data/blob/main/README.md)
  项目架构图、快速开始、40 端点清单、使用示例、FAQ。适用于：快速了解项目全貌、查找端点能力对照。

- [CHANGELOG.md（版本日志）](https://github.com/simonlin1212/a-stock-data/blob/main/CHANGELOG.md)
  从 V1.0 到 V3.3.0 的完整演进记录，包含每次修复的根因分析。适用于：理解版本演进路线、各数据源的替换决策背景。

- [mootdx 官方文档](https://github.com/rainx/pytdx)
  通达信 TCP 行情接口的 Python 封装。适用于：深入理解 K 线参数、财务数据字段含义、F10 分类。

- [东财数据中心 API 参考](https://data.eastmoney.com/)
  龙虎榜、解禁、融资融券等数据的前端页面。适用于：对照理解 datacenter API 的 reportName 和字段含义。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题追踪，包含大量实测反馈和接口失效报告。适用于：了解已知问题、贡献修复方案。

- [TradingAgents 社区](https://github.com/simonlin1212/TradingAgents-astock)
  作者的另一项目，AI 驱动的 A 股投研 Agent。适用于：看 a-stock-data 在实际 AI Agent 中的集成方式。

## 空白

- 缺少东财 API 的官方文档或公开规范——所有端点和参数均来自社区逆向分析和实测，无官方维护
- 缺少 iwencai SkillHub 的详细开发文档——API Key 申请流程和 X-Claw 鉴权机制仅有 README 级别的说明
- 缺少 A 股数据领域的中文系统化教程——目前资源以英文技术文档和项目 README 为主
