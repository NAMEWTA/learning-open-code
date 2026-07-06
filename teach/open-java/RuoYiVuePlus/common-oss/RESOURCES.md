# ruoyi-common-oss 对象存储模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（含 AWS SDK S3 v2 依赖）。以下外部资源用于补充 AWS SDK 原理与 S3 协议约定。

## Knowledge

- [官方文档: _AWS SDK for Java 2.x Developer Guide_ — AWS](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html)
  本模块底层依赖的 SDK 权威说明。理解 `S3AsyncClient` / `S3TransferManager` / `S3Presigner` / `AsyncRequestBody` / `AsyncResponseTransformer` 的用法和参数时查阅。第 2、4 课的核心原理来源。

- [代码: _ruoyi-common-oss 模块全部 18 个 Java 文件_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-oss/src/main/java/org/dromara/common/oss/)
  `OssClient` 接口 / `AbstractOssClientImpl` 抽象基类 / `DefaultOssClientImpl` 实现 / `OssFactory` 工厂 / `BucketUrlUtil` 工具类 等。任何关于「这个模块做了什么」的问题，最终答案在这些文件里。

- [官方文档: _AWS S3 API Reference — Virtual Hosted-Style vs Path-Style_](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html)
  理解 `BucketUrlUtil` 中 path-style（`host/bucket`）与 site-style（`bucket.host`）两种 URL 格式的区别，以及 `resolvePathStyleAccess` 方法为何要检测 `aliyun/qcloud/qiniu/obs` 关键词。

- [代码: _OssClientConfig 配置转换链_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-oss/src/main/java/org/dromara/common/oss/config/OssClientConfig.java)
  `formProperties(OssProperties)` 静态工厂方法，展示如何将外部 JSON 配置（`OssProperties`）转换为内部强类型配置（`OssClientConfig`），涉及 region 解析、path-style 自动推断、accessPolicy 转换等逻辑。

- [代码: _OSS 业务层使用现场_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/controller/)
  `SysOssController` 的上传下载接口；业务层如何通过 `OssFactory.instance()` 获取客户端，调用 `upload()` / `download()` / `presignGetUrl()` 等方法完成存储操作。

- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li](https://plus-doc.dromara.org/)
  本项目设计说明，含文件管理、OSS 配置等章节。理解模块在整体架构中的位置时查阅。

- [Java 标准库: _CompletableFuture_ — Oracle](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/CompletableFuture.html)
  理解 `doCustomUpload` 中 `.completionFuture().handleAsync(func).join()` 的链式调用模式，以及 `HandleAsyncResult` 与 `BiFunction<CompletedUpload, Throwable, T>` 的协作方式。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么 path-style 要这样判断」「某个 OSS 厂商 403 怎么排查」时，Issues 与讨论区最贴近维护者意图。

- [社区: _AWS SDK for Java 2.x GitHub Issues_](https://github.com/aws/aws-sdk-java-v2/issues)
  AWS SDK 本身的行为问题（如 `NettyNioAsyncHttpClient` 的连接池配置、`ChecksumValidatingPublisher` 的行为变化等）在这里追踪。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + AWS SDK 公开 API + 上述官方文档支撑。
- 若学习者需接入非 S3 兼容的国内对象存储（如 ucloud、coding-net 等非标准实现），需额外查阅对应厂商的 S3 兼容性说明。
