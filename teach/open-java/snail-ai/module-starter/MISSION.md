# 使命：启动与配置模块

## 为什么
学习者希望能从源码层面判断 Snail AI 应用是如何被 `snail-ai-starter` 启动、装配和交付的。掌握这个模块后，遇到端口、数据库、gRPC、静态后台或日志相关问题时，可以先定位边界，再决定是改 starter 配置、部署参数，还是进入 Server/Agent 业务模块继续排查。

## 成功的样子
- 能说明 `snail-ai-starter` 在整体架构中承担的启动、聚合依赖和配置承载职责。
- 能指出 Spring Boot 主类、默认配置、启动监听、关闭监听和日志配置分别解决什么问题。
- 能用一条 Maven 命令启动服务，并说清 HTTP、gRPC、静态后台和外部依赖的边界。

## 约束条件
- 读者具备 Java 和 Spring Boot 基础，但不假设已经熟悉 Snail AI 的内部模块。
- 本主题是 L1 模块总览，保持 15 分钟短课，细节索引放入参考页。
- 当前任务只写入 `teach/open-java/snail-ai/module-starter/`。

## 不在范围内
- 不深入讲解 Server Controller、Agent Handler Chain、RAG 检索、模型调用或持久化实现。
- 不逐文件解析已构建的前端静态资源 `admin/assets/**`。
- 不修改源项目配置、SQL 脚本、部署脚本或教学进度台账。
