# ruoyi-common-oss 对象存储模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**S3 兼容协议**：
Amazon S3 定义的 RESTful 对象存储协议。因其简洁和广泛支持，成为云对象存储的事实标准。阿里云 OSS、腾讯云 COS、七牛云 Kodo、华为云 OBS、MinIO 等服务均提供了 S3 兼容 API。`ruoyi-common-oss` 基于 AWS SDK S3 v2（Java），通过 S3 协议与各厂商通信，不直接依赖任一厂商的专有 SDK。
_Avoid_: 「S3 专指 AWS S3」（在本文档语境中，"S3" 指协议，具体厂商用全称）。

**OssClient**：
本模块的核心接口（`org.dromara.common.oss.client.OssClient`），定义了对象存储的全部操作契约：`upload()` / `download()` / `delete()` / `presignGetUrl()` / `presignPutUrl()`。每个方法提供带 `bucket` 前缀和不带前缀两组重载，前者显式指定 Bucket，后者使用配置中的默认 Bucket。接口继承 `AutoCloseable`，支持资源安全关闭。
_Avoid_: 「OSS 客户端」（容易与各厂商 SDK 的 Client 混淆，本接口是抽象层）。

**AbstractOssClientImpl**：
`OssClient` 的抽象基类（模板方法模式），提供了 70+ 个方法的完整实现——所有上传重载最终汇聚到 `bucketUpload(bucket, key, AsyncRequestBody, Options)` 私有方法，所有下载重载汇聚到 `doCustomDownload(...)`。子类只需实现 `doInitialize()` 一个抽象方法（创建具体的 `S3AsyncClient` / `S3TransferManager` / `S3Presigner`）。
_Avoid_: 「抽象客户端基类」（太泛，本处专指 OSS 模块的模板方法实现）。

**DefaultOssClientImpl**：
`AbstractOssClientImpl` 的唯一子类（`org.dromara.common.oss.client.DefaultOssClientImpl`），重写 `doInitialize()` 完成 AWS SDK 三大组件的创建：`S3AsyncClient`（底层异步 HTTP 客户端，用 Netty NIO）、`S3TransferManager`（高级传输管理器，封装分段上传/下载/重试）、`S3Presigner`（预签名 URL 生成器）。还负责创建 `asyncExecutor`（虚拟线程或固定线程池）。
_Avoid_: 「默认实现」（在本文档中指具体创建 AWS SDK 客户端的那个类）。

**OssFactory**：
OSS 客户端的工厂与缓存管理器（`org.dromara.common.oss.factory.OssFactory`）。所有方法为静态方法。核心流程：`instance()` → 从 Redis 取默认配置 key → `instance(configKey)` → 从 CacheUtils 取 JSON → 解析为 `OssProperties` → 转为 `OssClientConfig` → 双重检查锁创建/复用 `DefaultOssClientImpl`。配置变更时自动关闭旧客户端并创建新实例。用 `ConcurrentHashMap` 缓存 + 每 key 独立 `ReentrantLock` 保证线程安全。
_Avoid_: 「OSS 工厂类」（它就是，但强调它的缓存、配置热更新、安全关闭能力）。

**OssProperties**：
外部配置 POJO（`org.dromara.common.oss.properties.OssProperties`），字段与数据库中存储的 JSON 对应：`endpoint` / `domainUrl` / `prefix` / `accessKey` / `secretKey` / `bucketName` / `region` / `isHttps` / `accessPolicy`。通过 `OssClientConfig.formProperties()` 转换为内部强类型配置。配置源头是数据库的 `sys_oss_config` 表，经 `CacheUtils` 缓存到 Redis。
_Avoid_: 「OSS 配置类」（与 `OssClientConfig` 区分：一个是页面可编辑的 POJO，一个是内部不可变配置对象）。

**OssClientConfig**：
内部不可变配置对象（`org.dromara.common.oss.config.OssClientConfig`），实现 `Config<T,B>` 接口，提供 `copy()` 和 `toBuilder()` 方法。封装了 `endpoint` / `domain` / `accessKey` / `secretKey` / `bucket` / `region` / `prefix` / `useHttps` / `usePathStyleAccess`，并包含 `getEndpointUrl()` / `getDomainUrl()` / `getBucketUrl()` 等 URL 计算方法。配置变更检测（`verifyConfig`）依赖其 `equals/hashCode`。
_Avoid_: 「OSS 配置」（太泛，此处特指 `OssClientConfig` 类）。

