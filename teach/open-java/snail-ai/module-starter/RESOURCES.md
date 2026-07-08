# 启动与配置模块资源

## 知识

- [snail-ai-starter/pom.xml](../../../../open-java/snail-ai/snail-ai-starter/pom.xml)
  starter 聚合依赖、可执行 JAR 主类、最终产物名和 Maven repackage 边界。
- [SnailAiSpringbootApplication.java](../../../../open-java/snail-ai/snail-ai-starter/src/main/java/com/aizuda/snail/ai/starter/SnailAiSpringbootApplication.java)
  Spring Boot 主入口，说明扫描范围、异步、调度和默认时区。
- [StartListener.java](../../../../open-java/snail-ai/snail-ai-starter/src/main/java/com/aizuda/snail/ai/starter/listener/StartListener.java)
  ContextRefreshedEvent 后的启动钩子，用于统一触发自定义 `Lifecycle.start()`。
- [EndListener.java](../../../../open-java/snail-ai/snail-ai-starter/src/main/java/com/aizuda/snail/ai/starter/listener/EndListener.java)
  ContextClosedEvent 后的关闭钩子，用于统一触发自定义 `Lifecycle.close()`。
- [application.yml](../../../../open-java/snail-ai/snail-ai-starter/src/main/resources/application.yml)
  HTTP 端口、上下文路径、数据库、gRPC、资源存储、Skill 目录和短期记忆默认配置。
- [logback-boot.xml](../../../../open-java/snail-ai/snail-ai-starter/src/main/resources/logback-boot.xml)
  控制台日志、按级别滚动文件日志和异步 appender 配置。
- [Docker 部署文档](../../../../open-java/snail-ai/docs/deploy/docker.md)
  说明依赖组件由 Docker Compose 启动，Snail AI Server 可用 Maven/JAR 单独启动。
- [配置参考文档](../../../../open-java/snail-ai/docs/deploy/configuration.md)
  对 `application.yml` 的 HTTP、gRPC、数据库、资源和记忆配置做集中解释。

## 智慧（社区）

- 暂未收录外部社区。当前主题是源码边界课，优先依据工作区内源码、部署文档和配置文档验证结论。

## 空白

- 尚未为 Snail AI 上游 Issues、Discussions 或用户群建立稳定入口；后续若需要排查真实部署问题，应补充官方社区链接和常见故障案例。
