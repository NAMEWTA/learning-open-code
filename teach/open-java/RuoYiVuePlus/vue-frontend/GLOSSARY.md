# Vue 前端完整架构 - 术语表

| 术语 | 定义 | 使用场景 |
|------|------|----------|
| main.ts (入口文件 / Entry File) | Vue 3 应用的启动入口，负责组装插件链、注册指令、挂载根组件 | 所有启动逻辑在此文件中以 11 步序列执行 |
| createApp (创建应用 / Create Application) | Vue 3 的工厂函数，创建应用实例，后续通过 app.use() 注册插件 | main.ts 中 `const app = createApp(App)` |
| app.use() (插件注册 / Plugin Registration) | Vue 3 的插件安装方法，调用插件的 install(app) 函数进行全局注册 | main.ts 中链式注册 HighLight、ElementIcons、Pinia、Router、i18n 等 |
| el-config-provider (Element Plus 全局配置提供者) | Element Plus 的根上下文组件，注入语言包和组件尺寸到整个组件树 | App.vue 中包裹 `<router-view />` |
| 副作用导入 (Side-effect Import) | 仅通过 `import './file'` 执行模块顶层代码，不导入任何绑定 | `import './permission'` 注册路由守卫 |
| app.config.globalProperties (全局属性 / Global Properties) | Vue 3 应用实例的全局属性挂载点，所有组件实例可访问 | 注册 $tab、$modal、$cache、$download、$auth 五个全局方法 |
| installPlugin (插件安装函数 / Plugin Install Function) | 自定义插件函数，接收 app 实例并通过 globalProperties 挂载全局方法 | src/plugins/index.ts 中定义并导出 |
| directive (指令 / Directive) | Vue 3 的自定义指令，通过 app.directive() 注册，在 DOM 元素上添加行为 | v-hasPermi、v-hasRoles、v-copyText |
| @use (SCSS 模块导入 / SCSS Module Import) | SCSS 的模块系统语法，保证每个模块只加载一次 | src/assets/styles/index.scss 中按序加载 theme、layout、components |
| UnoCSS (原子 CSS 引擎 / Atomic CSS Engine) | 构建时按需生成 CSS 的原子化引擎，兼容 Tailwind CSS 工具类 | virtual:uno.css 导入，uno.config.ts 配置 |
| constantRoutes (常量路由 / Constant Routes) | 构建时已注册的路由表，包含登录页、404 等固定页面 | src/router/index.ts 中预定义 |
| dynamicRoutes (动态路由 / Dynamic Routes) | 根据用户权限在运行时动态注入的路由表 | 登录后通过 filterDynamicRoutes 过滤并 addRoute 注入 |
| router.beforeEach (路由前置守卫 / Route Before Guard) | Vue Router 的全局前置导航守卫，在每次路由切换前执行 | src/permission.ts 中实现登录态校验和动态路由注入 |
| whiteList (白名单 / Whitelist) | 无需登录即可访问的路由列表 | beforeEach 中判断：无 token 时仅白名单路由放行 |
| addRoute (动态添加路由 / Add Route Dynamically) | Vue Router 的运行时路由注入 API，添加新路由到路由器实例 | generateRoutes 后将后端菜单转换为路由并调用 addRoute 注入 |
| generateRoutes (生成路由表 / Generate Routes) | permission store 中的核心方法，从后端拉取菜单树并转换为前端路由 | 登录后 beforeEach 中调用 |
| filterAsyncRouter (异步路由过滤器 / Async Router Filter) | 将后端菜单中的字符串组件名映射为真实的 Vue 异步组件 | generateRoutes 中调用，处理三份菜单数据 |
| import.meta.glob (Vite 全局导入 / Vite Glob Import) | Vite 的静态导入语法，构建时将匹配的文件路径转为加载函数映射表 | 预建 viewModuleMap，运行时 O(1) 查找组件 |
| structuredClone (结构化克隆 / Structured Clone) | JavaScript 原生深拷贝方法，比 JSON.parse(JSON.stringify()) 更可靠 | generateRoutes 中将菜单数据克隆三份，分别用于侧边栏、路由注册、顶栏 |
| createCustomNameComponent (自定义名称组件 / Custom Name Component) | 为异步组件包裹一个有 name 的壳层组件，用于 keep-alive 缓存匹配 | filterAsyncRouter 中通过 loadView 间接调用 |
| duplicateRouteChecker (路由名称重复检测器) | 检查本地动态路由和后端菜单路由是否有重复 name 的防御性工具 | generateRoutes 末尾调用，重复 name 导致 keep-alive 混乱 → 404 |
| Pinia (Vue 状态管理库 / Vue State Management Library) | Vue 3 的官方状态管理库，替代 Vuex | src/store/modules/ 下所有 store 模块 |
| Setup Store 语法 (Setup Store Syntax) | Pinia 的 Composition API 风格 store 定义方式 | 所有 store 模块均使用 `defineStore('name', () => { ... })` |
| useStorage (VueUse 持久化存储 / VueUse Persistent Storage) | VueUse 提供的响应式 localStorage 封装，ref 值自动同步到 localStorage | app store 的 sidebarStatus、language、size；settings store 的 layout-setting |
| await-to-js (Go 风格错误处理 / Go-style Error Handling) | 将 Promise 的 reject 转为 [Error, Data] 元组的工具库 | store 中所有异步操作用 `const [err, res] = await to(promise)` |
| user store (用户状态 / User State) | 管理 token、roles、permissions、用户信息的 Pinia store | 登录/注销/getInfo，所有权限判断的锚点 |
| permission store (权限路由状态 / Permission Route State) | 管理路由表（完整路由、侧边栏菜单、顶栏菜单）的 Pinia store | generateRoutes 填充路由表，Layout 组件消费 |
| app store (应用壳层状态 / App Shell State) | 管理侧边栏状态、设备类型、语言、组件尺寸的 Pinia store | 侧边栏折叠、设备自适应、el-config-provider 语言注入 |
| settings store (设置状态 / Settings State) | 管理主题色、导航模式、标签页开关等用户偏好配置 | 主题/布局切换，useStorage 持久化到 localStorage |
| tagsView store (标签页状态 / Tags View State) | 管理已打开标签页、缓存列表、iframe 标签页 | 标签页的增删改查、keep-alive 缓存控制 |
| dict store (字典状态 / Dictionary State) | 管理字典数据的本地缓存 Map | setDict/getDict，配合 DictTag 组件使用 |
| Axios 实例 (Axios Instance) | 通过 axios.create() 创建的自定义请求实例，独立于全局 axios | src/utils/request.ts 中创建 service 实例 |
| 请求拦截器 (Request Interceptor) | Axios 在请求发送前执行的函数链 | Token 注入、防重复提交、参数加密 |
| 响应拦截器 (Response Interceptor) | Axios 在响应返回后执行的函数链 | 响应解密、统一错误码处理、401 重新登录 |
| RSA + AES 混合加密 (RSA + AES Hybrid Encryption) | 使用 RSA 公钥加密 AES 密钥、AES 加密请求体的混合加密方案 | POST/PUT 请求中 isEncrypt=true 时启用 |
| JSEncrypt (JS RSA 加密库 / JS RSA Encryption Library) | 浏览器端 RSA 加密的 JavaScript 库 | 加密 AES 密钥，写入 encrypt-key header |
| CryptoJS (JS 加密标准库 / JS Cryptography Standard Library) | 浏览器端 AES 加密的 JavaScript 库 | AES-ECB/PKCS7 加密请求体，解密响应体 |
| crypto.getRandomValues (Web Crypto API) | W3C 标准的浏览器真随机数生成 API | 生成 32 位随机 AES 密钥 |
| 防重复提交 (Anti-duplicate Submission) | 通过 sessionStorage 记录请求 (url, data, time) 防止 500ms 内重复提交 | 请求拦截器中检查，repeatSubmit: false 可关闭 |
| isRelogin 全局锁 (Global Re-login Lock) | 模块级单例变量，防止多个 401 响应同时弹出重新登录对话框 | 响应拦截器中 401 处理 |
| createHandledError (创建已处理错误 / Create Handled Error) | 创建一个携带 isHandled=true 标记的 Error 对象 | 拦截器处理后标记错误，防止上层重复弹窗 |
| isToken (Token 注入标志 / Token Injection Flag) | 自定义 header，设为 false 时跳过 Token 注入 | 登录接口：还没 token |
| isEncrypt (加密标志 / Encryption Flag) | 自定义 header，设为 true 时启用 RSA+AES 加密 | 登录、重置密码等敏感接口 |
| repeatSubmit (重复提交标志 / Repeat Submit Flag) | 自定义 header，设为 false 时关闭防重复提交检查 | 允许快速重复提交的接口（语义反转） |
| AxiosPromise (Axios Promise 类型包装) | 项目定义的泛型工具类型，封装返回值结构为 Promise<RuoYiAjaxResult<T>> | API 函数返回值类型标注 |
| PageResult (分页结果类型 / Pagination Result Type) | 分页接口的标准返回类型 { total: number; rows: T[] } | 全局共享类型，所有列表接口使用 |
| Layout (布局根组件 / Layout Root Component) | 中后台布局的根组件，包含侧边栏、顶栏、标签页、内容区 | src/layout/index.vue，所有业务页面的父级 |
| NavTypeEnum (导航类型枚举 / Navigation Type Enum) | 定义了 LEFT、TOP、MIX 三种导航布局模式 | settingsStore.navType 切换 |
| SidebarItem (侧边栏菜单项 / Sidebar Menu Item) | 递归渲染菜单树的核心组件，自引用实现无限层级 | 侧边栏和 TopBar 中复用 |
| hasOneShowingChild (单子路由检测 / Single Child Detection) | 判断父路由是否只有一个可见子路由，若是则跳过父级直接显示子项 | SidebarItem 中优化菜单层级 |
| alwaysShow (强制显示父级 / Always Show Parent) | 菜单 meta 属性，即使只有一个子路由也强制显示父级折叠菜单 | 配合 hasOneShowingChild 使用 |
| TopBar (顶部导航栏 / Top Navigation Bar) | TOP 模式下的水平菜单栏，含自适应溢出处理 | Navbar 组件中渲染，visibleNumber 计算可见数量 |
| keep-alive (组件缓存 / Component Cache) | Vue 内置的组件缓存机制，通过 include 数组控制缓存哪些组件 | AppMain.vue 中根据 tagsView 的 cachedViews 缓存页面 |
| cachedViews (缓存视图列表 / Cached Views List) | tagsView store 中维护的 keep-alive 缓存白名单 | keep-alive 的 :include 属性绑定 |
| affix (固定标签 / Affixed Tab) | 路由 meta 属性，标记页面标签不可关闭 | 首页的 affix: true |
| useWindowSize (窗口尺寸监听 / Window Size Watcher) | VueUse 提供的响应式窗口尺寸 composable | Layout 中监听宽度变化，992px 断点切换桌面/移动端 |
| v-hasPermi (权限指令 / Permission Directive) | 自定义指令，根据权限字符从 DOM 中移除无权限的元素 | `<el-button v-hasPermi="['system:user:add']">` |
| v-hasRoles (角色指令 / Role Directive) | 自定义指令，根据角色编码从 DOM 中移除无权限的元素 | `<el-button v-hasRoles="['admin', 'common']">` |
| v-copyText (复制指令 / Copy Directive) | 自定义指令，点击元素时复制指定文本到剪贴板 | `<span v-copyText="'要复制的文本'">点击复制</span>` |
| $auth (权限验证插件 / Auth Plugin) | 全局方法插件，提供 hasPermi/hasPermiOr/hasPermiAnd/hasRole/hasRoleOr/hasRoleAnd | 组件逻辑中程序化判断权限 |
| filterDynamicRoutes (动态路由过滤器 / Dynamic Route Filter) | 根据本地路由定义的 permissions/roles 字段过滤有权限的路由 | generateRoutes 中处理 local dynamicRoutes |
| 超级管理员绕过 (Super Admin Bypass) | 权限检查中为超级管理员预留的硬编码绕过逻辑 | '*:*:*' 权限字符、'admin' 角色自动通过所有检查 |
| composable (组合式函数 / Composable) | Vue 3 的可复用逻辑函数，以 use 前缀命名 | src/hooks/ 目录下的 10 个 composables |
| useTableSelection (表格多选 Composable) | 封装表格多选逻辑，返回 ids、selectedRows、single、multiple | 批量删除/导出场景 |
| useSearchToggle (搜索切换 Composable) | 封装搜索表单的显示/隐藏状态 | 配合 RightToolbar 的搜索按钮 |
| useSearchReset (搜索重置 Composable) | 封装搜索表单重置逻辑，含分页参数归位和自定义回调 | 所有 CRUD 页面的重置按钮 |
| useFormDialog (表单弹窗 Composable) | 封装表单弹窗的打开/关闭/重置，打开时自动重置表单 | 新增/编辑弹窗 |
| useDateRangeQuery (日期范围 Composable) | 将日期范围选择器值展开为 beginTime/endTime 查询参数 | 列表页的日期范围筛选 |
| useDialogState (弹窗状态 Composable) | 通用弹窗的打开/关闭状态管理，返回 reactive 对象 | 任何弹窗的基础 composable |
| useLoading (加载态 Composable) | 异步操作的 loading 状态管理，提供 withLoading 高阶包装器 | 所有异步请求的 loading 控制 |
| useTreeTableExpand (树表格展开 Composable) | 树形表格的全展开/全收起控制 | 部门管理等树表格页面 |
| useTreeCollapsed (树折叠 Composable) | 左侧树形筛选面板的折叠/展开状态 | TreePanel 组件配合使用 |
| Vite (构建工具 / Build Tool) | 下一代前端构建工具，基于 ESM 的开发服务器和 Rollup 的生产构建 | vite.config.ts |
| loadEnv (加载环境变量 / Load Environment Variables) | Vite 提供的环境变量加载函数，过滤 VITE_ 前缀暴露给客户端 | vite.config.ts 中 `loadEnv(mode, process.cwd())` |
| unplugin-auto-import (自动导入插件 / Auto Import Plugin) | Vite 插件，自动导入 Vue API、VueUse、Pinia，无需手动 import | 开发者直接使用 ref/computed/watch 无需 import |
| unplugin-vue-components (组件自动导入插件 / Components Auto Import Plugin) | Vite 插件，自动导入 Element Plus 组件，无需手动 import | 模板中直接使用 `<el-button>` 无需 import |
| vite-plugin-svg-icons-ng (SVG 精灵图插件 / SVG Sprite Plugin) | Vite 插件，构建时将 SVG 文件注册为 symbol，通过 <use> 引用 | SvgIcon 组件 + virtual:svg-icons-register |
| vite-plugin-compression (压缩插件 / Compression Plugin) | Vite 插件，构建后对产物进行 Gzip/Brotli 压缩 | .env.production 中 VITE_BUILD_COMPRESS 配置 |
| i18n / Vue I18n (国际化 / Internationalization) | Vue 的国际化库，提供 $t() 翻译函数和多语言切换 | src/lang/ 目录，支持 zh_CN 和 en_US |
| .env.development (开发环境配置 / Development Environment Config) | Vite 开发模式的环境变量文件 | VITE_APP_BASE_API=/dev-api，开发代理前缀 |
| .env.production (生产环境配置 / Production Environment Config) | Vite 生产构建的环境变量文件 | VITE_APP_BASE_API=/prod-api，生产 API 前缀 |
| Vite Proxy (Vite 开发代理) | Vite 开发服务器的请求代理功能，解决开发时跨域问题 | /dev-api → http://localhost:8080 |
| Pagination (分页组件 / Pagination Component) | 封装 ElPagination 的通用分页组件，v-model 绑定 queryParams | 所有列表页底部 |
| RightToolbar (表格工具栏组件 / Table Toolbar Component) | 表格右上方的搜索/刷新/列设置/导出工具栏 | 所有列表页顶部 |
| SvgIcon (SVG 图标组件 / SVG Icon Component) | 通过 icon-class 属性引用 SVG 精灵图中的图标 | 菜单图标、页面图标 |
| FileUpload (文件上传组件 / File Upload Component) | OSS 文件上传的通用组件，支持拖拽和限制 | 文件管理、表单附件上传 |
| ImageUpload (图片上传组件 / Image Upload Component) | 图片上传+预览组件 | 头像上传、商品图片 |
| Editor (富文本编辑器 / Rich Text Editor) | wangEditor 的 Vue 封装组件 | 通知公告、邮件模板编辑 |
| DictTag (字典标签组件 / Dictionary Tag Component) | 根据字典数据渲染状态标签 | 列表页的状态列 |
| IconSelect (图标选择器 / Icon Selector) | 可视化选择的图标选择器弹窗组件 | 菜单管理中配置图标 |
| TreePanel (树形面板 / Tree Panel) | 左侧树 + 右侧内容的通用布局面板 | 部门管理、字典管理等 |
| ParentView (父级视图 / Parent View) | 空父级菜单的路由占位组件，实际渲染 router-view | 后端菜单配置中 component: 'ParentView' |
| iFrame (内嵌框架 / Inline Frame) | 外链菜单的内嵌 iframe 组件 | component: 'InnerLink' 的菜单项 |
| Breadcrumb (面包屑 / Breadcrumb) | 根据当前路由的 meta 信息自动生成的面包屑导航 | Navbar 组件中显示 |
| Hamburger (汉堡按钮 / Hamburger Button) | 侧边栏折叠/展开的汉堡图标按钮 | Navbar 组件左侧 |
| UserSelect (用户选择器 / User Selector) | 弹窗搜索+多选的用户选择组件 | 流程审批人选择 |
| DocLink (文档链接 / Documentation Link) | 右下角悬浮的文档链接按钮 | 快速访问 RuoYi-Vue-Plus 文档 |
