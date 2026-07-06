# Mission: 全面读懂 RuoYi-Vue-Plus 的 ruoyi-common-encrypt 数据加解密模块

## Why
学习者要能在脑中完整重建 `ruoyi-common-encrypt` 这个公共模块「提供了什么能力、每个类各管什么、为什么这样设计」的全景，理解它如何用 **双通道架构**（API 层 + 数据库层）提供透明加解密能力，支持 5 种算法（AES/RSA/SM2/SM4/Base64），并能在自己的业务代码里正确选用。重点是**读懂模块设计与各组件职责**，不是从零实现一个加密框架。讲解全部基于本仓库真实代码（已逐文件核对）。

## Success looks like
- 能用一张图讲清模块的**双通道架构**：API 加密通道（`@ApiEncrypt` → `CryptoFilter` → Wrapper 包装器）和 DB 字段加密通道（`@EncryptField` → MyBatis 拦截器对 → `EncryptedFieldProcessor` → `EncryptorManager`），并说出每条通道的关键类。
- 能解释 5 种算法的定位差异：Base64 是编码（非加密）、AES/SM4 是对称加密（一个密钥）、RSA/SM2 是非对称加密（公钥加密+私钥解密），以及 `AlgorithmType` 枚举如何通过 `clazz` 字段实现算法到加密器的映射。
- 能讲清 API 加密的完整链路：POST/PUT 请求体解密（`DecryptRequestBodyWrapper` 用 RSA 解出 AES 密钥再解 body）、响应加密（`EncryptResponseBodyWrapper` 生成随机 AES 密钥加密响应，用 RSA 加密 AES 密钥放响应头），以及 `CryptoFilter` 如何协调整个过程。
- 能讲清 DB 字段加解密：`MybatisEncryptInterceptor` 拦截 `ParameterHandler.setParameters` 在 SQL 执行前替换字段值、`MybatisDecryptInterceptor` 拦截 `ResultSetHandler.handleResultSets` 在查询后还原字段值，以及 `FieldSnapshot` 机制如何保证入参加密后不影响业务代码中的对象引用。
- 能讲清 `EncryptorManager` 的缓存机制：`encryptorMap`（按算法+密钥缓存 `IEncryptor` 实例，避免重复创建）和 `fieldCache`（按 Class 缓存 `@EncryptField` 字段集合，避免重复反射）的双重缓存设计。
- 能说清 `EncryptContext`（加密参数载体）和 `EncryptContextFactory`（从 `@EncryptField` 注解 + `EncryptorProperties` 默认配置合成 `EncryptContext`）的协作方式 —— 注解优先、默认值兜底的参数解析逻辑。
- 能说清两套配置体系：`api-decrypt`（`ApiDecryptProperties` + `ApiDecryptAutoConfiguration`，控制 API 层加解密开关）和 `mybatis-encryptor`（`EncryptorProperties` + `EncryptorAutoConfiguration`，控制 DB 层加解密开关与默认算法），以及各自的 `@ConditionalOnProperty` 条件装配。
- 能说清加密标记前缀 `ENCRYPT_HEADER` 的作用：`EncryptorManager` 在加密时给结果加前缀、解密时先检查前缀再去除解密，利用此标记防止重复加解密。
- 能从 `pom.xml` 依赖出发，说清模块依赖 `hutool-crypto`（AES/RSA）、`bouncycastle`（SM2/SM4）这两个底层加密库，以及对 `ruoyi-common-core` 的协作依赖。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解以追踪真实代码 + 解释设计动机为主。
- 目标是「读懂并能正确选用」而非「能改框架」——练习以「读代码答问题 / 选型判断 / 复述链路」为主，不要求大量动手编码。
- 全部讲解基于仓库真实代码，引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- AES/RSA/SM2/SM4 各自的密码学原理与数学细节——仅讲本模块用到的 API 层次。
- Hutool 的 `SecureUtil`、`SmUtil` 完整 API —— 只讲本模块 `EncryptUtils` 里实际调用的那部分。
- 前端的 AES 加密、RSA 公钥生成、HTTP 拦截器等——本模块是后端加解密模块，前端如何配合加密仅在链路追踪时提及。
- 非本模块的加密场景（如登录密码的 BCrypt/MD5 加密、Token 签名等）。
