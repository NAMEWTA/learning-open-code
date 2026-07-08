# 课程快照：module-renderer-core

## 源项目信息
- **源仓库**：`open-ai-desktop/AionU`
  - **Git Commit**：`0ea13fd0136294ab7ff30215b580b0fc028c6f56`
  - **短 Commit**：`0ea13fd`
  - **分支**：`main`
- **快照时间**：2026-07-07T17:10:10+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-desktop/AionU/packages/desktop/src/renderer/main.tsx` | 根挂载、provider 组装与启动闸门 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Router.tsx` | 受保护路由、懒加载页面与重定向 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/components/layout/Layout.tsx` | UI shell、标题栏、侧栏与系统级 hooks 接入 | 🔴 核心 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/services/bootstrapRenderer.ts` | renderer 配置初始化等待 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/AuthContext.tsx` | `AuthProvider` 与 `useAuth` | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/ThemeContext.tsx` | `ThemeProvider` | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/FeedbackContext.tsx` | `FeedbackProvider` | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/LayoutContext.tsx` | `LayoutContext` | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/NavigationHistoryContext.tsx` | `NavigationHistoryProvider` | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/context/ConversationHistoryContext.tsx` | `ConversationHistoryProvider` | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/pages/conversation/Preview/context/PreviewContext.tsx` | `PreviewProvider` 真实来源 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/system/useDeepLink.ts` | 深链导航 hook | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/system/notification/useNotificationClick.ts` | 系统通知点击后的会话跳转 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/system/notification/useBrowserNotification.ts` | 浏览器通知与回跳行为 | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/ui/useConversationShortcuts.ts` | 会话快捷键 hook | 🟡 辅助 |
| `open-ai-desktop/AionU/packages/desktop/src/renderer/hooks/file/useDirectorySelection.tsx` | 目录选择器宿主上下文 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/e2e/specs/navigation.e2e.ts` | 导航主链 E2E 证据 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/renderer/LayoutSiderBrandHome.dom.test.tsx` | 品牌返回逻辑单测证据 | 🟡 辅助 |
| `open-ai-desktop/AionU/tests/unit/renderer/useBrowserNotification.dom.test.tsx` | 浏览器通知单测证据 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-renderer-core-module-tour | `lessons/0001-renderer-core-module-tour.html` | Renderer 核心模块导览短课 |

## 参考资料

- `reference/renderer-core-overview.html` — Renderer 核心与 UI Shell 参考

## 目录背景说明

- `packages/desktop/src/renderer/` 是本主题讨论的 renderer 根目录，但不再作为“引用源文件”条目写入快照。
- `hooks/context/` 与 `hooks/system/` 仅作为分组目录在参考文档中出现；快照里已展开为实际被分析的 `.tsx` / `.ts` 文件。

## 快照摘要
- 课程数：1
- 引用源文件数：19
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
