# 使命：资源管理模块

## 为什么
学习者需要从源码层面理解 Snail AI 如何接收文件上传、保存资源元数据、生成可访问 URL，并让用户头像、RAG 文档等上层功能复用同一套资源底座。掌握这个模块后，排查“文件上传成功但无法访问”“RAG 文档解析不到源文件”“头像资源权限不符合预期”时，可以先定位资源链路，再决定是否深入具体业务模块。

## 成功的样子
- 能沿 `POST /resource/upload` 说清文件流如何进入存储后端、写入 `sai_resource`，再生成 `accessUrl`。
- 能区分 `ResourceController` 管理接口、`FileAccessController` 文件访问接口与 `ResourceService` 领域服务的边界。
- 能说明 `LOCAL`、`MINIO`、`EXTERNAL` 三类存储类型在访问代理上的差异。
- 能判断 RAG 文档、用户头像、OpenAPI 外部头像如何复用或绕过资源上传链路。
- 能说出 `snail-ai-feature-resource` 的 Maven 坐标、直接依赖及其与 `snail-ai-biz-template` 的持久化分工。
- 能按方法签名查阅 `ResourceService` 与 `ResourceStorageService`，并与 L2 上传访问切片中的调用阶段一一对应。

## 约束条件
- 读者具备 Java、Spring Boot、MyBatis-Plus 和 HTTP 基础，但不假设熟悉对象存储实现细节。
- L1 短课控制在 15 分钟内；模块边界与主链路见 `lessons/`，HTTP 入口与调试见 `reference/resource-overview.html`。
- L3 构建 API（Maven 坐标、依赖、领域服务与策略签名）写入 `reference/resource-api.html`，与 overview 互补、避免重复。
- 当前任务只写入 `teach/open-java/snail-ai/module-resource/`。

## 不在范围内
- 不修改 `open-java/snail-ai/**` 源码、项目级 `index.md`、`_progress.*` 或其他教学主题。
- 不深入讲解前端资源选择器、对象存储桶权限策略、CDN、断点续传或病毒扫描。
- 不把 RAG 文档分片、向量化、检索召回或 Agent 责任链作为本课主线。
