# ruoyi-common-bom 资源清单

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充 Maven 原理与官方约定。

## Knowledge

- [代码: _ruoyi-common-bom 核心 POM_](RuoYi-Vue-Plus/ruoyi-common/ruoyi-common-bom/pom.xml)
  本模块唯一文件。集中声明 22 个 `ruoyi-common-*` 依赖的统一版本 `${revision}`。任何关于「BOM 管理了哪些依赖」的问题，答案都在这个文件里。

- [代码: _父 POM — BOM 导入处 + flatten-maven-plugin 配置_](RuoYi-Vue-Plus/pom.xml)
  第 157-164 行：`ruoyi-common-bom` 以 `scope=import`、`type=pom` 的方式导入到父 POM 的 `<dependencyManagement>` 中。第 75 行：`flatten-maven-plugin` 版本声明；第 523-548 行：插件完整配置（`resolveCiFriendliesOnly` + `process-resources` 阶段执行）。这是理解「BOM 如何生效」和「版本号如何替换」的两个关键锚点。

- [代码: _ruoyi-admin 业务模块 POM — BOM 生效现场_](RuoYi-Vue-Plus/ruoyi-admin/pom.xml)
  示例：`ruoyi-common-doc`、`ruoyi-common-social`、`ruoyi-common-mail` 等依赖只写 `groupId` 和 `artifactId`，没有 `<version>`——版本全部由父 POM 中导入的 BOM 提供。这是验证「BOM 版本仲裁生效」的最佳证据。

- [代码: _ruoyi-common 聚合 POM — 模块列表_](RuoYi-Vue-Plus/ruoyi-common/pom.xml)
  列出 22 个子模块的 `<modules>` 列表。与 BOM 的 `<dependencyManagement>` 对照阅读，可以看清「模块树」与「版本管理」的职责分离。

- [官方文档: _Maven POM Reference — Dependency Management_（maven.apache.org）](https://maven.apache.org/pom.html#Dependency_Management)
  `dependencyManagement` 与 `dependencies` 两大章节的官方定义。理解「声明版本但不下发传递依赖」的原理时查阅。

- [代码: _flatten-maven-plugin 官方文档_ — MojoHaus（mojohaus.org）](https://www.mojohaus.org/flatten-maven-plugin/)
  理解 `resolveCiFriendliesOnly` 模式替换 `${revision}` 的机制、`updatePomFile` 参数含义时查阅。本项目的核心版本管理方案依赖此插件。

- [官方文档: _Maven CI Friendly Versions_（maven.apache.org）](https://maven.apache.org/maven-ci-friendly.html)
  Maven 3.x 引入的 `${revision}` / `${sha1}` / `${changelist}` 属性规范。理解「为什么需要 flatten-maven-plugin」的根本原因——Maven 3.x 不支持变量占位符在发布 POM 中的自动解析。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么 BOM 这样组织」「版本升级策略」时，Issues 与讨论区最贴近维护者意图。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库 POM 文件 + 上述 Maven 官方文档 + flatten-maven-plugin 文档支撑。
