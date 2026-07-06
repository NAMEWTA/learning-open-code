# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-mqtt MQTT 客户端模块

## Why
学习者要能彻底读懂 `ruoyi-common-mqtt` 这个公共模块：它本身只有三个类，是对开源 MQTT 客户端框架 **Mica MQTT** 的一层「项目化适配」。理解它，等于理解 RuoYi-Vue-Plus 如何把 MQTT 协议引入微服务体系——用 Spring Boot 自动配置实现零代码接入、用虚拟线程优化 IO 性能、用生命周期监听器统一管理连接状态与消息处理。达到能给同事讲清「这个模块为什么只有三个类却支撑起设备通信」「MQTT 发布订阅模型与本模块的对应关系」，并能在此基础上自己搭建一个 MQTT 消息收发场景或排查断连/丢消息问题的程度。重点是**读懂 MQTT 协议核心概念与本模块设计动机**，不是从零实现一个 MQTT Broker。

## Success looks like
- 能用一句话说清 `ruoyi-common-mqtt` 与 Mica MQTT 的关系，并说出模块仅有的三个类各自承担什么职责。
- 能画出 MQTT 发布订阅模型的拓扑图（Broker / Publisher / Subscriber / Topic），并对照本模块说明它作为 MQTT Client 的角色。
- 能解释 `MqttAutoConfiguration` 如何通过 `@AutoConfiguration` + `@ConditionalOnProperty` + `AutoConfiguration.imports` 实现「依赖即生效、配置开关控制」的无侵入接入。
- 能讲清 `MqttClientCustomizer` Bean 为什么要用虚拟线程（Virtual Thread）替换 Mica MQTT 默认的线程池，以及它对高并发消息处理的性能意义。
- 能讲清两个监听器各自的责任边界：`MqttClientConnectListener` 管理连接生命周期（连接/断连/重连），`MqttClientGlobalMessageListener` 处理全局消息订阅，并说出它们分别实现的 Mica MQTT 接口。
- 能对照 `application.yml` 中 `mqtt.client` 配置段说出每个关键参数的含义（`client-id` / `keep-alive-secs` / `session-expiry-interval-secs` / `version`），并理解 MQTT 5 相对于 3.1.1 的改进。
- 能基于本模块编写一个简单的 MQTT 消息发布与订阅的实战代码片段，并说出 Topic 命名最佳实践。

## Constraints
- 学习者是全栈背景，本模块为纯后端 Java，讲解聚焦后端，但会在第 1 课介绍 MQTT 协议时联系前端/物联网设备的使用场景（点到为止）。
- 目标是「读懂」而非「能改造 MQTT Broker」——课程以追踪本仓库真实代码、解释设计动机为主，练习以「读代码答问题 / 复述链路 / 编写简单片段」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与类名。
- 交互语言：简体中文。

## Out of scope
- Mica MQTT 框架的完整 API 与底层 TCP 通信实现细节——仅讲本模块用到的接口与机制。
- MQTT Broker（如 EMQX、Mosquitto）的搭建、运维与集群部署——仅在本模块需要连接 Broker 时提到。
- 物联网设备端（如 ESP32、树莓派）的 MQTT 客户端编程——仅在第 1 课协议介绍时作为场景引出。
- RuoYi 业务模块中如何具体使用 MQTT 收发消息——仅在第 3 课实战环节给示例代码，不展开完整业务。
- MQTT 5 协议的全部新特性细节（如会话过期、主题别名、流控等）——仅讲本模块配置中涉及的版本选择与参数含义。
