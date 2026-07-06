# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-common-bom 统一版本管理模块

## Why
学习者要能彻底读懂 `ruoyi-common-bom` 这个纯 POM 构件：它没有任何 Java 代码（`packaging=pom`），却是整个 RuoYi-Vue-Plus 项目依赖版本管理的「总调度中心」——通过 Maven BOM（Bill of Materials）机制集中管理全部 22 个 `ruoyi-common-*` 子模块 + `ruoyi-common-redis` + `ruoyi-common-sms` 的统一版本。理解它，等于理解 Maven 多模块项目的版本治理核心：`dependencyManagement` 如何实现「一处声明、全局生效」、`${revision}` 属性如何与 `flatten-maven-plugin` 配合解决 Maven 3.x 的 CI Friendly 版本号问题、以及 BOM 的 `scope=import` 导入机制如何在父 POM 中生效。目标是**读懂设计动机与版本仲裁链**，不是从零学 Maven。

## Success looks like
- 能用一句话说清 BOM 是什么、为什么多模块 Maven 项目需要它，以及 `dependencyManagement` 与 `dependencies` 的本质区别。
- 能解释 `ruoyi-common-bom` 的 `pom.xml` 中每个 XML 节点的设计意图：`<packaging>pom</packaging>`、`<dependencyManagement><dependencies>...</dependencies></dependencyManagement>`、`<version>${revision}</version>`。
- 能讲清 `${revision}` 属性 + `flatten-maven-plugin`（`resolveCiFriendliesOnly` 模式）这套「Maven 3.x CI Friendly 版本号」方案的工作流程：声明时用变量 → 打包时插件替换为真实版本 → 发布到仓库的 POM 里变量消失。
- 能追踪「父 POM 如何通过 `scope=import` 导入 BOM」→「子模块如何省写 `<version>` 直接从 BOM 拿版本」→「Maven 依赖仲裁如何选择最终版本」这条完整链路。
- 能说清 `ruoyi-common-bom` 管理的全部 22 个依赖（按注释分组：核心、接口、excel、调度、日志、邮件、数据库、OSS、缓存、satoken、安全、短信、ES、社交、web、翻译、脱敏、序列化、加密、推送、mqtt、ai、mcp），并能解释为什么 `ruoyi-common-redis` 和 `ruoyi-common-sms` 不在 BOM 的 `modules` 列表里却在 `dependencyManagement` 里。
- 能独立完成「新增一个 `ruoyi-common-xxx` 模块并接入 BOM」和「统一升级所有 common 模块版本」两个实操任务。

## Constraints
- 学习者是全栈背景，有 Maven 基础使用经验（会 `mvn clean install`、知道 `pom.xml` 长什么样），但对 BOM、`dependencyManagement`、版本仲裁等高级特性不熟悉。
- 目标是「读懂设计 + 能上手操作」，不是「精通 Maven 规范」——课程以追踪本仓库真实 pom.xml 代码、解释设计动机为主，练习以「读 POM 答问题 / 模拟操作」为主。
- 全部讲解基于仓库真实代码（已逐文件核对），引用具体文件路径与 XML 代码行。
- 交互语言：简体中文。

## Out of scope
- Maven 生命周期、插件机制、坐标（GAV）的完整讲解——点到为止，不展开。
- 各 `ruoyi-common-*` 子模块内部的 Java 代码与业务逻辑——本课程只讲它们的版本如何被 BOM 管理。
- 除了 `flatten-maven-plugin` 外的其它 Maven 插件配置细节。
- Maven 4.0 的原生版本变量支持（仅作为对比提及，不深入）。
- Gradle 的版本目录（Version Catalog）机制——仅在与 BOM 概念对比时点到。
