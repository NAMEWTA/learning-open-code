# 策展资源 · ruoyi-common 全模块学习

## 一手资料（高信任度）

### 框架官方文档
| 资源 | 覆盖内容 | 何时取用 |
|------|---------|---------|
| [MyBatis-Plus 官方文档](https://baomidou.com/) | BaseMapper、分页插件、自动填充、乐观锁 | 学 common-mybatis 时查 API |
| [Sa-Token 官方文档](https://sa-token.cc/doc.html) | StpLogic、JWT、权限校验、多账号 | 学 common-satoken 时 |
| [SpringDoc 官方文档](https://springdoc.org/) | OpenAPI 3.0、自定义配置 | 学 common-doc 时 |
| [Jackson 官方文档](https://github.com/FasterXML/jackson-docs) | ObjectMapper、序列化器、Module | 学 common-json 时 |
| [AWS S3 SDK 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) | S3AsyncClient、TransferManager | 学 common-oss 时 |
| [JustAuth 官方文档](https://justauth.wiki/) | 30+ 平台 OAuth2.0 集成 | 学 common-social 时 |
| [Spring AI MCP](https://docs.spring.io/spring-ai/reference/) | MCP Client/Server | 学 common-mcp 时 |
| [Easy-Es 文档](https://easy-es.cn/) | ES ORM、Lambda 查询 | 学 common-elasticsearch 时 |
| [Hutool 文档](https://hutool.cn/docs/) | 加密工具、HTTP、日期、JSON | 贯穿始终 |

### 项目级资源
| 资源 | 说明 |
|------|------|
| [RuoYi-Vue-Plus GitHub](https://github.com/dromara/RuoYi-Vue-Plus) | 项目源码、Wiki、Issue |
| [Apache Fesod Sheet](https://github.com/apache/fesod-sheet) | Excel 读写引擎（替代 EasyExcel） |
| [MyBatis-Plus-Join](https://github.com/yulichang/mybatis-plus-join) | 联表查询扩展 |
| [MapStruct-Plus](https://mapstruct.plus/) | 编译期 Bean 转换增强 |
| [ip2region](https://github.com/lionsoul2014/ip2region) | 离线 IP 地址库 |
| [BouncyCastle](https://www.bouncycastle.org/java.html) | SM2/SM4 国密算法底层实现 |
| [dynamic-datasource](https://github.com/baomidou/dynamic-datasource) | 多数据源切换框架 |

### 社区与讨论
| 社区 | 说明 |
|------|------|
| [RuoYi-Vue-Plus Gitee](https://gitee.com/dromara/RuoYi-Vue-Plus) | 国内主仓库，活跃 Issue 讨论 |
| [Dromara 社区](https://gitee.com/dromara) | 项目所属开源组织 |

## 学习路径建议

1. **先通读** ruoyi-common-core（第1-2课）→ 它是所有模块的共同语言
2. **再理解** ruoyi-common-web（第3-4课）→ 理解请求是如何被处理的
3. **然后深入** ruoyi-common-mybatis（第5-7课）→ 数据层是业务的核心
4. **安全体系** ruoyi-common-satoken/security/sensitive（第12-13课）→ 认证授权
5. **数据处理** ruoyi-common-json/encrypt/excel/translation（第8-11,18课）
6. **外部集成** 按需学习（oss/mail/sms/social/mqtt/push/mcp/es 等）
7. **收尾** ruoyi-common-bom/总结（第19课）→ 建立全局视角
