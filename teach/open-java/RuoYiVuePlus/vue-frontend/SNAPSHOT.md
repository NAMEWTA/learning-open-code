# 课程快照：vue-frontend

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
| `&lt;svg-icon icon-class="user" /&gt;  &lt;!-- 引用 src/assets/icons/svg/user.svg --&gt;
&lt;svg-icon icon-class="system" class-name="custom-class" /&gt;` | 课程分析引用 | 🟡 辅助 |
| `.vue` | 课程分析引用 | 🟡 辅助 |
| `// router/index.ts 中的 dynamicRoutes
export const dynamicRoutes: RouteRecordRaw[] = [
  {
    path: '/monitor',
    component: Layout,
    permissions: ['monitor:logininfor:list'], // 需要此权限才可访问
    children: [...]
  }
];` | 课程分析引用 | 🟡 辅助 |
| `// src/directive/index.ts
export default (app: App) => {
  app.directive('copyText', copyText);
  app.directive('hasPermi', hasPermi);
  app.directive('hasRoles', hasRoles);
};` | 课程分析引用 | 🟡 辅助 |
| `// src/utils/api-types.ts
export type AxiosPromise&lt;T = any&gt; = Promise&lt;RuoYiAjaxResult&lt;T&gt;&gt;;

export interface RuoYiAjaxResult&lt;T = any&gt; {
  code: number;
  msg: string;
  data: T;
}` | 课程分析引用 | 🟡 辅助 |
| `// svg-icon.ts
createSvgIconsPlugin({
  iconDirs: [resolve(__dirname, '../../src/assets/icons/svg')],
  symbolId: 'icon-[dir]-[name]'  // 生成 &lt;symbol id="icon-user"&gt;
})` | 课程分析引用 | 🟡 辅助 |
| `auto-imports.d.ts` | 课程分析引用 | 🟡 辅助 |
| `components.d.ts` | 课程分析引用 | 🟡 辅助 |
| `main.ts` | 课程分析引用 | 🟡 辅助 |
| `src/api/types.ts` | 课程分析引用 | 🟡 辅助 |
| `src/assets/icons/svg/` | 课程分析引用 | 🟡 辅助 |
| `src/assets/styles/index.scss` | 课程分析引用 | 🟡 辅助 |
| `src/lang/en_US.ts` | 课程分析引用 | 🟡 辅助 |
| `src/lang/zh_CN.ts` | 课程分析引用 | 🟡 辅助 |
| `src/permission.ts` | 课程分析引用 | 🟡 辅助 |
| `src/plugins/index.ts` | 课程分析引用 | 🟡 辅助 |
| `src/router/index.ts` | 课程分析引用 | 🟡 辅助 |
| `src/store/modules/permission.ts` | 课程分析引用 | 🟡 辅助 |
| `vite.config.ts` | 课程分析引用 | 🟡 辅助 |
| `vite/plugins/index.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01-项目启动与入口架构 | `lessons/01-项目启动与入口架构.html` | 01 项目启动与入口架构 |
| 02-路由系统与动态菜单 | `lessons/02-路由系统与动态菜单.html` | 02 路由系统与动态菜单 |
| 03-Pinia状态管理五模块 | `lessons/03-Pinia状态管理五模块.html` | 03 Pinia 状态管理五模块 |
| 04-Axios封装与接口加密 | `lessons/04-Axios封装与接口加密.html` | 04 Axios 封装与接口加密 |
| 05-布局系统与三导航模式 | `lessons/05-布局系统与三导航模式.html` | 05 布局系统与三导航模式 |
| 06-权限控制三层体系 | `lessons/06-权限控制三层体系.html` | 06 权限控制三层体系 |
| 07-API层与业务模块 | `lessons/07-API层与业务模块.html` | 07 API 层与业务模块 |
| 08-通用组件与自定义指令 | `lessons/08-通用组件与自定义指令.html` | 08 通用组件与自定义指令 |
| 09-组合式函数体系 | `lessons/09-组合式函数体系.html` | 09 组合式函数体系 |
| 10-构建配置与环境管理 | `lessons/10-构建配置与环境管理.html` | 10 构建配置与环境管理 |

## 参考资料

- `reference/01.html`
- `reference/02.html`
- `reference/03.html`
- `reference/04.html`
- `reference/05.html`
- `reference/06.html`
- `reference/07.html`
- `reference/08.html`
- `reference/09.html`
- `reference/10.html`

## 快照摘要
- 课程数：10
- 引用源文件数：20
- 学习记录数：0
- 参考资料数：10
- 资产文件数：0
