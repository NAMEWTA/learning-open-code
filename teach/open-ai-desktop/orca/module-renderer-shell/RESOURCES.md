# Renderer Shell 模块资源

## 知识

- [src/renderer/src/main.tsx](../../../../open-ai-desktop/orca/src/renderer/src/main.tsx)  
  renderer 入口，安装 crash diagnostics，设置主题，挂载 i18n provider、根级错误边界和 `App`。
- [src/renderer/src/App.tsx](../../../../open-ai-desktop/orca/src/renderer/src/App.tsx)  
  应用 shell，总装配页面、modal、窗口 chrome、启动水合、session 持久化、runtime graph 同步和全局事件。
- [src/renderer/src/store/index.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/index.ts)  
  Zustand store 聚合入口，把 repo、worktree、terminal、tabs、settings、runtime status 等 slice 合成 `useAppStore`。
- [src/renderer/src/store/slices/tabs.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/tabs.ts)  
  统一 tab、tab group、split layout 的核心状态机，同时负责 session 水合后的模型修正。
- [src/renderer/src/runtime/sync-runtime-graph.ts](../../../../open-ai-desktop/orca/src/renderer/src/runtime/sync-runtime-graph.ts)  
  把 renderer 中挂载的 terminal panes、tab layout 和 mobile session snapshots 发布给 main runtime。
- [src/renderer/src/hooks/useIpcEvents.ts](../../../../open-ai-desktop/orca/src/renderer/src/hooks/useIpcEvents.ts)  
  renderer 侧集中订阅 main 进程事件，并将事件落到 store 或 UI 反馈。
- [src/renderer/src/hooks/useIpcEvents.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/hooks/useIpcEvents.test.ts)  
  验证 main 侧事件进入 renderer 后会触发正确 store action、toast 或 UI 状态变化。
- [src/renderer/src/runtime/sync-runtime-graph-scheduling.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/runtime/sync-runtime-graph-scheduling.test.ts)  
  验证 runtime graph 同步的帧级合并和 in-flight trailing publish 行为。
- [src/renderer/src/runtime/sync-runtime-graph.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/runtime/sync-runtime-graph.test.ts)  
  验证 runtime graph 与 mobile session tab snapshot 的核心投影逻辑。
- [src/renderer/src/store/slices/tabs.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/tabs.test.ts)  
  验证 tab 创建、激活、关闭、split group、布局修正和 session 水合行为。
- [src/renderer/src/store/slices/store-session-cascades.test.ts](../../../../open-ai-desktop/orca/src/renderer/src/store/slices/store-session-cascades.test.ts)  
  验证 store session 级联和持久化相关不变量。

## 智慧（社区）

- 本主题暂不依赖外部社区资料。理解重点在 Orca 自己的 renderer 状态边界和启动顺序。

## 空白

- `App.tsx` 很大，后续如需逐页学习，应另开专题拆组件树、右侧栏、terminal pane、browser pane 和 editor pane。
