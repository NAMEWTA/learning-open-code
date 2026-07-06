---
name: prioritize-features
description: "基于影响、工作量、风险和战略对齐度对功能待办列表进行优先级排序，给出前 5 推荐。适用于优先级排序功能待办、做范围决策，或排列产品创意。"
---

## 优先级排序功能待办列表

评估并排列功能创意待办列表，识别出应优先推进的前 5 个。

### 背景

你正在帮助为 **$ARGUMENTS** 排定功能的优先级。

如果用户提供了文件（电子表格、待办列表、机会评估），直接读取并分析。

### 领域背景

框架选择指南参见 `prioritization-frameworks` skill。关键建议：

**机会得分**（Dan Olsen，《The Lean Product Playbook》）推荐用于评估客户问题：机会得分 = 重要性 × (1 − 满意度)，归一化到 0–1。高重要性 + 低满意度 = 最好的机会。优先考虑**问题（机会）**，而非解决方案。

**ICE** 推荐用于快速评分：影响（机会得分 × 客户数）× 信心 × 容易度。**RICE** 对大型团队将触达作为单独因子加入。

### 操作指引

用户将描述其产品目标、期望成果，并提供功能创意。依次完成以下步骤：

1. **理解优先级**：确认产品目标和成功指标。

2. **评估每个功能**，对照：
   - **影响**：它对期望成果的推动力有多大？如有客户数据，考虑机会得分。
   - **工作量**：需要多少开发、设计和协调工作？
   - **风险**：存在多少不确定性？哪些假设需要测试？
   - **战略对齐度**：它与产品愿景和当前目标的匹配度如何？

3. **推荐前 5 个功能**，附带：
   - 明确的排名（1-5）
   - 每个选择的简要理由
   - 考虑的关键权衡
   - 什么被降级了以及为什么

4. **如有帮助，以优先级表格呈现**。

逐步思考。如果输出较多，保存为 markdown。

---

### 延伸阅读

- [Kano Model: How to Delight Your Customers Without Becoming a Feature Factory](https://www.productcompass.pm/p/kano-model-how-to-delight-your-customers)
- [The Product Management Frameworks Compendium + Templates](https://www.productcompass.pm/p/the-product-frameworks-compendium)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm)（视频课程）
