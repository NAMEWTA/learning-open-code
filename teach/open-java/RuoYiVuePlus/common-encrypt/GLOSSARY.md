# ruoyi-common-encrypt 数据加解密模块 Glossary

记录学习者在 8 节课程中**真正理解**的核心术语。覆盖双通道架构、算法体系、拦截器、上下文工厂、配置五大块。

## Terms

**双通道架构**：
本模块最核心的设计理念。API 加密通道在 Controller 层拦截请求/响应进行加解密（基于 Servlet Filter + Wrapper）；DB 字段加密通道在 MyBatis 层拦截 SQL 入参/出参进行加解密（基于 MyBatis Interceptor）。两条通道独立配置、独立开关，可在同一个项目中按需组合使用。
_Avoid_: 「两种加密方式」（两者是不同层次的拦截，不可混用）。

**IEncryptor（加密器接口）**：
本模块加密算法的顶层抽象。定义三个方法：`algorithm()` 返回算法类型、`encrypt(value, encodeType)` 加密并指定编码格式、`decrypt(value)` 解密（自动识别 Base64/Hex 编码）。
_Avoid_: 「加密算法」（接口是行为约定，算法是具体实现）。

**AbstractEncryptor（加密器基类）**：
所有加密算法实现类的抽象基类，实现 `IEncryptor` 接口。构造函数接收 `EncryptContext`，做配置校验与注入。AES、RSA、SM2、SM4、Base64 五种加密器均继承它。

**AlgorithmType（算法类型枚举）**：
枚举 5 种算法并绑定对应的加密器实现类。`DEFAULT(null)` 表示走 yml 默认配置，`BASE64(Base64Encryptor.class)` 等直接引用加密器类。`EncryptorManager` 通过 `clazz` 字段反射实例化加密器。

**EncryptContext（加密上下文）**：
加密参数的载体（DTO），包含 `algorithm`、`password`、`publicKey`、`privateKey`、`encode` 五个字段。它在 `EncryptContextFactory` → `EncryptorManager` → `IEncryptor` 之间流转，是加密器工厂的「材料清单」。

**EncryptContextFactory（加密上下文工厂）**：
从 `@EncryptField` 注解的字段 + `EncryptorProperties` 默认配置合成 `EncryptContext`。核心逻辑是「注解值优先、默认值兜底」：当注解属性为 `DEFAULT` 或空字符串时，回退到 yml 全局配置。使得单个字段可以覆盖全局算法/密钥。

**EncryptorManager（加密管理器）**：
模块的加解密调度中心。维护两级缓存：`encryptorMap` 按 `(算法, 编码, password, publicKey, privateKey)` 缓存加密器实例；`fieldCache` 按 Class 缓存 `@EncryptField` 字段集合。加密时先加 `ENCRYPT_HEADER` 前缀标记，解密时先检查前缀再去除解密——利用前缀防止同一字段被重复加密。
_Avoid_: 「加密工具类」（它有状态、有缓存，是管理类而非纯工具）。

**EncryptedFieldProcessor（加密字段处理器）**：
DB 字段加解密的核心执行者。`encrypt(sourceObject)` 递归遍历对象的 `@EncryptField` 字段并用加密器替换值，返回 `FieldSnapshot` 列表；`decrypt(sourceObject)` 同样递归遍历并还原。支持对象嵌套、集合、Map 的递归处理，用 `IdentityHashMap` 做循环引用检测。

**FieldSnapshot（字段快照）**：
`EncryptedFieldProcessor.encrypt()` 的返回值。记录字段的原始值（`target` + `field` + `value`），`restore()` 方法恢复原始值。`MybatisEncryptInterceptor` 在 SQL 执行后批量调用 `restore()` 保证业务代码中对象字段不变——即入参加密只对 SQL 生效，业务对象不受污染。

