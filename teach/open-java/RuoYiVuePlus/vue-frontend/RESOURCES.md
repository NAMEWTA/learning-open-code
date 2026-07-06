> **服务工作流：** `../T-teach/T-teach.md`
> **产物文件名：** `resources.md`
> **父目录规则：** 本模板产物写入 `YYYY-MM-DD-<kebab-name>/` change 目录内

# Vue 前端完整架构 Resources

## Knowledge

- **官方文档: _Vue Router 4/5 — 动态路由与导航守卫_ — Vue.js 官方**
  https://router.vuejs.org/zh/guide/advanced/dynamic-routing.html
  覆盖动态路由 `addRoute` / `removeRoute` API、全局前置守卫 `beforeEach` 的 resolve 流程、路由元信息 `meta` 的类型扩展。**当学习 permission store 的 `generateRoutes()` 方法和 `permission.ts` 路由守卫时需要反复查阅此文档。**

- **官方文档: _Pinia — Setup Store 语法与组合式 API_ — Pinia 官方**
  https://pinia.vuejs.org/zh/core-concepts/
  覆盖 `defineStore` 的 Setup Store 语法（与 Options Store 的对比）、`$patch`、`$reset`、`$subscribe` 等实例方法，以及在 `useStorage`（VueUse）配合下实现持久化的模式。**当分析 `useUserStore`、`useAppStore`、`useSettingsStore`、`useTagsViewStore` 等 7 个 store 模块时，以此为语法基准。**

- **官方文档: _Axios — 拦截器机制与实例化模式_ — Axios 官方**
  https://axios-http.com/zh/docs/interceptors
  覆盖请求/响应拦截器的注册、执行顺序、`config` 对象的动态修改（headers 注入、参数加密）、错误传播链。**当追踪 `src/utils/request.ts` 中 RSA+AES 混合加密、防重复提交、401 重新登录弹窗等拦截逻辑时必须对照此文。**

- **官方文档: _Element Plus — 组件体系与主题定制_ — Element Plus 官方**
  https://element-plus.org/zh-CN/component/overview.html
  覆盖 ElTable、ElForm、ElDialog、ElTree 等核心组件的 API 设计、插槽机制、事件约定，以及 CSS 变量驱动的主题定制和暗黑模式。**当阅读 `plus-ui-vue` 中的业务页面（`views/system/user/index.vue` 等）和自定义组件封装（`Pagination`、`RightToolbar` 等）时，需以 Element Plus 组件 API 作为理解基线。**

- **官方文档: _Vite — 构建配置、环境变量与代理_ — Vite 官方**
  https://cn.vitejs.dev/config/
  覆盖 `defineConfig` 中的 `resolve.alias`、`server.proxy` 代理配置、`build` 优化选项、环境变量 `import.meta.env` 的加载机制（`loadEnv` + `VITE_` 前缀约定）。**当分析 `vite.config.ts`、`.env.development`/`.env.production` 环境文件、以及 `vite/plugins/` 目录中的 UnoCSS / auto-import / SVG-icons 等插件时，需要此文档作为工程化参考。**

- **开源项目: _vue-element-plus-admin — 中后台前端解决方案_ — 官方示例**
  https://github.com/kailong321200875/vue-element-plus-admin
  一个与 RuoYi-Vue-Plus 前端架构高度相似的开源中后台模板，同样使用 Vue 3 + Element Plus + Pinia + Vue Router。覆盖完整的路由权限、布局系统、标签页管理等模式。**当需要对比理解 RuoYi 前端的某些设计决策（如动态路由生成、多布局切换、标签页持久化）在其他项目中的不同实现方式时，可以进行横向对比学习。**

- **开源项目: _RuoYi-Vue-Plus 后端仓库 — 前后端 API 契约_ — Dromara 社区**
  https://github.com/dromara/RuoYi-Vue-Plus
  前端所有 API 调用的后端对端实现。覆盖菜单路由数据结构（`/system/menu/getRouters` 返回的 `RouteRecordRaw[]` 格式）、登录响应体（`LoginResult` 中的 `access_token` 字段）、用户权限信息（`UserInfo` 中的 `roles`、`permissions` 字段）、字典数据结构等。**当追踪前端数据流时需要对照后端返回的实际 JSON 结构，以确保理解的前端处理逻辑与后端契约一致。**

## Wisdom (Communities)

- **在线社区: _RuoYi-Vue-Plus 官方 Gitee 仓库 Issues 区_ — Dromara 社区**
  https://gitee.com/dromara/RuoYi-Vue-Plus/issues
  项目的官方问题跟踪区，包含大量真实用户遇到的前端问题（路由 404、权限不生效、菜单不显示、Token 过期处理等）和官方维护者的回复。**当遇到具体技术障碍或想了解常见坑点时，搜索相关 issue 获取社区智慧和解决方案。**

- **在线社区: _Element Plus 中文社区 / Discord_ — Element Plus 团队**
  https://github.com/element-plus/element-plus/discussions
  Element Plus 官方的 GitHub Discussions，涵盖组件使用疑问、主题定制技巧、版本升级迁移等问题。**当业务开发中遇到 Element Plus 组件的非预期行为或高级用法时，在此寻求针对性帮助。**

## Gaps
- 路由 Name 重复检测机制（`duplicateRouteChecker`）和 `createCustomNameComponent` 为组件注入 `name` 选项的实现，属于项目特有的工程化技巧，社区中无直接的教程资源，需要直接阅读 `src/store/modules/permission.ts` 和 `src/utils/createCustomNameComponent.tsx` 源码。
- RSA + AES 混合加密的请求体加密方案（`src/utils/crypto.ts` + `src/utils/jsencrypt.ts`）属于项目自研的前后端加密协议，社区无通用教程，需对照 `src/utils/request.ts` 中的拦截器代码和后端安全配置一起理解。
- `unplugin-auto-import` 和 `unplugin-vue-components` 实现的自动导入机制在 Vite 插件层配置，对初学者存在理解门槛。当需要理解为什么某些 API（如 `ref`、`ElMessage`）无需手动 import 时，需阅读 `vite/plugins/` 中的 auto-import 配置和这两个插件的官方文档。