**OssAsyncExecutorConfig**：
异步执行器配置 record（`org.dromara.common.oss.config.OssAsyncExecutorConfig`）。两个字段：`enabledVirtualThread`（是否用虚拟线程）和 `corePoolSize`（线程池大小，默认 CPU 核数）。`DefaultOssClientImpl.doInitialize()` 根据此配置决定创建 `newVirtualThreadPerTaskExecutor()` 还是 `newScheduledThreadPool(corePoolSize)`。
_Avoid_: 「线程池配置」（专指 OSS 模块的上传/下载异步回调执行器）。

**BucketUrlUtil**：
Bucket URL 构建工具类（`org.dromara.common.oss.util.BucketUrlUtil`）。核心能力：`rebuildUrlHeader(isHttps, base)` 重设协议头；`getPathStyleBucketUrl()` 生成 `{protocol}://{base}/{bucket}`；`getSiteStyleBucketUrl()` 生成 `{protocol}://{bucket}.{base}`。还负责 `removeHttpProtocolHeader()` 去除已有协议头。
_Avoid_: 「URL 工具类」（专指 OSS Bucket URL 构建）。

**AccessPolicy**：
访问策略枚举（`org.dromara.common.oss.enums.AccessPolicy`）。三个值：`PRIVATE(0, BucketCannedACL.PRIVATE, ObjectCannedACL.PRIVATE)` — 私有访问；`PUBLIC_READ_WRITE(1, ...)` — 公开读写；`PUBLIC_READ(2, ...)` — 公开读。每个枚举值携带对应的 AWS SDK `BucketCannedACL` 和 `ObjectCannedACL`，通过 `formType(String)` 从字符串解析。
_Avoid_: 「访问控制」（太泛，本处指 S3 Bucket 的预制访问策略）。

**AccessControlPolicyConfig**：
访问策略配置 record（`org.dromara.common.oss.config.AccessControlPolicyConfig`）。两个字段：`enabled`（是否启用 ACL）和 `accessPolicy`（策略类型）。默认实例 `DEFAULT` 为 `enabled=false, accessPolicy=PUBLIC_READ_WRITE`。通过 `OssClientConfig.resolveAccessControlPolicy()` 从 `OssProperties.accessPolicy` 字符串构建。
_Avoid_: 「ACL 配置」（和 `AccessPolicy` 区分：这是开关+策略的组合 record）。

**S3StorageException**：
本模块的统一运行时异常（`org.dromara.common.oss.exception.S3StorageException`），继承 `RuntimeException`。提供 4 个构造器和 4 个静态工厂方法 `form(...)`。`AbstractOssClientImpl` 中所有 CompletableFuture 的异常、初始化失败、参数校验失败都经 `toStorageException()` 转换为此异常。
_Avoid_: 「OSS 异常」（只指 `S3StorageException` 这个类）。

**HandleAsyncResult**：
异步操作的结果包装 record（`org.dromara.common.oss.model.HandleAsyncResult<T>`）。两个字段：`result: T` 和 `error: Throwable`。提供 `isSuccess()` / `isFailure()` / `getResult()` / `getError()` 方法，以及 `of()` / `success()` / `failure()` 静态工厂。用于 `doCustomUpload` 返回可同时检查成功值和错误信息的单一对象。
_Avoid_: 「异步结果」（专指本模块的泛型 record）。

**OutputStreamDownloadSubscriber**：
响应式下载订阅器（`org.dromara.common.oss.io.OutputStreamDownloadSubscriber`），实现 `Consumer<ByteBuffer>` 和 `AutoCloseable`。在异步下载中作为数据消费者：`accept(ByteBuffer)` 方法循环将 ByteBuffer 写入内部 `WritableByteChannel`。当 target 是 `FileOutputStream` 时，优化为直接使用 `FileOutputStream.getChannel()` 而非 `Channels.newChannel()` 包装。
_Avoid_: 「下载器」（它不做 HTTP 请求，只消费 SDK 推送的字节流）。

**Path-Style / Site-Style (Virtual-Hosted Style)**：
S3 的两种 Bucket 寻址方式。Path-Style：`https://endpoint.com/bucket-name/key`（Bucket 名在 URL 路径中）。Site-Style：`https://bucket-name.endpoint.com/key`（Bucket 名在子域名中）。`BucketUrlUtil` 同时支持两种格式，`resolvePathStyleAccess()` 方法根据 endpoint 是否包含已知云厂商关键词（`aliyun/qcloud/qiniu/obs`）自动推断应该用哪种。
_Avoid_: 「路径风格」/「域名风格」（两个是互斥的，不能混用）。

## 待收录
- S3TransferManager — 课程完成后若学习者有深入理解再收录。
- CompletableFuture 模式 — 第 4 课异步体系讲完后收录。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。
