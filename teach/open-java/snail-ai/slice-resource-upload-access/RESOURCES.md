# 资源上传和访问资源

## 知识

- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/ResourceController.java`
  Admin 资源上传、删除、分页入口。适用于确认 API 边界和登录注解。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/service/resource/ResourceAdminService.java`
  管理端默认 `bizType`、当前用户、分页过滤、删除授权和响应对象组装。适用于追踪 Admin 入口如何调用资源能力。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/ResourceService.java`
  上传、读取、删除、按 `storageKey` 查询和 `bizType` 调整的核心服务。适用于理解资源模块的主闭环。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/ResourceStorageService.java`
  存储策略接口。适用于确认 `store/load/delete/getAccessUrl/exists` 的稳定契约。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/ResourceStorageFactory.java`
  根据配置选择默认存储，按资源行中的 `storageType` 回放对应策略。适用于定位后端切换问题。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/LocalResourceStorageService.java`
  本地文件存储、路径归一化、路径穿越防护和 `/files/` URL 生成。适用于排查本地文件访问。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/strategy/MinioResourceStorageService.java`
  MinIO 对象写入、读取、删除、bucket 初始化和 `/files/` URL 生成。适用于排查 MinIO 配置与对象访问。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/config/ResourceConfig.java`
  `snail-ai.resource.*` 默认配置。适用于确认当前使用 `LOCAL` 还是 `MINIO`。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/util/StorageKeyGenerator.java`
  `storageKey` 格式、`bizType` 清理、日期路径和 UUID 文件名。适用于解释访问凭证和路径结构。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/util/MimeTypeUtils.java`
  MIME 类型按扩展名检测。适用于解释访问响应的 `Content-Type`。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/enums/ResourceBizTypeEnum.java`
  `GENERAL`、`AVATAR`、`ATTACHMENT`、`DOCUMENT`、`DOCUMENT_PREVIEW` 业务类型。适用于判断资源归属。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-features/snail-ai-feature-resource/src/main/java/com/aizuda/snail/ai/features/resource/enums/ResourceStorageTypeEnum.java`
  `LOCAL`、`MINIO`、`EXTERNAL` 存储类型。适用于区分代理读取和外部 URL。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/resource/po/ResourcePO.java`
  `sai_resource` 持久化对象字段。适用于把服务链路映射到数据库。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-persistence/snail-ai-biz-storage/snail-ai-biz-template/src/main/java/com/aizuda/snail/ai/persistence/resource/mapper/ResourceMapper.java`
  资源表 MyBatis-Plus mapper。适用于确认基础 CRUD 来源。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/controller/FileAccessController.java`
  `/files/**` 公开访问入口、`storageKey` 校验、代理存储限制、响应头和下载参数。适用于排查 URL 访问失败。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/interceptor/SnailJobWebMvcConfigurerAdapter.java`
  认证拦截器排除 `/files/**` 的事实来源。适用于确认公开访问边界。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-admin/src/main/java/com/aizuda/snail/ai/admin/interceptor/AuthenticationInterceptor.java`
  `@LoginRequired` 的角色检查、token 解析和用户会话写入。适用于确认 Admin 资源接口权限。
- `open-java/snail-ai/snail-ai-server/snail-ai-server-openapi/src/main/java/com/aizuda/snail/ai/openapi/service/OpenApiUserService.java`
  外部头像资源创建 `EXTERNAL` 记录。适用于理解外部 URL 不走 `/files/**` 的边界。
- `open-java/snail-ai/docs/sql/snail_ai_schema.sql`
  `sai_resource` 表结构、唯一索引和业务索引。适用于核对字段和数据库约束。
- `teach/open-java/snail-ai/module-resource/lessons/0001-resource-module-tour.html`
  L1 资源模块导览。适用于回看资源模块的总体位置。
- `teach/open-java/snail-ai/module-persistence/reference/persistence-overview.html`
  L1 持久化与存储适配参考。适用于区分业务库记录和文件或对象存储。
- `teach/open-java/snail-ai/slice-rag-ingestion/reference/rag-ingestion-flow-map.html`
  L2 RAG 摄入切片。适用于对照 `DOCUMENT` 与 `DOCUMENT_PREVIEW` 资源在 RAG 中的用途。

## 智慧（社区）

- 本主题本次只依赖仓库源码和已生成 L1/L2 教学主题，没有引入外部社区链接。后续若要做生产排障，可把部署配置、Nginx 代理规则、对象存储 bucket 策略和真实 404 日志作为学习记录补充。

## 空白

- 暂未覆盖前端上传控件、反向代理配置和浏览器缓存策略，因为本主题聚焦 Server 端资源上传与访问链路。
- 暂未覆盖生产级私有文件鉴权、签名 URL、对象存储直传和 CDN 分发，因为当前源码主路径是 `/files/**` 公开代理访问。
