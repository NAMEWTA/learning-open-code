# Resources: React 企业级前端学习资源策展

## 一手资料（最高信任度）

| 资源 | 覆盖内容 | 何时取用 |
|------|---------|---------|
| [React 官方文档](https://react.dev/) | React 核心概念：组件、JSX、state、props、Hook、Effect | **主要学习对象**，所有 React 基础概念以官方文档为准 |
| [UmiJS 官方文档](https://umijs.org/) | 约定式路由、运行时配置、插件体系、构建优化 | 理解 ruoyi-react 的项目骨架和路由机制时 |
| [Zustand 官方文档](https://zustand.docs.pmnd.rs/) | 轻量状态管理：create、store、selector、middleware | 理解 ruoyi-react 的 6 个 store 时 |
| [Ant Design 官方文档](https://ant.design/) | UI 组件 API：Table、Form、Modal、Menu、Layout | 查阅具体组件的 props 和用法时 |
| [ProComponents 官方文档](https://procomponents.ant.design/) | 高级组件：ProLayout、ProTable、ProForm、PageContainer | 理解 BasicLayout 和 CRUD 页面模板时 |
| [TanStack Query 文档](https://tanstack.com/query/latest) | 服务端状态管理：useQuery、useMutation、缓存策略 | 理解 useDict 等 hook 的缓存机制时 |
| [Axios 官方文档](https://axios-http.com/) | HTTP 客户端：拦截器、请求配置、响应处理 | 理解 request.ts 的拦截器链时 |
| [TypeScript 官方手册](https://www.typescriptlang.org/docs/) | 类型系统：interface、泛型、类型推导、工具类型 | 理解 API 类型定义和组件 props 类型时 |

## 代码导航（ruoyi-react 项目内关键文件索引）

### 项目骨架与配置
- `package.json` — 依赖清单，了解所有使用的库和版本
- `config/config.ts` — **UmiJS 核心配置**：路由定义、插件配置、代理设置
- `vite.config.ts` — Vite 构建配置：路径别名、代码分包、代理
- `tsconfig.json` — TypeScript 编译配置
- `.env.development` / `.env.production` — 环境变量

### 应用入口与运行时
- `src/app.tsx` — **UmiJS 运行时配置**：全局初始化（getInitialState）、根容器包装（QueryClientProvider）
- `src/global.less` — 全局样式
- `src/typings.d.ts` — 全局类型声明

### 布局
- `src/layouts/BasicLayout.tsx` — **主布局组件**（500+ 行）：ProLayout 配置、菜单渲染、用户下拉、标签页

### 路由
- `src/pages/dynamicPage.tsx` — **动态路由核心**：解析后端路由树，匹配并渲染对应页面组件

### 状态管理（6 个 Zustand Store）
- `src/stores/userStore.ts` — 用户信息（昵称、头像、权限）
- `src/stores/appStore.ts` — 布局设置（主题、暗黑模式、语言、组件尺寸）→ 持久化到 localStorage
- `src/stores/permissionStore.ts` — **权限与路由核心**：后端路由树、菜单数据、reloadMenus()
- `src/stores/tagsViewStore.ts` — 多标签页状态（打开、关闭、刷新、拖拽排序）
- `src/stores/dictStore.ts` — 字典数据缓存
- `src/stores/noticeStore.ts` — 实时通知管理

### HTTP 请求层
- `src/api/request.ts` — **Axios 封装核心**：请求/响应拦截器、Token 附加、加密、401 处理、防重复提交
- `src/api/types.ts` — 通用 API 类型：`R<T>` 响应包装、`PageQuery`、`PageResult`、`BackendRoute`
- `src/api/login.ts` — 登录 API
- `src/api/menu.ts` — 路由/菜单 API
- `src/api/system/` — 系统管理 API（user, role, dept, dict, menu, config, notice, post, oss, client）
- `src/api/monitor/` — 监控 API（cache, online, operlog, logininfo）
- `src/api/tool/` — 代码生成器 API

### 认证与持久化
- `src/utils/auth.ts` — Token 存取（localStorage key: `Admin-Token`）
- `src/utils/cookie.ts` — Cookie 工具
- `src/utils/jsencrypt.ts` — RSA 加密（加密 AES 密钥）
- `src/utils/crypto.ts` — AES 加密（加密请求体）

### 自定义 Hook
- `src/hooks/useDict.ts` — 字典数据获取（react-query 缓存）
- `src/hooks/useLoading.ts` — 通用异步加载状态
- `src/hooks/useTableSelection.ts` — 表格行选择
- `src/hooks/useDateRangeQuery.ts` — 日期范围查询
- `src/hooks/useSearchReset.ts` — 搜索表单重置
- `src/hooks/useTableExport.ts` — 表格导出

### 典型页面（学习范本）
- `src/pages/login.tsx` — 登录页：表单提交、加密、Token 存储、跳转
- `src/pages/index.tsx` — 仪表盘：PageContainer、ProCard、echarts 图表
- `src/pages/system/user/index.tsx` — **最佳 CRUD 范本**：ProTable + 搜索 + 新增/编辑弹窗 + 删除 + 导出 + 字典
- `src/pages/system/role/index.tsx` — 角色管理：表格 + 权限树分配
- `src/pages/system/menu/index.tsx` — 菜单管理：树形表格 + 图标选择器
- `src/pages/tool/gen/index.tsx` — 代码生成器：表格 + 预览 + 下载

### 布局子组件
- `src/components/layout/TagsView.tsx` — 多标签页栏
- `src/components/layout/LayoutSettings.tsx` — 布局设置抽屉
- `src/components/layout/MessageBox.tsx` — 消息通知
- `src/components/layout/MenuSearch.tsx` — 菜单搜索
- `src/components/layout/LocaleSelect.tsx` — 语言切换

### 实时推送
- `src/utils/push.ts` — SSE/WebSocket 推送连接管理

## 社区

| 社区 | 链接 | 用途 |
|------|------|------|
| React 中文文档 | https://zh-hans.react.dev/ | React 概念学习中首选 |
| UmiJS GitHub | https://github.com/umijs/umi | Issue 追踪、讨论 |
| Ant Design GitHub | https://github.com/ant-design/ant-design | Issue 追踪 |
| RuoYi-Vue-Plus 官方文档 | https://gitee.com/dromara/RuoYi-Vue-Plus | 项目整体架构理解 |
| React 中文社区 | https://react-china.org/ | 讨论和问题求助 |

## 推荐学习路径

1. **React 基础**（课程 01-03）：JSX → 组件与 Props → State 与 Hook（useState、useEffect、useRef、useCallback、useMemo）
2. **项目骨架**（课程 04-05）：UmiJS 项目结构 → 路由系统 → 布局机制
3. **状态管理**（课程 06-07）：Zustand 核心 → ruoyi-react 的 6 个 Store 详解
4. **HTTP 与持久化**（课程 08-09）：Axios 拦截器链 → Token 认证 → 加密 → 持久化存储
5. **动态路由**（课程 10-11）：后端路由树 → DynamicPage 匹配 → 菜单渲染 → 权限控制
6. **页面组成**（课程 12）：ProTable CRUD → 搜索表单 → 弹窗表单 → 字典与导出
7. **实战与调试**（课程 13-14）：新增 CRUD 页面实战 → 调试技巧 → 从零搭建项目骨架
