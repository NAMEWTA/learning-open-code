---
name: prioritize-assumptions
description: "使用影响 × 风险矩阵对假设进行优先级排序，并为每项假设建议实验方法。适用于对假设列表进行分类、决定先测试什么，或应用假设优先级画布。"
---

## 优先级排序假设

使用影响 × 风险矩阵对假设进行分类，并建议有针对性的实验。

### 背景

你正在帮助为 **$ARGUMENTS** 排定假设的优先级。

如果用户提供了包含假设或研究数据的文件，请先阅读。

### 领域背景

**ICE** 非常适用于假设优先级排序：影响（机会得分 × 客户数）× 信心（1–10）× 容易度（1–10）。机会得分 = 重要性 × (1 − 满意度)，归一化到 0–1（Dan Olsen）。**RICE** 将影响拆分为触达 × 影响：(R × I × C) / E。完整公式和模板参见 `prioritization-frameworks` skill。

### 操作指引

用户将提供一个待排序的假设列表。应用以下框架：

1. **对每个假设**，评估两个维度：
   - **影响**：验证该假设所创造的价值 AND 受影响的客户数量（在 ICE 中：影响 = 机会得分 × 客户数）
   - **风险**：定义为 (1 - 信心) × 工作量

2. **使用影响 × 风险矩阵对每个假设进行分类**：
   - **低影响，低风险** → 推迟测试，优先处理更高优先级的假设
   - **高影响，低风险** → 直接实施（低风险，高回报）
   - **低影响，高风险** → 放弃该创意（不值得投资）
   - **高影响，高风险** → 设计实验进行测试

3. **对每个需要测试的假设**，建议一个实验：
   - 以最小工作量最大化验证学习
   - 衡量实际行为，而非意见
   - 有明确的成功指标和阈值

4. **呈现结果**为优先级排序矩阵或表格。

逐步思考。如果输出较多，保存为 markdown。

---

### 延伸阅读

- [Assumption Prioritization Canvas: How to Identify And Test The Right Assumptions](https://www.productcompass.pm/p/assumption-prioritization-canvas)
- [Continuous Product Discovery Masterclass (CPDM)](https://www.productcompass.pm/p/cpdm)（视频课程）
