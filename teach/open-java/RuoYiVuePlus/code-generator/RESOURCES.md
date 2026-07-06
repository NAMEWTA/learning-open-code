# Resources — ruoyi-gen 学习资源策展

## 一手资料（Primary Sources）

### 核心服务与入口

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `GenController.java` | 12 个 REST API 端点全貌：表导入、配置保存、预览、单表/批量下载、同步数据库、查询数据源列表 | 学习入口点——先通读 API 列表，建立对模块能力的整体认知 |
| `IGenTableService.java` | 服务接口契约，定义了导入、预览、下载、同步等核心方法签名 | 理解服务层职责边界，在阅读实现类之前先看接口 |
| `GenTableServiceImpl.java` | 核心业务逻辑：导入表时从 AnyLine 读取元数据、构建渲染上下文、模板渲染、ZIP 打包下载、同步数据库结构 | 深入理解每条 API 的完整处理流程，特别是 `buildRenderContext()` / `writeCodeToZip()` / `synchDb()` |

### 模板引擎层

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `TemplateEngineUtils.java` | 模板引擎核心：FreeMarker 引擎初始化、上下文构建（`buildContext`，将所有表/列/选项信息转换为模板变量字典）、模板列表组装（按 tplCategory + frontendType + 数据库类型选择模板）、输出文件名生成 | 理解"如何把 GenTable 对象变成模板能用的上下文"以及"如何根据配置选择正确的模板组合" |
| `PathNamedTemplate.java` | 模板委托包装器，将模板路径名与 Hutool Template 对象绑定，使模板可同时携带渲染能力和路径标识 | 理解模板文件的组织模型——为什么每个模板需要同时知道"自己是什么"和"渲染出什么文件路径" |
| `GenConstants.java` | 所有常量定义：模板分类（CRUD/TREE）、前端类型（Vue/React）、Java 类型、HTML 控件类型、列类型分组、固定模板路径集合 | 阅读代码时作为常量速查表，理解模板路径的命名约定 |

### 字段初始化与类型推断

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `GenUtils.java` | 表名→类名转换（前缀移除+驼峰命名）、列字段初始化（数据库类型→Java 类型→HTML 控件类型的三层映射）、字段命名约定匹配（status→开关、name→模糊查询、image/avatar→图片上传等） | 理解"为什么同一个 varchar 字段，叫 status 生成开关控件，叫 name 生成文本框"——这是整个生成器智能化的核心 |
| `GenTable.java` | 业务表领域模型：包含生成所需的所有元信息（包名、模块名、业务名、模板分类、前端类型、树表参数），以及 `isTree()`/`isCrud()`/`isSuperColumn()` 等判断方法 | 理解"用户在前端配置了什么信息"以及这些信息如何在模板间传递 |
| `GenTableColumn.java` | 列字段领域模型：包含数据库列信息（列名、类型、是否主键、是否自增）和生成配置（Java 类型、HTML 控件类型、查询方式、是否参与增/改/查/列表），以及 `isPk()`/`isInsert()`/`isDictColumn()`/`getTsType()` 等辅助方法 | 理解每一列的配置如何影响最终生成的代码——为什么一个字段可能在 Controller 中出现但在 BO 中不出现 |

### 动态数据源与元数据引擎集成

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `MyBatisDataSourceMonitor.java` | AnyLine 与 baomidou 动态数据源的桥接器：实现 `DataSourceMonitor` 接口，通过 `ConfigTable.KEEP_ADAPTER=2`（自定义模式）解决同一 JdbcTemplate 对应多种数据库的适配问题 | 理解"代码生成器如何支持切换不同数据源读取不同数据库的表结构" |
| `GenProperties.java` | 代码生成全局配置（作者、默认包名、表前缀移除策略），从 `generator.yml` 加载 | 理解全局配置如何影响表初始化时的默认值填充 |
| `generator.yml` | 全局配置示例文件，定义 author、packageName、autoRemovePre、tablePrefix | 理解配置入口，知道如何修改默认生成参数 |

### FreeMarker 模板文件

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `fm/java/` 目录下的 7 个 `.ftl` 模板 | 后端代码模板：Domain、VO、BO、Mapper、Service、ServiceImpl、Controller。Controller 模板包含条件性生成（导出/状态/排序/唯一校验） | 当需要理解生成的代码结构或修改生成逻辑时，逐模板阅读 |
| `fm/vue/` 目录下的 4 个 `.ftl` 模板 | Vue 前端代码模板：API 封装、TypeScript 类型、标准 CRUD 页面、树表页面 | 当需要修改 Vue 端生成代码风格或添加新控件类型时阅读 |
| `fm/react/` 目录下的 4 个 `.ftl` 模板 | React 前端代码模板：API 封装、TypeScript 类型、标准 CRUD 页面、树表页面 | 当需要修改 React 端生成代码风格时阅读 |
| `fm/sql/` 目录下的 4 个 `.ftl` 模板 | 数据库菜单 SQL 模板：MySQL、Oracle、PostgreSQL、SQL Server 四种方言的菜单数据插入语句 | 理解不同数据库的 SQL 差异如何通过模板分离来解决 |
| `fm/xml/mapper.xml.ftl` | MyBatis Mapper XML 模板：生成基础 CRUD 的 resultMap 和 SQL 片段 | 理解 MyBatis-Plus 下仍需手写 XML 的场景（复杂查询、关联映射） |

### 数据访问层

| 资源 | 覆盖内容 | 何时取用 |
|------|----------|----------|
| `GenTableMapper.java` + `GenTableMapper.xml` | 业务表数据访问：继承 `BaseMapperPlus`，自定义查询已导入表名列表（用于去重），忽略数据权限和租户拦截 | 理解 gen 模块的数据隔离策略——为何需要绕过数据权限拦截 |
| `GenTableColumnMapper.java` | 业务字段数据访问：继承 `BaseMapperPlus`，通过 lambda 查询按 tableId 和 sort 排序获取列信息 | 了解最简单的 Mapper 可以有多简洁（零自定义方法） |

## 依赖框架文档（Secondary Sources）

| 资源 | 覆盖内容 | 链接 |
|------|----------|------|
| FreeMarker 模板语言参考 | 指令语法（if/list/assign）、内建函数（?has_content、?string）、表达式语法 | https://freemarker.apache.org/docs/ |
| AnyLine 官方文档 | 元数据 API（ServiceProxy.metadata()）、adapter 机制、数据源配置 | https://gitee.com/anyline/anyline |
| Hutool 模板引擎封装 | TemplateEngine、TemplateConfig、自定义引擎注册 | https://doc.hutool.cn/pages/TemplateUtil/ |
| MyBatis-Plus 官方文档 | BaseMapperPlus、LambdaQueryWrapper、分页插件 | https://baomidou.com/ |
| baomidou dynamic-datasource | 动态数据源切换（@DS 注解）、多数据源配置 | https://gitee.com/baomidou/dynamic-datasource-spring-boot-starter |

## 推荐社区

- **RuoYi-Vue-Plus 官方 Gitee**：https://gitee.com/dromara/RuoYi-Vue-Plus — 提交 Issue、查看文档和更新日志
- **Dromara 社区**：https://dromara.org/ — RuoYi-Vue-Plus 所属开源组织，包含 AnyLine、Hutool 等依赖项目
- **FreeMarker 邮件列表**：https://freemarker.apache.org/mailing-lists.html — 模板引擎问题的高级讨论
