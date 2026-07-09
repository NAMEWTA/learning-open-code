# 教学笔记：研报层

- 研报层是 a-stock-data 10 层架构中唯一同时使用东财、同花顺、iwencai 三大数据源的层
- 东财 reportapi 是主力（免费、覆盖全），iwencai 是唯一能 NL 搜索的补充
- 重点提醒学习者：东财所有端点走 em_get() 限流，忽略此点会封 IP
- iwencai 需 API Key——提醒学习者未申请 Key 时跳过 2.3 节，不影响其他层
- 同花顺直连无鉴权，但 HTML 解析脆弱——提醒关注 V3.2.5 的 EPS 列名修复
