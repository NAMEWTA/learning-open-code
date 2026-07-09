# 使命：主题研报批量检索全链路

## 为什么
用户希望在投资研究中快速获取某一主题（如"人形机器人""低空经济"）的全部机构研报——通过多关键词语义搜索发现不同角度的研报，去重合并后下载PDF原文，形成对该产业链的全面机构观点覆盖。

## 成功的样子
- 能编写多关键词列表，通过 iwencai 并行搜索获取广度覆盖
- 能对搜索结果进行 UID 去重，保留每组最高分段落
- 能通过东财 reportapi 交叉补充同标的研报并下载 PDF
- 能处理 iwencai 超时/401、PDF 下载 403 Referer 等异常路径

## 约束条件
- iwencai 需 API Key + X-Claw Headers (SkillHub 2.0)，不是免费接口
- 东财 reportapi 免费无 key，但需 Referer 鉴权 + `em_get` 限流
- 需已掌握研报层基础知识（已在 L1 module-research 中讲解）

## 不在范围内
- 研报内容的 NLP 分析或情感打分
- 个股深度估值分析（另有 `slice-single-valuation` 主题）
- iwencai 的数据查询模式（`iwencai_query`），本主题聚焦搜索模式
