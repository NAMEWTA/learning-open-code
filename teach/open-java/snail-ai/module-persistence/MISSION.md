# 使命：持久化与存储适配模块

## 为什么
学习者需要把 Snail AI 的业务库、向量库和搜索引擎边界放回整体架构中理解，知道 RAG、Memory 和 Admin 管理入口为什么可以在不同存储后端之间切换。掌握这个边界后，后续下钻 PgVector、Milvus、Elasticsearch 或 MyBatis-Plus 方言时，能先判断自己正在看的是业务数据、向量索引还是全文索引。

## 成功的样子
- 能说清 `snail-ai-server-persistence` 的三类子模块：业务库、向量存储、搜索存储。
- 能从 `StoreInstanceController` 追到 `sai_store_instance`、`VectorStoreFactory` 和 `SearchEngineFactory`。
- 能判断一个 RAG 或 Memory 变更应该依赖 mapper/PO、向量模板接口，还是搜索引擎接口。
- 能按领域（app、agent、skill、admin、mcp、openapi、rag、model、vector、search）快速查到 PO 字段、Mapper 签名和存储 DTO/异常类型。

## 约束条件
- L1 lesson 必须控制为 15 分钟短课；L3 接口清单写入 `reference/persistence-api.html`。
- 模块职责、Factory 路由、StoreInstance 管理见 `reference/persistence-overview.html`。
- PO/Mapper 字段与方法签名见 `reference/persistence-api.html`，与 overview 互补、避免重复。
- 输出限定在 `teach/open-java/snail-ai/module-persistence/`。

## 不在范围内
- 不逐行讲解方言 XML 和初始化 SQL（见 overview 与后续 L2 切片）。
- 不展开 PgVector、Milvus、Elasticsearch 的完整读写实现。
- 不讲 RAG 摄入、检索融合或 Memory 注入的完整垂直切片。
