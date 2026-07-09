# 公告层 资源

## 知识

- [SKILL.md 公告层章节 (§7.1-§7.2)](https://github.com/simonlin1212/a-stock-data/blob/main/SKILL.md)
  公告层完整代码块：_cninfo_ts_to_date() 时间戳转换、_cninfo_orgid() 动态 orgId 映射（含 V3.2.2 修复说明）、cninfo_announcements() 公告全文检索、mootdx F10 公告摘要。适用于：复制即用的代码参考、orgId 故障排查。

- [巨潮资讯网 (cninfo.com.cn)](https://www.cninfo.com.cn/)
  中国证监会指定上市公司信息披露网站，沪深北三市全量公告原文。适用于：验证公告链接、手动浏览公告类型分类、理解 orgId 与股票代码的映射关系。

- [mootdx 官方文档 (pytdx)](https://github.com/rainx/pytdx)
  通达信 TCP 协议 Python 封装。F10 模块提供公司资料（9 大类文本）含最新公告摘要。适用于：深入理解 F10 的 name 参数选项。

## 智慧（社区）

- [a-stock-data GitHub Issues](https://github.com/simonlin1212/a-stock-data/issues)
  项目问题追踪。#19 记录了硬编码 orgId 导致 601xxx 公告缺失的完整排查过程与修复方案。适用于：了解该 Bug 的根因分析思路。

- [r/chinastocks](https://reddit.com/r/chinastocks)（英文）
  A 股投资讨论社区。适用于：了解公告在投资决策中的实际使用场景，但信息密度一般。

## 空白

- 巨潮 cninfo API 无官方文档——_cninfo_orgid() 使用的 szse_stock.json 端点为社区发现，无公开说明
- 缺少巨潮公告检索 API 的参数完整说明——pageSize/pageNum 分页行为、sortName/sortType 可选值、公告类型分类编码均靠实测推演
- mootdx F10 的 name 参数（如"最新提示"）依赖通达信协议约定，无官方字段对照表
