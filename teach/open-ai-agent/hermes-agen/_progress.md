# Hermes Agent · 教学文档生成进度

> 📊 总体进度：9/13 goals done · 69% · L1 阶段收尾（最后 4 个审查中）
> 🕐 最后更新：2026-07-09

## 按层级统计

| 层级 | 完成 | 总数 | 进度 |
|------|------|------|------|
| L0 项目总览 | 1 | 1 | ✅ 100% |
| L1 模块总览 | 8 | 12 | 🔄 最后 4 个审查中 |
| L2 垂直切片 | 0 | - | ⏳ 审查完成后提取 |
| L3 微观 API | 0 | - | ⏳ 待 L2 |
| L4 深度剖析 | 0 | - | ⏳ 待触发 |

## L1 模块完成清单

| # | Goal | 状态 | 审查 |
|---|------|------|------|
| 1 | agent-core — Agent 核心引擎 | ✅ done | conditional_pass |
| 2 | agent-entry — Agent 入口层 | ✅ done | conditional_pass |
| 3 | gateway — 消息网关 | ✅ done | conditional_pass |
| 4 | tools — 工具层 | ✅ done | conditional_pass |
| 5 | skills — 技能系统 | ✅ done | conditional_pass |
| 6 | cli-framework — CLI 框架 | ✅ done | conditional_pass |
| 7 | plugins — 插件系统 | ✅ done | conditional_pass |
| 8 | providers — 模型提供商 | ✅ done | conditional_pass |
| 9 | cron — 定时任务调度 | 🔄 审查中 | — |
| 10 | tui — 终端 UI | 🔄 审查中 | — |
| 11 | acp — Agent Client Protocol | 🔄 审查中 | — |
| 12 | web — Web 仪表盘 | 🔄 审查中 | — |

## 下阶段计划

L1 全部完成后将：
1. 运行覆盖率终检，扫描未被引用的源文件
2. 从 L1 产出提取 L2 垂直切片 goal
3. 生成 L3 微观 API 参考
4. 触发 L4 深度剖析（高复杂度函数）
