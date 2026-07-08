# 使命：资源上传和访问

## 为什么
学习者需要能从 Admin 资源上传入口开始，沿着源码追到文件落盘或写入 MinIO、资源表记录、访问 URL 生成和 `/files/**` 公开读取。掌握这条切片后，才能排查“上传成功但访问 404”“头像或文档 URL 不可用”“资源删除后对象残留”“公开文件边界不清楚”等真实问题。

## 成功的样子
- 能说清 `POST /resource/upload`、`DELETE /resource/{id}`、`GET /resource/page` 分别进入哪些服务方法。
- 能画出 `ResourceController`、`ResourceAdminService`、`ResourceService`、存储策略、`ResourcePO` 和 `FileAccessController` 的完整调用路径。
- 能解释 `storageKey`、`accessUrl`、`bizType`、`storageType`、`creatorId` 在上传、分页、删除和访问中的作用。
- 能区分 `LOCAL`、`MINIO` 和 `EXTERNAL` 的读取边界，并据此定位 `/files/**` 访问失败原因。

## 约束条件
- 本主题是 L2 垂直切片，课程只保留主路径，接口清单、源码片段和排障表放到 `reference/`。
- 源项目根目录是 `open-java/snail-ai`，以当前源码为准。

## 不在范围内
- 不讲前端上传组件和页面交互。
- 不展开 RAG 文档解析、embedding、向量库写入和检索流程。
- 不设计新的签名 URL、鉴权下载或对象存储直传方案。
