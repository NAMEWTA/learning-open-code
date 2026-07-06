# 课程快照：common-modules

## 源项目信息
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue-plus`
  - **Git Commit**：`348141427d86fbe39041ffafbc5b26473722cd63`
  - **短 Commit**：`3481414`
  - **分支**：`6.X`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue`
  - **Git Commit**：`728fdbfe0eae5b5b4ed186801ea9e96e8365ced7`
  - **短 Commit**：`728fdbf`
  - **分支**：`6.X-Vue`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-react`
  - **Git Commit**：`e74984e0e05d8807eda19d0a3f7fb9e23771619d`
  - **短 Commit**：`e74984e`
  - **分支**：`6.X-React`
- **快照时间**：2026-07-06T15:39:55+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `# 通过 springdoc.api-docs.enabled 控制开关
springdoc:
  api-docs:
    enabled: true
  swagger-ui:
    path: /swagger-ui.html
  info:
    title: RuoYi-Vue-Plus API
    version: 6.0.0` | 课程分析引用 | 🟡 辅助 |
| `api/login.ts` | 课程分析引用 | 🟡 辅助 |
| `api/monitor/operlog.ts` | 课程分析引用 | 🟡 辅助 |
| `config/ValidatorConfig.java + validate/ 目录` | 课程分析引用 | 🟡 辅助 |
| `constant/ 目录下 6 个常量接口` | 课程分析引用 | 🟡 辅助 |
| `domain/R.java` | 课程分析引用 | 🟡 辅助 |
| `exception/ 目录下 9 个异常类` | 课程分析引用 | 🟡 辅助 |
| `org.dromara:ruoyi-common-core` | 课程分析引用 | 🟡 辅助 |
| `pom.xml` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-admin` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-modules-system` | 课程分析引用 | 🟡 辅助 |
| `service/DictService.java · PermissionService.java` | 课程分析引用 | 🟡 辅助 |
| `src/directive/permission/index.ts` | 课程分析引用 | 🟡 辅助 |
| `src/utils/request.ts` | 课程分析引用 | 🟡 辅助 |
| `src/views/login.vue` | 课程分析引用 | 🟡 辅助 |
| `src/views/monitor/operlog/` | 课程分析引用 | 🟡 辅助 |
| `src/views/system/oss/` | 课程分析引用 | 🟡 辅助 |
| `store/modules/user.ts` | 课程分析引用 | 🟡 辅助 |
| `utils/ 目录下 30+ 个工具类` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01-core-exception-constants | `lessons/01-core-exception-constants.html` | 01 · ruoyi-common-core 核心基石（上）：异常体系与常量设计 |
| 02-core-utils-validation | `lessons/02-core-utils-validation.html` | 02 · ruoyi-common-core 核心基石：异常体系、工具类与参数校验 |
| 03-web-filter-interceptor | `lessons/03-web-filter-interceptor.html` | 03 · ruoyi-common-web：请求处理全链路 |
| 04-web-exception-handler | `lessons/04-web-exception-handler.html` | 04 · ruoyi-common-web：全局异常处理与响应增强 |
| 05-mybatis-entity-mapper | `lessons/05-mybatis-entity-mapper.html` | 05 · ruoyi-common-mybatis：实体基类与增强 Mapper |
| 06-mybatis-data-permission | `lessons/06-mybatis-data-permission.html` | 06 · ruoyi-common-mybatis（中）：数据权限体系全链路 |
| 07-mybatis-query-plugin | `lessons/07-mybatis-query-plugin.html` | 07 · ruoyi-common-mybatis（下）：查询构造器与插件链 |
| 08-encrypt-api-db | `lessons/08-encrypt-api-db.html` | 08 · ruoyi-common-encrypt：API加解密与数据库字段加密 |
| 09-excel-import-export | `lessons/09-excel-import-export.html` | 09 · ruoyi-common-excel：动态导入导出引擎 |
| 10-excel-annotation-dropdown | `lessons/10-excel-annotation-dropdown.html` | 10 · ruoyi-common-excel（下）：注解驱动的列映射与下拉框 |
| 11-json-serialize | `lessons/11-json-serialize.html` | 11 · ruoyi-common-json：Jackson 配置与响应增强框架 |
| 12-satoken-auth | `lessons/12-satoken-auth.html` | 12 · ruoyi-common-satoken：认证与权限核心 |
| 13-security-sensitive | `lessons/13-security-sensitive.html` | 13 · ruoyi-common-security + sensitive：安全拦截与数据脱敏 |
| 14-social-login | `lessons/14-social-login.html` | 14 · ruoyi-common-social：第三方登录 OAuth2.0 集成 |
| 15-log-doc | `lessons/15-log-doc.html` | 15 · ruoyi-common-log + doc：操作日志与API文档 |
| 16-mail-es-mcp | `lessons/16-mail-es-mcp.html` | 16 · ruoyi-common-mail + elasticsearch + mcp：邮件、搜索与AI协议 |
| 17-oss-storage | `lessons/17-oss-storage.html` | 17 · ruoyi-common-oss：对象存储抽象层 |
| 18-translation | `lessons/18-translation.html` | 18 · ruoyi-common-translation：翻译器框架 |
| 19-bom-summary | `lessons/19-bom-summary.html` | 19 · ruoyi-common-bom + 全模块总结：依赖管理与前后端协作全景 |

## 参考资料

- `reference/module-cheatsheet.html`

## 快照摘要
- 课程数：19
- 引用源文件数：19
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
