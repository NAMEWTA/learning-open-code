# CONTEXT.md 格式

## 结构

```md
# {上下文名称}

{一两句话描述这个上下文是什么以及它为什么存在。}

## 语言

**Order**：
{一两句话描述该术语}
_Avoid_：Purchase, transaction

**Invoice**：
交付后发送给客户的付款请求。
_Avoid_：Bill, payment request

**Customer**：
下订单的个人或组织。
_Avoid_：Client, buyer, account
```

## 规则

- **要有明确观点。** 当同一概念存在多个词时，选择最好的一个，并在 `_Avoid_` 下列出其他的。
- **保持定义精炼。** 最多一两句话。定义它是什么，而不是它做什么。
- **只包含此项目上下文特有的术语。** 通用编程概念（超时、错误类型、工具模式）即使项目大量使用也不应包含。在添加术语之前，问自己：这是一个此上下文独有的概念，还是一个通用编程概念？只有前者才属于这里。
- **当自然出现聚类时将术语分组到子标题下。** 如果所有术语属于一个统一的领域，扁平列表也可以。

## 单上下文 vs 多上下文仓库

**单上下文（大多数仓库）：** 仓库根目录下一个 `CONTEXT.md`。

**多上下文：** 仓库根目录下一个 `CONTEXT-MAP.md`，列出上下文、它们的位置以及它们如何相互关联：

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md) — generates invoices and processes payments
- [Fulfillment](./src/fulfillment/CONTEXT.md) — manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

此技能推断适用哪种结构：

- 如果 `CONTEXT-MAP.md` 存在，读取它来查找上下文
- 如果只有根目录下的 `CONTEXT.md`，则为单上下文
- 如果两者都不存在，在解析第一个术语时按需延迟创建根目录下的 `CONTEXT.md`

当存在多个上下文时，推断当前主题与哪个上下文相关。如果不清楚，请询问。
