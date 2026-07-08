# RAG 功能模块资源

## 知识

- [官方架构文档：RAG 流水线](../../../../open-java/snail-ai/docs/architecture/rag-pipeline.md)
  官方说明文档摄入、检索、融合、Rerank 和上下文注入的概念流程。适用于建立模块全景，并和源码差异做对照。
- [DocumentPipeline.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/pipeline/DocumentPipeline.java)
  文档摄入核心管线。适用于定位解析、分片、chunk 持久化、向量库和搜索引擎双写边界。
- [RagSearchPipeline.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/search/pipeline/RagSearchPipeline.java)
  检索管线调度器。适用于理解 Spring `List<RagSearchHandler>` 如何串起配置解析、向量检索、BM25、融合、重排和收尾。
- [RAG 检索 handlers](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/search/pipeline/handler)
  当前检索阶段的真实实现。适用于核对 `@Order` 顺序、启停条件、指标字段和源码相对官方文档的差异。
- [RAG 分片策略](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy/chunker)
  默认、delimiter、regex、smart 四类分片策略。适用于后续摄入切片学习。
- [RAG 文档解析策略](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy/parser)
  PDF、DOCX、Excel、Markdown、HTML、TXT 解析器。适用于确认当前源码实际支持的文件格式。
- [RagDocumentController.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/RagDocumentController.java)
  Admin 文档上传、预览、提交、重处理和分页入口。适用于定位对外摄入接口。
- [RagSearchController.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/RagSearchController.java)
  Admin 知识库 CRUD、搜索调试和流式问答入口。适用于定位对外检索接口。
- [RAG DTO 与枚举](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/dto)
  `ChunkDTO`、`KnowledgeInfoDTO` 等管线流转对象。适用于对照 `reference/rag-api.html` 字段含义。
- [RAG 枚举与去重模型](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/enums)
  分片模式、融合策略、文档状态、去重策略与动作。适用于确认配置值与运行时枚举映射。
- [去重决策类型](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/dedup)
  `DedupResult`、`UploadDecision` 及命中维度枚举。适用于上传预览/提交切片学习。
- [RagSearchHandler 与 RagSearchContext](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/search/pipeline)
  检索管线契约与共享上下文字段。适用于扩展或调试检索阶段。
- [导入/解析/分片/融合策略接口](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/strategy)
  `DocumentImportStrategy`、`DocumentParser`、`ChunkStrategy`、`HybridFusion` 及其实现类。适用于新增文件格式或分片算法。
- [ContentHashUtil.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/util/ContentHashUtil.java)
  内容 SHA-256 哈希工具。适用于去重与 `ImportResult.contentHash` 一致性核对。

## 智慧（社区）

- 当前主题暂不引入外部社区材料；以本工作区源码、官方文档和后续源码审查记录作为主要反馈来源。

## 空白

- 未检索外部 Issue、PR 或社区讨论，后续若分析真实缺陷或设计争议，应补充对应讨论链接。
- 当前没有针对 RAG 模块的测试用例清单；后续切片课需要继续搜索测试目录或补充可执行验证路径。
