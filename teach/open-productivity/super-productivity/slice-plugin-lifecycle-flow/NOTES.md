# 教学笔记：插件生命周期全链路

- 本主题按 L2 垂直切片组织：从插件可见入口一路追到运行时边界，不做全模块百科。
- 用户明确要求区分 web iframe/plugin bridge、Electron OAuth、Node executor 三条边界。
- 用户明确要求不要把插件初始化和实际 issue sync adapter 懒创建混在一起；reference 中用判断表单独说明。
- `src/assets/community-plugins.json` 是社区插件展示列表，不是运行时自动安装或自动加载机制。
