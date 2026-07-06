---
name: sql-queries
description: "从自然语言描述生成 SQL 查询。支持 BigQuery、PostgreSQL、MySQL 及其他方言。从上传的图表或文档中读取数据库 schema。适用于编写 SQL、构建数据报表、探索数据库，或将业务问题转化为查询语句。"
---

# SQL 查询生成器

## 目的
将自然语言需求转化为跨多种数据库平台的优化 SQL 查询。帮助产品经理、分析师和工程师生成准确的查询，无需手动编写语法。

## 工作方式

### 第 1 步：理解你的数据库 Schema
- 如果你提供了 schema 文件（SQL、文档或图表描述），我会读取并分析它
- 提取表名、列定义、数据类型和关系
- 识别主键、外键和索引策略

### 第 2 步：处理你的请求
- 明确你需要检索或分析的具体数据
- 确认 SQL 方言（BigQuery、PostgreSQL、MySQL、Snowflake 等）
- 询问任何额外需求（过滤、聚合、排序）

### 第 3 步：生成优化查询
- 编写利用数据库结构的高效 SQL
- 包含注释解释复杂逻辑
- 针对大数据集的性能考量
- 如果适用，提供替代方案

### 第 4 步：解释和测试
- 用通俗语言解释查询逻辑
- 建议如何测试或验证结果
- 提供性能优化建议
- 如果需要，生成测试脚本或样本数据

## 使用示例

**示例 1：从 Schema 文件生成查询**
```
上传你的 database_schema.sql 文件，然后说：
"生成一个查询，找出过去 30 天内注册且至少有 5 次活跃会话的用户"
```

**示例 2：从图表描述生成查询**
```
"这是我的数据库结构：Users 表（id、email、created_at），
Sessions 表（id、user_id、timestamp、duration）。
生成一个查询，计算 2026 年 1 月每位用户的平均会话时长。"
```

**示例 3：复杂分析查询**
```
"创建一个 BigQuery 查询，按地区和客户等级分析我们的收入，
包含同比增长率。"
```

## 核心能力

- **多方言支持**：兼容 BigQuery、PostgreSQL、MySQL、Snowflake、SQL Server
- **文件读取**：读取 schema 文件、SQL dump 和数据文档
- **查询优化**：建议索引、分区和性能改进
- **查询解释**：拆解查询逻辑，便于学习和文档编写
- **测试支持**：可生成测试查询和样本数据脚本
- **脚本执行**：为你的数据库创建可执行的 SQL 脚本

## 获取最佳结果的技巧

1. **提供上下文**：分享你的数据库 schema 或结构
2. **明确具体**：清楚描述你需要什么数据以及过滤条件
3. **注明数据库**：指定你使用的 SQL 方言
4. **包含约束条件**：说明数据量、时间范围和性能需求
5. **指定输出格式**：如需特定输出格式，请说明

## 输出格式

你将获得：
- **SQL 查询**：带注释的生产就绪 SQL 代码
- **解释说明**：查询的功能和工作原理
- **性能说明**：优化建议和考量
- **测试脚本**（如需）：样本数据和验证查询

---

### 延伸阅读

- [The Product Analytics Playbook: AARRR, HEART, Cohorts & Funnels for PMs](https://www.productcompass.pm/p/the-product-analytics-playbook-aarrr)
- [How to Become a Technology-Literate PM](https://www.productcompass.pm/p/how-to-become-a-technology-literate)
