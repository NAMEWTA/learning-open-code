# 使命：Web UI 交互全链路——Streamlit 前端到分析完成

## 为什么
已掌握 Web 模块各文件的独立职责（L1 module-web），现在需要将它们串联成完整的请求-响应链路。理解用户一次点击"开始分析"后，数据如何在 sidebar → app.py 状态机 → runner 后台线程 → ProgressTracker → 前端组件之间流转，才能对 Streamlit 单进程架构下的异步任务编排形成直觉，进而能够独立定制或调试这类交互式分析 UI。

## 成功的样子
- 能画出从 ticker 输入到报告展示的完整 6 阶段交互链路图，标注每个阶段的线程归属
- 能说出 app.py 5 状态机的每个状态的进入条件和退出条件
- 能解释后台线程如何通过 graph.stream() chunk 逐块检测阶段完成并更新 ProgressTracker
- 能描述暂停/恢复/停止的信号传递路径（UI → Event/Lock → 后台线程 → 清理动作）
- 能走通 PDF/Markdown 导出的两条路径及其降级策略

## 约束条件
- 已学完 L0 项目全景图 + L1 module-web 模块总览
- 15 分钟短课合约，每节 ≤1500 中文 + ≤4 h2
- 仅覆盖 Web UI 交互链路，不深入 Agent 分析逻辑、数据获取、LangGraph 内部实现

## 不在范围内
- LangGraph 节点内部编排逻辑（见 module-graph、slice-analysis-pipeline）
- Agent 角色分析算法（见 module-agents）
- LLM provider 路由与模型注册（见 module-llm-clients、slice-llm-routing）
- Streamlit 框架自身的组件 API 详解（见 Streamlit 官方文档）
