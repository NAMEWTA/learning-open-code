# 日历 time block 同步 资源

## 知识

- [Super Productivity 官方文档 — Calendars](https://super-productivity.com/guides/calendars/) — 用户侧日历集成、time block 与 iCal 配置说明。
- [RFC 5545 iCalendar](https://datatracker.ietf.org/doc/html/rfc5545) — iCal 事件字段与 VEVENT 语义，理解 `get-relevant-events-from-ical.ts` 的输入格式。
- [NgRx Effects 文档](https://ngrx.io/guide/effects) — `TimeBlockSyncEffects` 与 `CalendarIntegrationEffects` 的副作用模型。
- 源码测试：`src/app/features/calendar-integration/time-block/time-block-sync.effects.spec.ts` — coalesce、backfill、delete 队列行为。
- 源码测试：`src/app/features/calendar-integration/store/calendar-integration.effects.spec.ts` — auto-import 与 sync window 门控。

## 智慧（社区）

- [Super Productivity GitHub Discussions](https://github.com/super-productivity/super-productivity/discussions) — 日历重复导入、跨设备 deterministic id、time block 限流等议题（如 #7677）。
- [Super Productivity GitHub Issues](https://github.com/super-productivity/super-productivity/issues) — 搜索 `calendar`、`time block`、`iCal` 标签获取真实故障案例。

## 空白

- 各第三方日历插件（Google、CalDAV 等）的私有 API 限流策略无统一公开文档；课程以插件 `definition.timeBlock` 契约为准，具体 HTTP 行为需读 `packages/plugin-dev/*-calendar-provider/`。
