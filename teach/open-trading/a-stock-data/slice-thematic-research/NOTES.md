# 教学笔记：主题研报批量检索全链路

## 教学要点

- 强调 iwencai 的"唯一价值"——NL 语义搜索是其他数据源无法替代的能力
- 强调东财 PDF 下载的 Referer 鉴权是常见坑点，403 时首先检查 Referer
- 去重逻辑 `dedup_articles` 虽然是简单的 dict 去重，但 uid 的 fallback 逻辑值得关注

## 学生常见疑问

- "iwencai 和东财 reportapi 有什么区别？" → iwencai 是主题搜索（NL语义），东财是按股票代码查研报，两者互补
- "为什么不用 ChatGPT 直接分析研报内容？" → PDF 下载后可用 AI 工具分析，但数据采集层的关注点是"获取到哪些研报"
