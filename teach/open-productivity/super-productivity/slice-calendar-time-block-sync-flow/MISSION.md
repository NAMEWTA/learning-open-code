# 使命：日历事件导入与插件 time block 写回全链路

## 为什么
读者需要分清 Super Productivity 里三条容易混淆的日历链路：外部日历事件如何被拉取并投影到 Planner/Schedule、何时自动导入成本地任务、以及本地 scheduled task 如何通过插件 API 写回远端日历 time block。掌握后能快速判断“事件没出现”“重复导入”“time block 没写回”“拖拽日历块无效”该查哪一层。

## 成功的样子
- 能画出从 iCal/插件 agenda 到 `calendarEvents$`、再到 Schedule blocked block 的读方向。
- 能判断 auto-import、banner 提示、手动“添加为任务”分别走哪条 effect/service。
- 能解释 `TimeBlockSyncEffects` 何时 upsert/delete，以及 coalesce 队列为何存在。
- 能区分 iCal 只读事件、可写插件事件拖拽、与 task→time block 写回三条边界。

## 约束条件
- 本主题是 L2 垂直切片，首课 15 分钟内完成。
- 源码路径在 SNAPSHOT 中使用源项目内相对路径。
- 只写入 `teach/open-productivity/super-productivity/slice-calendar-time-block-sync-flow/`。

## 不在范围内
- 不展开 Google Calendar / CalDAV 插件 HTTP 细节与 OAuth。
- 不完整讲 Schedule blocked block split 算法（见 `slice-planner-schedule-flow`）。
- 不覆盖 issue provider 通用双向同步（见 `slice-issue-import-sync-flow`）。
