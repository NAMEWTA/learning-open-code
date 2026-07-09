# 教学笔记：Web UI 交互全链路

## 教学重点
- 线程归属是关键区分点：哪些代码跑在 Streamlit 主线程、哪些跑在 daemon 后台线程
- 暂停/恢复/停止的状态机转换（running → paused → running 或 running → stop_requested → stopped）是最容易理解偏差的地方
- 强调历史记录的两层设计（已完成 / 未完成）及其与 tracker 状态的对应关系

## 关联课程
- L0: 00-overview/lessons/0001-project-map.html
- L1: module-web/lessons/0001-web-module-tour.html
- L2: slice-analysis-pipeline（分析流水线切片）、slice-cli-flow（CLI 交互切片）

## 后续可扩展
- 如需深入 Streamlit 自定义组件开发，可新增 theme-customization 主题
- 如需对比 CLI vs Web 的交互差异，可新增 cross-interface-comparison 主题
