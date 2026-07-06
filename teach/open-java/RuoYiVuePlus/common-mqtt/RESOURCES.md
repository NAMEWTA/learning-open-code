# ruoyi-common-mqtt MQTT 客户端模块 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充 MQTT 协议原理与 Mica MQTT 官方约定。

## Knowledge

- [官方文档: _Mica MQTT 官方文档_ — Dreamlu（dreamlu.net）](https://mica-mqtt.dreamlu.net/guide/spring/client.html)
  本模块封装的核心框架权威说明。理解 `MqttClientCreator` / `IMqttClientConnectListener` / `IMqttClientGlobalMessageListener` 接口时查阅。本模块的一切都建立在它之上。
- [代码: _ruoyi-common-mqtt 模块三件套_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-mqtt/src/main/java/org/dromara/common/mqtt/)
  `MqttAutoConfiguration` / `MqttClientConnectListener` / `MqttClientGlobalMessageListener`。任何关于「这个模块做了什么」的问题，最终答案在这三个文件里。
- [协议规范: _MQTT 5.0 官方规范_ — OASIS（docs.oasis-open.org）](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)
  理解 MQTT 5 协议特性（会话过期、原因码、用户属性、请求/响应模式等）时查阅。第 1 课协议介绍的核心参考。
- [协议规范: _MQTT 3.1.1 官方规范_ — OASIS](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html)
  MQTT 3.1.1 版本规范。与 MQTT 5 对比时参考。
- [官方文档: _Spring Boot 自动配置_ — Spring（docs.spring.io）](https://docs.spring.io/spring-boot/reference/features/developing-auto-configuration.html)
  理解 `@AutoConfiguration` / `AutoConfiguration.imports` / `@ConditionalOnProperty` / `@Bean` 机制时查阅。第 2 课的核心原理来源。
- [代码: _MQTT 配置文件_](RuoYi-Vue-Plus/ruoyi-admin/src/main/resources/application.yml)
  `mqtt.client` 配置段。理解 MQTT 客户端连接参数（`ip`/`port`/`client-id`/`keep-alive-secs`/`version` 等）的实际值及其含义时查阅。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目设计说明。理解模块在整体架构中的位置时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么用虚拟线程」「MQTT 连接断线重连策略」时，Issues 与讨论区最贴近维护者意图。Mica MQTT 与 RuoYi-Vue-Plus 同属 Dromara 生态，问题常能交叉解答。
- [资源: _MQTT Essentials 系列文章_ — HiveMQ（hivemq.com）](https://www.hivemq.com/mqtt-essentials/)
  MQTT 协议入门的最佳科普系列。涵盖发布订阅、QoS、Topic、遗嘱消息等核心概念，图文并茂。第 1 课协议介绍的补充读物。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + Mica MQTT 官方文档 + MQTT 协议规范支撑。
