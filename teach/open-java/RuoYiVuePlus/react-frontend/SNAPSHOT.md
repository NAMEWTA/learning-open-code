# 课程快照：react-frontend

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
- **快照时间**：2026-07-06T15:39:56+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `// ruoyi-react 菜单渲染的核心逻辑
{menuData.map((item) => (
  &lt;Menu.Item key={item.path} icon={item.icon}&gt;
    {item.name}
  &lt;/Menu.Item&gt;
))}` | 课程分析引用 | 🟡 辅助 |
| `// src/pages/dynamicPage.tsx
import ReportPage from './report';

const migratedPages = {
  // ... 已有映射
  '@/views/report/index': ReportPage,  // ← 新增这一行
};` | 课程分析引用 | 🟡 辅助 |
| `// src/pages/report/index.tsx
const ReportPage: React.FC = () => {
  return (
    &lt;PageContainer&gt;
      &lt;ProCard title="报表管理"&gt;
        {/* 页面内容 */}
      &lt;/ProCard&gt;
    &lt;/PageContainer&gt;
  );
};
export default ReportPage;` | 课程分析引用 | 🟡 辅助 |
| `@/views/system/user/index` | 课程分析引用 | 🟡 辅助 |
| `app.tsx` | 课程分析引用 | 🟡 辅助 |
| `cat src/.umi/umi.ts` | 课程分析引用 | 🟡 辅助 |
| `import NoticePage from './system/notice';

const migratedPages = {
  // ... 其他映射
  '@/views/system/notice/index': NoticePage,   // ← 添加这行
};` | 课程分析引用 | 🟡 辅助 |
| `import { useDict } from '@/hooks/useDict'` | 课程分析引用 | 🟡 辅助 |
| `pages/login.tsx` | 课程分析引用 | 🟡 辅助 |
| `src/` | 课程分析引用 | 🟡 辅助 |
| `src/pages/` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01-jsx-basics | `lessons/01-jsx-basics.html` | 01 · JSX：React 的模板语言 |
| 02-components-props | `lessons/02-components-props.html` | 02 · 组件与 Props：React 的积木系统 |
| 03-useState-useEffect | `lessons/03-useState-useEffect.html` | 03 · State 与 Hook（上）：useState 和 useEffect |
| 04-hooks-advanced | `lessons/04-hooks-advanced.html` | 04 · Hook（下）：useRef、useMemo、useCallback 与自定义 Hook |
| 05-umijs-skeleton | `lessons/05-umijs-skeleton.html` | 05 · UmiJS 项目骨架：理解 ruoyi-react 的目录与约定 |
| 06-routing-layout | `lessons/06-routing-layout.html` | 06 · 路由系统与布局：ProLayout 如何撑起整个后台 |
| 07-zustand-core | `lessons/07-zustand-core.html` | 07 · Zustand 状态管理（上）：核心概念与模式 |
| 08-zustand-stores | `lessons/08-zustand-stores.html` | 08 · Zustand 状态管理（下）：ruoyi-react 的 6 个 Store 详解 |
| 09-axios-interceptor | `lessons/09-axios-interceptor.html` | 09 · HTTP 请求层：Axios 拦截器链与请求封装 |
| 10-persistence-auth | `lessons/10-persistence-auth.html` | 10 · 持久化：Token 认证、localStorage 与数据留存 |
| 11-dynamic-routes-1 | `lessons/11-dynamic-routes-1.html` | 11 · 动态路由（上）：后端路由树与菜单生成 |
| 12-dynamic-routes-2 | `lessons/12-dynamic-routes-2.html` | 12 · 动态路由（下）：DynamicPage 匹配与权限控制 |
| 13-page-composition | `lessons/13-page-composition.html` | 13 · 页面组成：ProTable CRUD 全流程解剖 |
| 14-add-crud-page | `lessons/14-add-crud-page.html` | 14 · 实战：新增一个完整的 CRUD 页面 |
| 15-debug-build | `lessons/15-debug-build.html` | 15 · 调试技巧与从零搭建项目骨架 |

## 参考资料

- `reference/axios-persistence-cheatsheet.html`
- `reference/dynamic-routing-cheatsheet.html`
- `reference/protable-crud-cheatsheet.html`
- `reference/react-core-cheatsheet.html`
- `reference/zustand-cheatsheet.html`

## 快照摘要
- 课程数：15
- 引用源文件数：11
- 学习记录数：0
- 参考资料数：5
- 资产文件数：0
