# 课程快照：module-packages

## 源项目信息
- **源仓库**：`open-ai-desktop/openhanako`
  - **Git Commit**：`acb1b2b860d0d877a9ba57b9022347643e892b1c`
  - **短 Commit**：`acb1b2b`
  - **分支**：`main`
- **快照时间**：2026-07-07T13:21:57+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `packages/plugin-protocol/src/index.ts` | 共享协议常量、PluginUiMessage 消息格式、资源类型、错误码体系、验证函数 | 🔴 核心 |
| `packages/plugin-sdk/src/index.ts` | WebView/iframe 端 SDK：postMessage 通信、资产/API URL 生成、主题同步、单例模式 | 🔴 核心 |
| `packages/plugin-runtime/src/index.ts` | Node 端运行时：definePlugin 生命周期、defineTool/defineCommand/defineProvider、EventBus、Session/Agent/Media/Task API、ResourceIO、用量追踪 | 🔴 核心 |
| `packages/plugin-components/src/index.ts` | 组件库 barrel 导出 | 🔴 核心 |
| `packages/plugin-components/src/theme.tsx` | HanaThemeProvider、10 套内置主题、CSS 变量令牌系统、themeStyleFor | 🔴 核心 |
| `packages/plugin-components/src/controls.tsx` | Button/IconButton/TextInput/Textarea/Switch/Select 表单控件 | 🟡 辅助 |
| `packages/plugin-components/src/layout.tsx` | CardShell/SettingRow/EmptyState/List 布局组件 | 🟡 辅助 |
| `packages/plugin-components/src/classnames.ts` | cx() CSS 类名拼接工具 | 🟢 参考 |
| `examples/plugins/sdk-showcase/manifest.json` | 示例插件 manifest 声明（hostCapabilities、contributes page/widget） | 🟡 辅助 |
| `examples/plugins/sdk-showcase/index.js` | 示例插件生命周期（definePlugin、defineBusHandler、requestBus） | 🟡 辅助 |

## 已生成课程

（暂无课程）

## 参考资料

| 编号 | 参考文件 | 描述 |
|------|---------|------|
| 01 | `reference/packages-overview.html` | 四包架构总览、协议定义、SDK API 完整清单、运行时 helpers 分类表、组件库与主题系统、完整开发示例 |

## 快照摘要
- 课程数：0
- 引用源文件数：10
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
