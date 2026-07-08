# 移动端应用工程资源

## 知识

- [AionU mobile/package.json](../../../open-ai-desktop/AionU/mobile/package.json)
  本模块最直接的本地入口，确认 Expo Router、React Navigation、SecureStore、axios、Jest 的依赖关系与脚本边界。适用于：先判断 `mobile/` 是什么形态的工程。
- [Expo Router 文档：Introduction](https://docs.expo.dev/router/introduction/)
  官方说明 Expo Router 的文件路由模型和跨平台定位。适用于：理解 `app/_layout.tsx`、`(tabs)`、`Redirect` 与页面入口之间的关系。
- [Expo Router 文档：Notation](https://docs.expo.dev/router/basics/notation/)
  官方说明 `_layout.tsx`、路由分组与文件命名规则。适用于：快速解读 `app/(tabs)/chat`、`app/file-preview.tsx` 这类目录为何能直接成为页面入口。
- [Expo SecureStore 文档](https://docs.expo.dev/versions/latest/sdk/securestore/)
  官方说明安全存储的用途与限制。适用于：理解 `ConnectionContext` 为什么把连接配置和 token 放进 `expo-secure-store`。
- [React Navigation 文档：Drawer Navigator](https://reactnavigation.org/docs/drawer-navigator/)
  官方说明抽屉导航在 React Navigation 中的职责。适用于：理解聊天页和文件页为什么都各自包一层 Drawer。

## 智慧（社区）

- [Expo 社区文档首页](https://docs.expo.dev/)
  当你想把当前源码决策和 Expo 的推荐实践对照时，从这里继续钻到 Router、Camera、SecureStore、构建等专题最稳妥。
- [React Navigation 官方站](https://reactnavigation.org/)
  当你需要判断 Drawer、Tabs、Stack 组合是否符合标准导航模式时，优先回到官方文档而不是二手博客。

## 空白

- 当前仓库内没有专门解释 `mobile/` 与桌面端协议兼容策略的设计文档；这部分只能从 `bridge.ts`、`websocket.ts` 和测试反推。
- `mobile/` 的组件层较多，但本 goal 只做 L1 总览；若后续需要讲聊天渲染、文件浏览器和设置页交互，还需要拆出更细的 L2 课程。
