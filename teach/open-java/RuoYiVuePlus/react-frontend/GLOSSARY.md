# GLOSSARY — React 企业级前端（ruoyi-react）术语表

| 术语 | 定义 | 首次出现 |
|------|------|---------|
| **JSX** | JavaScript XML，React 的模板语法。在 .tsx 文件中写类似 HTML 的标签，编译后变成 React.createElement() 调用 | 课程 01 |
| **表达式** | 能放在赋值语句 = 右边的代码片段。JSX 的 {} 中只能放表达式，不能放 if/for 等语句 | 课程 01 |
| **Fragment** | 空标签 `<>...</>`，用于包裹多个相邻 JSX 元素而不产生额外 DOM 节点 | 课程 01 |
| **组件 (Component)** | React 的基本构建单元。是一个函数，接收 props，返回 JSX。首字母必须大写 | 课程 02 |
| **Props** | 父组件传给子组件的只读数据。任意 JS 类型都可以作为 props，包括函数（回调） | 课程 02 |
| **children** | 特殊 prop，写在组件标签<strong>之间</strong>的内容自动传入 | 课程 02 |
| **State** | 组件的内部可读写内存。State 值改变时 React 自动重新渲染组件 | 课程 03 |
| **useState** | React Hook，创建组件内部状态。返回 [当前值, 更新函数]。更新函数触发重渲染 | 课程 03 |
| **useEffect** | React Hook，在渲染之后执行副作用（数据请求、订阅、DOM 操作）。通过依赖数组控制执行时机 | 课程 03 |
| **副作用 (Side Effect)** | 渲染以外的操作：数据请求、修改 DOM、设置定时器、订阅事件 | 课程 03 |
| **依赖数组** | useEffect 的第二个参数 []。空数组=只执行一次；有值=依赖变了执行；省略=每次执行 | 课程 03 |
| **useRef** | React Hook，创建一个可变容器（.current），修改不触发重渲染。常用于 DOM 引用和保存非 UI 值 | 课程 04 |
| **useMemo** | React Hook，缓存昂贵计算结果。依赖不变时返回缓存值，避免重复计算 | 课程 04 |
| **useCallback** | React Hook，useMemo 的函数版。缓存函数引用，用于传给 memo 子组件以避免不必要的重渲染 | 课程 04 |
| **自定义 Hook** | 用 use 开头的普通函数，内部调用其他 Hook，封装可复用逻辑（不封装 UI） | 课程 04 |
| **UmiJS** | 蚂蚁集团出品的企业级 React 框架。提供约定式路由、插件体系、构建优化。ruoyi-react 使用 @umijs/max（满配版） | 课程 05 |
| **约定大于配置** | UmiJS 核心理念。文件放在特定目录就自动拥有特定能力，不需要手工注册 | 课程 05 |
| **app.tsx** | UmiJS 运行时配置入口。导出 getInitialState()（全局初始化）和 rootContainer()（根 Provider 包装） | 课程 05 |
| **config/config.ts** | UmiJS 构建和路由的静态配置文件。定义 routes 数组、插件、代理、别名等 | 课程 05 |
| **Vite** | 下一代前端构建工具，UmiJS 4 底层使用 Vite 作为 bundler | 课程 05 |
| **ProLayout** | @ant-design/pro-components 提供的高级布局组件，提供侧边栏、顶栏、面包屑、菜单等管理后台能力 | 课程 06 |
| **BasicLayout** | ruoyi-react 的主布局组件（src/layouts/BasicLayout.tsx），封装 ProLayout + 菜单 + 标签页 + 用户操作 | 课程 06 |
| **Outlet** | React Router 的占位组件，子路由的内容渲染在此处 | 课程 06 |
| **menuDataRender** | ProLayout 的 prop，返回格式化的菜单数组，渲染为左侧导航栏 | 课程 06 |
| **静态路由** | 写死在 config.ts routes 中的路由（如 /login、/index），所有用户都一样 | 课程 06 |
| **动态路由** | 从后端 API 获取的路由树，根据用户权限不同返回不同菜单和页面 | 课程 06/11 |
| **Zustand** | 极简的 React 全局状态管理库。无需 Provider，通过 create() 创建 store，组件通过 selector 订阅。德文"状态" | 课程 07 |
| **Store** | Zustand 中存储全局状态的容器。包含 state 字段和 action 方法，通过 create() 创建 | 课程 07 |
| **selector** | Zustand 的精准订阅机制。组件通过 useXxxStore(state => state.field) 只订阅需要的字段 | 课程 07 |
| **persist** | Zustand 中间件，自动将 store 数据同步到 localStorage/AsyncStorage | 课程 07/10 |
| **permissionStore** | ruoyi-react 最核心的 store。存储后端路由树（backendRoutes）、格式化菜单（menuData）、权限标识（permissions） | 课程 08 |
| **reloadMenus** | permissionStore 的核心方法。应用启动时调用，并行请求 getInfo() + getRouters()，生成菜单和权限数据 | 课程 08 |
| **appStore** | 布局和外观设置的 store。使用 persist 中间件持久化到 localStorage('layout-setting-react') | 课程 08 |
| **tagsViewStore** | 多标签页状态管理 store。持久化已打开的页面标签列表到 localStorage | 课程 08 |
| **dictStore** | 字典数据缓存 store。配合 useDict Hook 和 react-query 实现 10 分钟 staleTime | 课程 08 |
| **Axios** | 基于 Promise 的 HTTP 客户端（浏览器 + Node.js）。ruoyi-react 用它发所有 API 请求 | 课程 09 |
| **拦截器 (Interceptor)** | Axios 的中间件机制。请求拦截器在发送前处理（附加 token、加密），响应拦截器在返回后处理（解密、错误处理） | 课程 09 |
| **RSA** | 非对称加密算法。ruoyi-react 用 RSA 公钥加密 AES 密钥，后端用 RSA 私钥解密 | 课程 09 |
| **AES** | 对称加密算法。ruoyi-react 用随机 AES 密钥加密请求体，速度快且适合大体积数据 | 课程 09 |
| **两层加密** | RSA 加密 AES 密钥 + AES 加密请求体。兼顾安全性（RSA）和性能（AES） | 课程 09 |
| **401 处理** | 响应拦截器中检测 code=401，弹出重新登录 Modal（防重复：isRelogin.show 标记位） | 课程 09 |
| **localStorage** | 浏览器持久化存储 API，数据在标签页和浏览器重启后仍存在。ruoyi-react 用其存储 Token 和布局设置 | 课程 10 |
| **Token** | JWT 认证令牌。登录后从后端获取，存于 localStorage('Admin-Token')，每次请求通过 Authorization header 携带 | 课程 10 |
| **记住我 (Remember Me)** | 登录页功能。勾选后用 Cookie 保存用户名，下次打开自动回填 | 课程 10 |
| **react-query** | TanStack Query，服务端状态管理库。ruoyi-react 用它缓存字典数据（10min staleTime）和提供请求去重 | 课程 10 |
| **BackendRoute** | 后端返回的路由数据类型。包含 name/path/component/meta/children，是树形结构 | 课程 11 |
| **menuData** | BackendRoute 格式化后的菜单数组，传给 ProLayout 渲染侧边栏 | 课程 11 |
| **DynamicPage** | ruoyi-react 的动态路由调度组件。作为 catch-all 路由，运行时匹配 URL 到后端路由树并渲染对应 React 组件 | 课程 12 |
| **migratedPages** | DynamicPage 中的映射表。key 为 Vue 时代的组件路径（如 @/views/system/user/index），value 为 React 组件 | 课程 12 |
| **findRouteByPath** | 在 BackendRoute 树中递归查找匹配当前 URL 的路由的函数 | 课程 12 |
| **迁移占位卡片 (Migration Placeholder)** | 当后端路由的 component 在 migratedPages 中找不到对应 React 组件时显示的占位 UI，提示"页面尚未迁移" | 课程 12 |
| **permissions** | 从后端路由树提取的权限标识字符串数组（如 ['system:user:list']），用于前端按钮级权限控制 | 课程 12 |
| **ProTable** | @ant-design/pro-components 的高级表格组件。内置搜索、分页、排序、工具栏、刷新等能力 | 课程 13 |
| **columns** | ProTable 的列定义数组。每个 column 定义表格显示（title/dataIndex/render）和搜索行为（valueType/valueEnum） | 课程 13 |
| **valueType** | ProTable column 的属性，决定搜索表单控件的类型（text→Input, select→Select, dateRange→DatePicker.Range） | 课程 13 |
| **request** | ProTable 的 prop，接收异步函数作为数据源。ProTable 自动传入分页和搜索参数，从返回值提取 data 和 total | 课程 13 |
| **render** | column 的自定义渲染函数。参数 (dom, record, index, action)，返回 JSX。最常用于操作列和状态列 | 课程 13 |
| **valueEnum** | column 的枚举值映射对象。用于 select 搜索下拉和表格显示的自动翻译 | 课程 13 |
| **ModalForm** | @ant-design/pro-components 的表单弹窗组件。内置表单验证 + 确定/取消按钮，与 ProTable 配套使用 | 课程 13/14 |
| **字典 (Dict)** | ruoyi 的数据模式。将枚举数据（如状态、类型）存在后端字典表中，前端通过 useDict Hook 获取并在表格/搜索中使用 | 课程 13 |
| **useDict** | ruoyi-react 自定义 Hook。根据字典类型获取字典数据，含 react-query 10 分钟缓存 | 课程 04/13 |
| **actionRef** | ProTable 的 ref。通过 actionRef.current?.reload() 手动刷新表格 | 课程 14 |
| **React Developer Tools** | Chrome/Firefox 扩展。提供 Components 面板（查看组件树/props/state/hooks 并可实时修改）和 Profiler 面板（性能分析） | 课程 15 |
