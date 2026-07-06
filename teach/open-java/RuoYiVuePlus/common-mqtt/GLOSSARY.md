# ruoyi-common-mqtt MQTT 客户端模块 Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**MQTT**：
Message Queuing Telemetry Transport（消息队列遥测传输）的缩写。由 IBM 开发的轻量级发布订阅消息协议，基于 TCP/IP，专为低带宽、高延迟、不可靠网络环境下的物联网设备通信设计。OASIS 标准，当前最新版本为 5.0（本模块支持 mqtt_3_1 / mqtt_3_1_1 / mqtt_5）。
_Avoid_: 「消息队列」（MQTT 本质是发布订阅协议，不是 RabbitMQ/Kafka 那样的消息队列中间件）。

**Mica MQTT**：
Dromara 社区出品的开源 MQTT 客户端/服务端框架（本项目使用其 `mica-mqtt-client-spring-boot-starter`）。基于 t-io 网络框架，提供 MQTT 3.x 和 5.0 协议的完整 Java 实现。`ruoyi-common-mqtt` 的全部 MQTT 通信能力来自它。
_Avoid_: 「MQTT Broker」（Mica MQTT 既可以做客户端也可以做服务端，本模块只做客户端）。

**发布订阅模型（Pub/Sub）**：
MQTT 的核心通信模式。消息发送者（Publisher）不直接发消息给接收者（Subscriber），而是发布到 Broker 上的某个主题（Topic）；订阅者向 Broker 订阅自己感兴趣的主题后，Broker 负责将消息路由给所有匹配的订阅者。这种「空间解耦」使得发送者和接收者互不知晓对方的存在。
_Avoid_: 「点对点通信」（和 RabbitMQ 的 queue 模型不同，MQTT 是主题广播模型）。

**Broker**：
MQTT 的中央消息代理服务器（如 EMQX、Mosquitto、HiveMQ）。负责接收所有发布者的消息、维护订阅关系、将消息路由到匹配的订阅者。本模块作为 MQTT Client 连接到 Broker，既是消息的发布者也是订阅者。
_Avoid_: 「服务端」（Broker 是 MQTT 体系内对消息代理服务器的专有称呼）。

**Topic**：
MQTT 中消息的分类标签，是一个 UTF-8 字符串，用 `/` 分层（如 `sensor/temperature/room1`）。订阅者可使用通配符：单层 `+`（如 `sensor/+/room1`）和多层 `#`（如 `sensor/#`）。Topic 不需要预先创建，发布时自动创建。
_Avoid_: 「消息队列名」（Topic 是路由标签而非队列）。

**QoS（Quality of Service）**：
MQTT 消息交付质量保证级别，分为三级：QoS 0（至多一次，发完即忘）、QoS 1（至少一次，确认送达）、QoS 2（恰好一次，四步握手确认）。级别越高，可靠性越强，开销也越大。本模块的 `MqttClientGlobalMessageListener` 默认处理所有 QoS 级别的消息。
_Avoid_: 「可靠传输」（QoS 有精确的三个级别定义，不是简单的"可靠/不可靠"）。

**MqttClientCreator**：
Mica MQTT 的客户端创建器接口（`org.dromara.mica.mqtt.core.client.MqttClientCreator`），负责配置并创建 MQTT 客户端实例。通过链式调用设置连接参数（`ip`/`port`/`clientId`/`username`/`password`/`version` 等）和回调监听器。由 Mica MQTT 的自动配置创建后注入 Spring 容器，本模块通过 `MqttClientCustomizer` 对其进行定制。
_Avoid_: 「MQTT 客户端」（Creator 是构建器/工厂，不是客户端实例本身）。

**虚拟线程（Virtual Thread）**：
Java 21 引入的轻量级线程（Project Loom），由 JVM 而非操作系统管理，创建开销极低（数百字节 vs 传统线程的 MB 级），阻塞时自动挂起并释放底层平台线程。本模块在 `MqttClientCustomizer` 中使用 `VirtualThreadTaskExecutor` 替换 Mica MQTT 默认的普通线程池，使大量并发 MQTT 连接/消息处理不再受 OS 线程数限制。
_Avoid_: 「协程」（Java 虚拟线程是 JVM 管理的轻量级线程，实现机制与 Go goroutine 等协程不同）。

**MqttAutoConfiguration**：
MQTT 模块的 Spring Boot 自动配置类（`config/MqttAutoConfiguration.java`）。用 `@AutoConfiguration` 声明为自动配置类，用 `@ConditionalOnProperty(value="mqtt.client.enabled", havingValue="true")` 控制开关，用 `@Bean` 注册两个监听器和 `MqttClientCustomizer`。通过 `AutoConfiguration.imports` 文件被 Spring Boot 发现。
_Avoid_: 「MQTT 配置」（它不只是配置，是模块的装配入口和全部 Bean 定义来源）。

**IMqttClientConnectListener**：
Mica MQTT 的连接生命周期监听器接口（`org.dromara.mica.mqtt.core.client.IMqttClientConnectListener`）。声明两个回调：`onConnected(ChannelContext, boolean isReconnect)` — 连接成功时触发（含首次连接和断线重连）；`onDisconnect(ChannelContext, Throwable, String, boolean isRemove)` — 断开连接时触发。本模块通过 `MqttClientConnectListener` 实现该接口，在回调中记录日志并可在 `onDisconnect` 中动态更新 `clientId`/`username`/`password` 以支持凭证轮换。
_Avoid_: 「连接事件监听器」（该接口不仅监听事件，断连回调中还可修改重连参数）。

**IMqttClientGlobalMessageListener**：
Mica MQTT 的全局消息监听器接口（`org.dromara.mica.mqtt.core.client.IMqttClientGlobalMessageListener`）。声明一个回调：`onMessage(ChannelContext context, String topic, MqttPublishMessage message, byte[] payload)`。当客户端收到任何已订阅主题的消息时触发，是所有 Topic 消息的统一入口。本模块通过 `MqttClientGlobalMessageListener` 实现该接口，将消息 topic 和 payload（UTF-8 解码）记入日志。
_Avoid_: 「消息处理器」（它是全局监听器，一个客户端只有一个，不是按 Topic 分散的多个处理器）。

**client-id**：
MQTT 协议要求的客户端唯一标识符，在 `mqtt.client.client-id` 中配置。Broker 用它将消息路由到正确的持久会话（Persistent Session）。同一 Broker 上不可有两个相同 client-id 的连接同时在线。物联网场景中通常使用设备 SN 号，项目中配置为固定字符串 `000001`。
_Avoid_: 「客户端名称」（`mqtt.client.name` 是 Mica MQTT 层面的客户端名称，`client-id` 是 MQTT 协议层面的唯一标识，两者不同）。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。
