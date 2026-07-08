# 资源管理模块资源

## 知识

- [snail-ai-feature-resource/pom.xml](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/pom.xml)
  资源 feature 模块 Maven 坐标与直接依赖（commons-core、biz-template、minio、okhttp-jvm）。适用于理解构建边界与持久化/对象存储能力来源。
- [snail-ai-server-features/pom.xml](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/pom.xml)
  feature 聚合 POM，列出 `snail-ai-feature-resource` 在 server-features 中的位置。
- [ResourceService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/ResourceService.java)
  资源上传、加载、删除、按 storageKey 查询和 `bizType` 调整的核心服务。适用于理解文件流、元数据和访问 URL 如何闭环。
- [ResourceController.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/ResourceController.java)
  管理端资源上传、删除、分页接口。适用于区分登录态管理接口与公开文件访问接口。
- [ResourceAdminService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/resource/ResourceAdminService.java)
  管理端上传默认业务类型、分页筛选和删除授权逻辑。适用于理解 creator/admin 权限边界。
- [FileAccessController.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/FileAccessController.java)
  `/files/**` 公开资源代理入口。适用于理解 storageKey 校验、inline/attachment、缓存和 `nosniff` 响应头。
- [SnailJobWebMvcConfigurerAdapter.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/interceptor/SnailJobWebMvcConfigurerAdapter.java)
  Web 拦截器排除 `/openapi/**` 和 `/files/**`。适用于确认文件访问入口不走登录拦截器。
- [ResourceStorageService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/ResourceStorageService.java)
  存储策略接口。适用于理解本地、MinIO、外部 URL 等实现需要满足的最小契约。
- [ResourceStorageFactory.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/ResourceStorageFactory.java)
  按配置选择默认存储或按类型取具体存储。适用于排查 `storageType` 配置和 Bean 注册问题。
- [LocalResourceStorageService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/LocalResourceStorageService.java)
  本地文件系统存储实现。适用于理解上传目录、路径穿越防护和 `/files/{storageKey}` 访问 URL。
- [MinioResourceStorageService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/MinioResourceStorageService.java)
  MinIO 存储实现。适用于理解对象 key、bucket 初始化、上传、读取和删除。
- [ResourceConfig.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/config/ResourceConfig.java)
  `snail-ai.resource.*` 配置绑定对象。适用于定位默认存储类型、上传目录和 MinIO 连接参数。
- [StorageKeyGenerator.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/util/StorageKeyGenerator.java)
  生成 `{bizType}/{yyyy}/{MM}/{dd}/{uuid}.{ext}` 存储键。适用于理解公开访问凭证为什么不暴露自增 ID。
- [MimeTypeUtils.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/util/MimeTypeUtils.java)
  基于扩展名和 JDK 猜测 MIME 类型。适用于理解响应 Content-Type 来源。
- [ResourcePO.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/resource/po/ResourcePO.java)
  `sai_resource` 持久化对象。适用于理解资源元数据字段。
- [ResourceMapper.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/resource/mapper/ResourceMapper.java)
  MyBatis-Plus `BaseMapper<ResourcePO>`。适用于确认资源表没有额外 XML 映射。
- [snail_ai_schema.sql](../../../../open-java/snail-ai/docs/sql/snail_ai_schema.sql)
  `sai_resource`、`sai_rag_document.resource_id`、`sai_user.resource_id` 表结构。适用于确认唯一键、索引和业务外键关系。
- [RagDocumentService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/rag/RagDocumentService.java)
  RAG 直传文档复用 `ResourceService.upload` 并保存 `resourceId`。适用于理解资源模块如何支撑 RAG 摄入。
- [DocumentUploadPreviewService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/rag/DocumentUploadPreviewService.java)
  RAG 预览上传使用 `DOCUMENT_PREVIEW`，提交时提升为 `DOCUMENT`，跳过或取消时删除临时资源。适用于理解临时资源生命周期。
- [DocumentPipeline.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-rag/src/main/java/com/aizuda/snail/ai/features/rag/pipeline/DocumentPipeline.java)
  RAG 处理文档时通过 `ResourceService.load(resourceId)` 读取原始文件。适用于理解资源模块与解析管线的运行关系。
- [UserService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/UserService.java)
  用户头像更新校验 `bizType=AVATAR` 并保存 `resourceId`。适用于理解头像资源复用边界。
- [OpenApiUserService.java](../../../../open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/service/OpenApiUserService.java)
  OpenAPI 外部头像以 `storageType=EXTERNAL` 直接写入资源元数据。适用于理解外部 URL 不走 `/files/**` 代理。

## 智慧（社区）

- 当前主题暂不引入外部社区材料；以本工作区源码、数据库脚本和相邻教学主题作为主要反馈来源。

## 空白

- 未检索 Snail AI Issue、PR 或部署案例。若后续要评估公开文件 URL 的安全策略，应补充真实生产配置、网关鉴权或对象存储权限讨论。
- L3 `resource-api.html` 已覆盖 Maven 坐标与领域 API；断点续传、文件大小限制、病毒扫描、CDN 缓存和前端资源选择体验留给后续专题。
