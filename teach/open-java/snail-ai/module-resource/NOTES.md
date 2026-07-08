# 资源管理模块笔记

- 生成时间：2026-07-07。
- 源项目根目录：`open-java/snail-ai`。
- 当前主题遵循用户限制：只写入 `teach/open-java/snail-ai/module-resource/**`，不更新项目级索引、进度文件或源项目。
- 课程设计为 L1 模块总览，核心问题是“文件如何从上传变成业务可复用资源”，不是 RAG 分片或对象存储运维。
- 需要特别提醒学习者：`/resource/**` 和 `/files/**` 的权限边界不同；`/files/**` 使用 storageKey 作为公开访问凭证，不使用自增资源 ID。
