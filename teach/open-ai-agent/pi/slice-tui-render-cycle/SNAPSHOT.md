# 课程快照：slice-tui-render-cycle

## 源项目信息
- **源仓库**：`open-ai-agent/pi`
  - **Git Commit**：`2e4ad6a09423002f58b9a5dc2749f7db7929d0f0`
  - **短 Commit**：`2e4ad6a`
  - **分支**：`main`
- **快照时间**：2026-07-07T16:25:11+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `open-ai-agent/pi/packages/coding-agent/docs/tui.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/extensions/built-in-tool-renderer.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/extensions/entry-renderer.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/examples/extensions/message-renderer.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/export-html/tool-renderer.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/src/core/tools/render-utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/streaming-render-debug.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/coding-agent/test/suite/regressions/4167-thinking-toggle-pending-tool-render.test.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/CHANGELOG.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/README.md` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/package.json` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/autocomplete.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/box.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/cancellable-loader.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/editor.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/image.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/input.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/loader.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/markdown.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/select-list.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/settings-list.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/spacer.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/text.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/components/truncated-text.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/editor-component.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/fuzzy.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/index.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/keybindings.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/keys.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/kill-ring.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/native-modifiers.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/stdin-buffer.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/terminal-colors.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/terminal-image.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/terminal.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/tui.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/undo-stack.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/utils.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/src/word-navigation.ts` | 课程分析引用 | 🟡 辅助 |
| `open-ai-agent/pi/packages/tui/test/tui-render.test.ts` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001-flow-map | `lessons/0001-flow-map.html` | TUI 渲染全链路 · 短课 |

## 参考资料

- `reference/tui-render-cycle-flow-map.html` — TUI 渲染全链路 流程速查

## 快照摘要
- 课程数：1
- 引用源文件数：40
- 学习记录数：0
- 参考资料数：1
- 资产文件数：0
