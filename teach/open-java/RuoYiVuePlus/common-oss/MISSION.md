# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-oss 对象存储模块

## Why
学习者要能彻底读懂 `ruoyi-common-oss` 这个公共模块：它包含 **18 个 Java 文件**，基于 AWS SDK S3 v2 构建了一套 S3 兼容的对象存储抽象——用工厂模式管理多客户端实例、用异步传输管理器实现非阻塞上传下载、用预签名 URL 生成临时访问凭证、用访问策略枚举控制 Bucket 权限。理解它，等于理解 RuoYi-Vue-Plus 如何把一个重量级云 SDK「封装」成业务层 5 行代码就能用的能力——面向接口编程、配置从 Redis 热加载、异步任务用虚拟线程执行、URL 构建兼容虚拟主机与路径风格。达到能给同事讲清「为什么 upload() 能同时支持 Path / File / InputStream / byte[] 六种入参」「配置热更新时旧客户端怎么安全关闭」「阿里云 OSS / 腾讯云 COS / 七牛云 / 华为云 OBS 切换到底改几行」，并能在此基础上自己接入一个新的 S3 兼容厂商或排查上传 403 问题的程度。重点是**读懂设计动机与真实代码执行路径**，不是读 AWS SDK 文档。

## Success looks like
- 能用一句话说清 `ruoyi-common-oss` 与 AWS SDK S3 v2 的关系，并说出模块的 7 个子包的职责分工（client / config / factory / io / model / properties / util）。
- 能画出 `OssClient` 接口 → `AbstractOssClientImpl` 抽象基类 → `DefaultOssClientImpl` 具体实现的继承链，说出「模板方法模式」在哪几个方法上体现。
- 能解释 `OssFactory.instance()` 的完整逻辑：从 Redis 取配置 key → 从 CacheUtils 取 JSON → 反序列化为 `OssProperties` → 转 `OssClientConfig` → 双重检查锁创建 `DefaultOssClientImpl` → 配置变更时自动关闭旧客户端。
- 能追踪 `upload(File)` 的完整代码路径：File → RandomAccessFile → ReadableByteChannel → AsyncRequestBody → S3TransferManager.upload() → CompletableFuture → PutObjectResult。
- 能讲清 `BucketUrlUtil` 的两种 URL 风格（path-style vs site-style/virtual-hosted）的区别、`rebuildUrlHeader` 的作用、以及 `resolvePathStyleAccess` 为什么通过检查 `aliyun/qcloud/qiniu/obs` 关键词来判断。
- 能理解异步体系：`CompletableFuture` + `handleAsync` 的写法、`OssAsyncExecutorConfig` 的虚拟线程 vs 线程池两种模式、`OutputStreamDownloadSubscriber` 如何实现 `Consumer<ByteBuffer>` 做响应式流下载、`HandleAsyncResult` 如何包装成功/失败。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在「实战」课提及前端通过预签名 URL 直接上传到 OSS 的场景。
- 目标是「读懂」而非「能基于 AWS SDK 从零写一个存储系统」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路」为主。
- 全部讲解基于仓库真实代码与 AWS SDK S3 v2 的公开 API（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- AWS SDK S3 v2 各 API 的完整文档与参数说明——只讲项目里实际调用的 API，不讲整个 SDK。
- OSS 业务层的完整 CRUD（如 `SysOssController` / `SysOssService`）——仅在与本模块配合的点上提及。
- 工作流 / 定时任务 / 消息通知中调用 OSS 存储的业务编排细节。
- 前端直传 OSS 的完整签名流程——仅提及 `presignPutUrl` 的用途。
