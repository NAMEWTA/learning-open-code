# 教学笔记：LangGraph 工作流引擎模块

- 学生已通过 L0 课程了解项目 7 阶段 pipeline 的全景，本课程聚焦 graph 包的具体代码实现
- 关键教学难点：conditional_logic 的条件路由在 setup.py 中通过 `getattr(self.conditional_logic, f"should_continue_{analyst_type}")` 动态绑定，需要解释这种设计模式
- Propagator 类非常薄（仅 create_initial_state + get_graph_args），重点在初始状态中 InvestDebateState 和 RiskDebateState 的 TypedDict 结构
- checkpointer 只在 `checkpoint_enabled=True` 时激活，默认关闭——需要说明默认行为与启用后的差异
