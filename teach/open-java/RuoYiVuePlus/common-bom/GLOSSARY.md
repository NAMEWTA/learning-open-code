# ruoyi-common-bom Glossary

记录学习者在 3 节课程中**真正理解**的核心术语。

## Terms

**BOM（Bill of Materials）**：
Maven 的一种特殊 POM 类型（`packaging=pom`），不产出任何 JAR/WAR 构件，唯一的职责是在 `<dependencyManagement>` 中集中声明一组依赖的统一版本。其他项目通过 `scope=import` 导入该 POM，即可让所有声明的依赖自动获得指定版本——实现「一处声明，全局生效」。
_Avoid_: 「物料清单文件」（BOM 是 Maven 术语，不是泛指任何清单）。

**dependencyManagement**：
Maven POM 中的配置区块，用于**声明依赖的版本**而不实际引入依赖。它只定义「如果某个模块要用这个依赖，版本应该是多少」，本身不往 classpath 添加任何 jar。子模块在自己的 `<dependencies>` 中引用时无需再写 `<version>`，版本由最近的 `<dependencyManagement>` 决定。
_Avoid_: 「依赖管理器」（易与 Spring 的 `DependencyManager` 混淆）。

**${revision}（CI Friendly 版本变量）**：
Maven 3.2+ 引入的一种特殊属性，用于在 POM 的 `<version>` 字段中替代硬编码的版本号。配合 `flatten-maven-plugin` 使用：开发时 POM 写 `<version>${revision}</version>`，打包时插件将变量替换为真实版本号（如 `6.0.0-BETA`）。发布到 Maven 仓库的 `.pom` 文件中不含任何变量，保证下游消费者兼容。
_Avoid_: 「动态版本号」（revision 在构建时即确定，非运行时动态）。

**flatten-maven-plugin**：
Mojohaus 社区的 Maven 插件（本项目使用 1.7.3 版本），核心功能是「展平」POM 文件中的变量占位符。本项目的 `resolveCiFriendliesOnly` 模式只替换 `${revision}` / `${sha1}` / `${changelist}` 三个 CI 变量，不改变其他任何内容。在 `process-resources` 阶段执行 `flatten` goal，在 `clean` 阶段执行 `clean` goal 还原 `.flattened-pom.xml`。
_Avoid_: 「POM 精简插件」（它的核心是「变量替换」而非「去掉不必要的信息」）。

**scope=import（BOM 导入范围）**：
Maven `<dependency>` 的一种特殊 `<scope>` 值，仅用于 `<dependencyManagement>` 内部的 `type=pom` 依赖。语义是：把目标 POM 的 `<dependencyManagement>` 内容「合并」到当前 POM 的 `<dependencyManagement>` 中——相当于把远程 BOM 的版本声明全部复制过来。这是 BOM 机制生效的唯一方式。
_Avoid_: 「导入依赖」（scope=import 不引入传递依赖，只引入版本声明）。

**版本仲裁（Dependency Mediation）**：
Maven 在依赖树中出现同一依赖多个版本时的「选胜者」规则：**深度优先 → 先声明优先**。具体为：①到依赖树的根路径最短的版本胜出；②同深度时，在 POM 中先声明的胜出。BOM 通过 `<dependencyManagement>` 在最近祖先（父 POM）处直接锁定版本，使得所有子模块都使用同一版本，绕过仲裁的不确定性。
_Avoid_: 「依赖冲突解决」（仲裁是 Maven 自动进行的，不是手动解决）。

**packaging=pom**：
Maven 的一种打包类型，表示该模块不产出二进制构件（无 JAR/WAR），仅作为 POM 文件存在。聚合模块（带 `<modules>`）和 BOM 模块都使用此类型。本模块的 `ruoyi-common-bom` 即是一例。
_Avoid_: 「POM 类型」（全称是 `packaging=pom`，与 `type=pom` 含义不同但常关联）。

**聚合 POM（Aggregator POM）vs BOM**：
聚合 POM（如 `ruoyi-common/pom.xml`）用 `<modules>` 声明「构建时按什么顺序编译子模块」——管的是**构建顺序**。BOM（如 `ruoyi-common-bom/pom.xml`）用 `<dependencyManagement>` 声明「依赖版本是多少」——管的是**版本一致性**。同一个 POM 可以同时是聚合 POM 和 BOM，但本项目中两者分离。
_Avoid_: 「父 POM」（聚合 POM 和 BOM 都不一定非得是父 POM，只是常见用法）。

**GAV（GroupId:ArtifactId:Version）**：
Maven 坐标三要素。在 RuoYi-Vue-Plus 中，所有 `ruoyi-common-*` 模块的 `groupId` 统一为 `org.dromara`，`version` 统一为 `${revision}`（即 `6.0.0-BETA`），`artifactId` 各模块独立。BOM 的作用就是通过 GAV 精确锁定「谁、是什么版本」。
_Avoid_: 「Maven 坐标」（GAV 是坐标的精确组成部分）。

**type=pom**：
Maven `<dependency>` 中 `<type>` 为 `pom` 时，表示这个依赖本身是一个 POM 构件而非 JAR。导入 BOM 时 `<type>pom</type>` 是**必须的**——它告诉 Maven：「这个依赖的产物是一个 POM 文件，请解析它的 `<dependencyManagement>` 区块」，而非去找 JAR。
_Avoid_: 与 `packaging=pom` 含义不同：前者是「我要消费一个 POM 类型的产物」，后者是「我这个模块的打包方式是 POM」。

## 待收录
- 无 —— 课程已全部完成。

## Rules
- 仅在用户**真正理解**术语后才收录——术语表是压缩知识的记录，不是字典。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 定义内部使用术语表自身的术语——一旦入库，后续定义优先使用它。
- 理解加深时在原文上修订，不留过时条目。