**ENCRYPT_HEADER（加密标记前缀）**：
一个常量字符串前缀（定义在 `ruoyi-common-core` 的 `Constants` 中）。`EncryptorManager.encrypt()` 在加密结果前拼接此前缀、`decrypt()` 先 `startsWith` 检查前缀再去除解密。作用：标记「这个值已经被加密了」，防止对已加密值重复加密（如多次 save 场景）。

**@ApiEncrypt（API 加密注解）**：
标记在 Controller 方法上的注解。只有一个属性 `response()`：默认 `false`（只解密请求），设为 `true` 时同时加密响应。由 `CryptoFilter` 读出，控制请求是否需解密、响应是否需加密。

**@EncryptField（字段加密注解）**：
标记在实体类 String 字段上的注解。五个属性：`algorithm`（算法，默认走全局）、`password`（AES/SM4 密钥）、`publicKey`（RSA/SM2 公钥）、`privateKey`（RSA/SM2 私钥）、`encode`（编码格式，默认走全局）。`@Inherited` 使其可在继承链上生效。

**EncodeType（编码类型枚举）**：
加密后字节数据的编码方式。`BASE64`（Base64 字符串）、`HEX`（十六进制字符串）、`DEFAULT`（走 yml 全局配置）。对 `Base64Encryptor` 不生效（其加密结果本身已是 Base64 编码文本）。

**CryptoFilter（加解密过滤器）**：
API 加解密通道的入口，实现 `Servlet Filter`。拦截所有请求，对 POST/PUT 请求检查请求头中的加密密钥（`encrypt-key`）做请求体解密，对 `@ApiEncrypt(response=true)` 的方法做响应体加密。加密时的密钥协商：客户端用 RSA 公钥加密随机 AES 密钥 → 服务端 RSA 私钥解密得 AES 密钥 → 用 AES 加解密业务报文。

**DecryptRequestBodyWrapper（解密请求体包装器）**：
`HttpServletRequestWrapper` 子类。构造时从请求头取 RSA 加密的 AES 密钥 → RSA 私钥解密 → Base64 解码得 AES 密钥明文 → 读取原始请求体 → AES 解密得 JSON 明文。将解密后的 `body` 字节缓存为可重复读的 `ByteArrayInputStream`。

**EncryptResponseBodyWrapper（加密响应体包装器）**：
`HttpServletResponseWrapper` 子类。用 `ByteArrayOutputStream` 拦截并缓存响应内容。`getEncryptContent()` 方法：生成 24 字节随机 AES 密钥 → Base64 编码 → RSA 公钥加密 → 放响应头；业务响应内容 AES 加密 → 设置 `Content-Length`。前端从响应头取加密的 AES 密钥，解密后解业务内容。

**MybatisEncryptInterceptor（MyBatis 入参加密拦截器）**：
MyBatis Plugin，拦截 `ParameterHandler.setParameters(PreparedStatement)`。在 SQL 执行前，通过 `EncryptedFieldProcessor.encrypt()` 将 `@EncryptField` 字段值替换为密文，`invocation.proceed()` 执行后通过 `FieldSnapshot.restore()` 恢复原值。实现「加密只对 SQL 生效，业务对象不受影响」。

**MybatisDecryptInterceptor（MyBatis 出参解密拦截器）**：
MyBatis Plugin，拦截 `ResultSetHandler.handleResultSets(Statement)`。在 SQL 查询后，通过 `EncryptedFieldProcessor.decrypt()` 将查询结果中的密文字段还原为明文。对 `null` 结果直接返回不处理。

**EncryptUtils（加解密工具类）**：
纯静态工具类，封装 Hutool `SecureUtil` 和 `SmUtil` 的加解密操作。AES 要求密钥 16/24/32 位，SM4 要求 16 位。RSA 和 SM2 提供密钥生成（`generateRsaKey()` / `generateSm2Key()`）。RSA 操作前校验密钥格式和最小 1024 位安全要求。额外提供 MD5、SHA256、SM3 哈希方法。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。
