---
name: analyze-feature-requests
description: "按主题、战略对齐度、影响、工作量和风险对功能请求列表进行分析和优先级排序。适用于审查客户功能请求、分类待办列表，或做优先级决策。"
---

## 分析功能请求

对照产品目标对客户功能请求进行分类、评估和优先级排序。

### 背景

你正在分析 **$ARGUMENTS** 的功能请求。

如果用户提供了文件（电子表格、CSV 或包含功能请求的文档），直接读取并分析。如果数据是结构化格式，考虑创建汇总表。

### 领域背景

绝不允许客户设计解决方案。优先考虑**机会（问题）**，而非功能。使用**机会得分**（Dan Olsen）来评估客户报告的问题：机会得分 = 重要性 × (1 − 满意度)，归一化到 0-1。完整详情和模板参见 `prioritization-frameworks` skill。

### 操作指引

用户将描述其产品目标并提供功能请求。依次完成以下步骤：

1. **理解目标**：确认将指导优先级排序的产品目标和期望成果。

2. **将请求按主题分类**：将相关请求分组，为每个主题命名。

3. **评估战略对齐度**：对每个主题，评估其与所述目标的对齐程度。

4. **优先选出前 3 个功能**，基于：
   - **影响**：客户价值和受影响的用户数量
   - **工作量**：所需的开发和设计资源
   - **风险**：技术和市场不确定性
   - **战略对齐度**：与产品愿景和目标的匹配度

5. **对每个优先功能**，提供：
   - 理由（客户需求、战略对齐度）
   - 值得考虑的替代方案
   - 高风险假设
   - 如何以最小工作量测试这些假设

逐步思考。保存为 markdown 或创建结构化的输出文档。

---

### 延伸阅读

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm)（视频课程）
