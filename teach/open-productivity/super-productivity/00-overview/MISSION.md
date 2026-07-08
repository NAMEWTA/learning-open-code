# 使命：super-productivity 项目整体架构总览

## 为什么
学习者希望从 0 到 1 建立 super-productivity 的全局源码地图，之后能在 Angular、NgRx、Electron、Capacitor、同步与插件系统之间快速定位代码，不被多端工程和大量 feature 目录淹没。

## 成功的样子
- 能用一句话说明产品定位和主要技术栈。
- 能从 `src/main.ts`、`src/app/app.routes.ts`、`electron/start-app.ts` 判断 Web、桌面、移动端的启动边界。
- 能把后续深入学习拆成清晰的 L1 模块和 L2 垂直切片。
- 能说明哪些大体积资产、生成物、测试固件暂不纳入源码教学覆盖。

## 约束条件
- 本主题是批量生成模式，不等待交互确认。
- 每节 lesson 必须保持 15 分钟内可完成，长表格和索引放入 reference。
- 所有持久化产物只写入 `teach/open-productivity/super-productivity/00-overview/`。

## 不在范围内
- 不逐文件讲解全部 feature、effect、selector 和组件实现。
- 不运行完整构建、端到端测试或移动端打包。
- 不把 Electron、Capacitor、SuperSync 或插件系统的深层实现提前塞进 L0。
