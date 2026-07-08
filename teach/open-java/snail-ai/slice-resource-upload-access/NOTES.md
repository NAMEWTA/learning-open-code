# 便签

- 用户要求本主题只写入 `teach/open-java/snail-ai/slice-resource-upload-access/**`，因此本次未更新 `teach/open-java/snail-ai/index.md`、`_progress.md` 或 `_progress.json`。
- 课程应承接已有 L1 `module-resource`、`module-persistence` 和 L2 `slice-rag-ingestion`，聚焦 Server 端资源上传、持久化、访问 URL 和权限边界。
- 关键源码事实：`/resource/*` 入口有 `@LoginRequired`；`/files/**` 被认证拦截器排除，但只接受符合 UUID 日期路径格式的 `storageKey`，且只代理 `LOCAL` 和 `MINIO`。
