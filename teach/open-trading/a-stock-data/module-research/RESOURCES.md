# 研报层 资源

## 知识

- [SKILL.md § Layer 2 研报层](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  源项目核心文件 L534-808，包含 eastmoney_reports / download_pdf / eastmoney_industry_reports / ths_eps_forecast / iwencai_search 全部实现代码。适用于：所有函数的完整参数和返回值字段参考。

- [东财 reportapi 前端页面](https://data.eastmoney.com/report/stock.jshtml)
  个股研报的浏览器端入口，可用于对照理解 reportapi JSON 字段含义。适用于：查看研报列表的筛选条件和展示字段。

- [同花顺个股 — 机构预测页](https://basic.10jqka.com.cn/new/688017/worth.html)
  一致预期 EPS 的 HTML 页面（以 688017 为例），是 ths_eps_forecast() 的数据来源。适用于：对照验证解析出的 DataFrame 列含义。

- [iwencai SkillHub 文档](https://openapi.iwencai.com)
  iwencai OpenAPI 官方文档，包含 comprehensive/search 和 query2data 端点说明。适用于：理解 channel/search/query 参数组合、API Key 申请流程。

- [pandas read_html 文档](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html)
  ths_eps_forecast() 依赖 pandas.read_html() 解析同花顺 HTML 表格。适用于：了解 HTML 表格解析的参数和兼容性注意事项。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  接口失效报告和修复记录，包含 V3.2.3 行业研报新增、V3.2.5 EPS 列名修复等实战问题。适用于：了解研报层接口的已知坑点。

- [东财数据 API 交流群（非官方）](https://github.com/simonlin1212/a-stock-data/discussions)
  项目 Discussions 区，社区用户分享端点发现和使用技巧。适用于：发现新的东财端点、确认接口是否仍然可用。

## 空白

- 东财 reportapi 无官方文档——所有参数（cb、qType、industryCode 等）均来自逆向分析，无权威参数说明
- 东财行业码无公开码表——需要通过全行业查询 (`industry_code="*"`) 从结果反查，bxpa 等旧端点已 404
- iwencai X-Claw 鉴权机制（SkillHub 2.0）仅有 README 级别说明，缺少详细的 Token 生命周期和限流策略文档
- 同花顺 basic.10jqka.com.cn 的 worth.html 页面无公开 API 文档——ths_eps_forecast() 走 HTML 解析，字段结构可能随页面改版变化
