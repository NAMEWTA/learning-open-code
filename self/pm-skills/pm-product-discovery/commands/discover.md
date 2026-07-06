---
description: 运行完整的 product discovery 流程——从创意构思到假设映射再到实验设计
argument-hint: "<产品或功能创意>"
---

# /discover -- 完整发现流程

运行结构化的 product discovery 流程，从发散思维到聚焦验证。串联多个 skills 为单一的端到端工作流。

## 调用方式

```
/discover 我们项目管理工具的智能通知系统
/discover 新产品：面向非母语者的 AI 写作助手
```

## 工作流

### 第 1 步：理解发现背景——已有产品还是新产品？

### 第 2 步：头脑风暴创意（发散阶段）

应用 **brainstorm-ideas-existing** 或 **brainstorm-ideas-new** skill。检查点："这里有 10 个创意。哪些需要压力测试？选择 3-5 个。"

### 第 3 步：识别假设（批判性思维阶段）

应用 **identify-assumptions-existing** 或 **identify-assumptions-new** skill

### 第 4 步：优先级排序假设（聚焦阶段）

应用 **prioritize-assumptions** skill——在影响 × 风险矩阵上映射假设

### 第 5 步：设计实验（验证阶段）

应用 **brainstorm-experiments-existing** 或 **brainstorm-experiments-new** skill

### 第 6 步：创建发现计划

保存为 markdown：探索的创意 → 选定的创意 → 关键假设表格 → 验证实验 → 时间线 → 决策框架

### 第 7 步：提供后续建议

## 注意事项

- 这是一个 15-30 分钟的结构化工作流
- 在每个检查点，用户可以重定向、跳过或深入
- 发现计划应是一份活文档
