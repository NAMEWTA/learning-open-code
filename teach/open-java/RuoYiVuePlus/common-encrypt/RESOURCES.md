# ruoyi-common-encrypt 数据加解密模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**（`RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-encrypt/`）。以下外部资源用于补充算法原理与框架约定。

## Knowledge

- [官方文档: _Hutool 加密解密工具_ — Hutool（hutool.cn）](https://www.hutool.cn/docs/#/crypto/%E6%A6%82%E8%BF%B0)
  本模块的底层加密实现。`EncryptUtils` 中 AES/RSA 操作使用 `SecureUtil`，SM2/SM4 操作使用 `SmUtil`。理解对称加密/非对称加密/国密算法在本模块中的具体调用方式时查阅。
- [官方文档: _MyBatis Plugin（拦截器）机制_ — MyBatis（mybatis.org）](https://mybatis.org/mybatis-3/configuration.html#plugins)
  理解 `MybatisEncryptInterceptor` 和 `MybatisDecryptInterceptor` 如何通过 `@Intercepts` + `@Signature` 拦截 `ParameterHandler.setParameters` 和 `ResultSetHandler.handleResultSets`，以及 `Plugin.wrap(target, this)` 的代理机制。
- [官方文档: _Servlet Filter 机制_ — Jakarta EE（jakarta.ee）](https://jakarta.ee/specifications/servlet/)
  理解 `CryptoFilter` 作为 Servlet Filter 在请求进入 Controller 前拦截的机制，以及 `HttpServletRequestWrapper` / `HttpServletResponseWrapper` 如何实现请求体和响应体的透明替换。
- [官方文档: _RuoYi-Vue-Plus 官方文档 · 数据安全_ — Lion Li（plus-doc.dromara.org）](https://plus-doc.dromara.org/)
  本项目对 API 加密和数据库字段加密的设计说明与使用示例。理解「为什么分两套配置」「业务里怎么用注解」时查阅。
- [官方文档: _Spring Boot AutoConfiguration_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `ApiDecryptAutoConfiguration` 和 `EncryptorAutoConfiguration` 如何通过 `@AutoConfiguration` + `@ConditionalOnProperty` 实现条件装配，以及 `@EnableConfigurationProperties` 如何绑定 `api-decrypt.xxx` / `mybatis-encryptor.xxx` 配置。
- [代码: _annotation / config / core / enums / filter / interceptor / properties / utils 八大目录_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-encrypt/src/main/java/org/dromara/common/encrypt/)
  模块第一现场。任何「这个能力到底怎么实现」的问题，最终答案在这里。
- [官方文档: _Bouncy Castle Crypto Package_ — Bouncy Castle（bouncycastle.org）](https://www.bouncycastle.org/documentation/)
  SM2/SM4 国密算法的底层实现库。Hutool 的 `SmUtil` 内部调用 Bouncy Castle，理解 SM2 椭圆曲线参数和 SM4 分组密码时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样设计」「某版本行为变化」时，Issues 和讨论区是最贴近维护者意图的反馈源。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。
