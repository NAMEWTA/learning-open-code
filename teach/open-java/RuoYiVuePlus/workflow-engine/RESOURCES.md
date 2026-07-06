# RuoYi-Vue-Plus 工作流模块（Warm-Flow）Resources

## Knowledge

- [官方文档: _Warm-Flow 工作流引擎在线文档_ — Warm-Flow（dromara 社区）](http://warm-flow.cn/)
  引擎的一手资料。理解 `TaskService/InsService/DefService/NodeService/HisTaskService` 的对外 API、`FlowParams`、`SkipType`、节点类型、监听器机制时取用——本项目几乎所有「引擎能力」都来自这里，模块只是封装。

- [官方文档: _Warm-Flow 监听器（Listener）_ — Warm-Flow](http://warm-flow.cn/#/warm-flow/listener)
  讲全局监听器 `GlobalListener` 的 create/start/assignment/finish 四个回调时机。理解本项目 `WorkflowGlobalListener` 为什么能在节点流转时插手「动态办理人、抄送、发事件」时取用。

- [官方文档: _RuoYi-Vue-Plus 官方文档 · 工作流_ — Lion Li 团队](https://plus-doc.dromara.org/#/ruoyi-vue-plus/workflow/workflow)
  本项目自己的工作流使用文档：流程设计、办理人配置、业务接入步骤。理解 `flow_definition` 设计、按钮权限、办理人 storageId、业务模块接入约定时取用。

- [源码: _ruoyi-workflow 模块_ — 本仓库](RuoYi-Vue-Plus/ruoyi-modules/ruoyi-workflow)
  最高信任度的事实来源。重点：`service/impl/FlwTaskServiceImpl.java`（发起+办理核心）、`listener/WorkflowGlobalListener.java`（引擎回调）、`handler/FlowProcessEventHandler.java`（发事件）、`service/impl/TestLeaveServiceImpl.java`（业务接入范例）、`service/impl/WorkflowServiceImpl.java`（对外 API 实现）。

- [源码: _ruoyi-api/workflow 跨模块契约_ — 本仓库](RuoYi-Vue-Plus/ruoyi-api/src/main/java/org/dromara/workflow)
  `WorkflowService` 接口 + `StartProcessDTO/CompleteTaskDTO` + `ProcessEvent/ProcessTaskEvent/ProcessDeleteEvent` 三个事件。理解「业务模块为什么不依赖 workflow 实现也能发起流程、收流程事件」时取用——这是解耦的物理边界。

- [源码: _前端工作流对接（两套 UI）_ — 本仓库](plus-ui-vue/src/api/workflow)
  Vue：`api/workflow/{task,instance,definition,category,spel,leave}`、`components/Process/submitVerify.vue`、`views/workflow/processDefinition/design.vue`。React 同构：`plus-ui-react/src/api/workflow/*`、`components/workflow/SubmitVerify.tsx`。理解前端如何调接口、审批弹窗如何组装参数、设计器如何 iframe 嵌入时取用。

- [文章: _Spring `@EventListener` 与 `ApplicationEventPublisher`_ — Spring 官方文档](https://docs.spring.io/spring-framework/reference/core/beans/context-introduction.html#context-functionality-events-annotation)
  理解本项目「引擎事件 → `SpringUtils.context().publishEvent()` → 业务 `@EventListener(condition=...)`」这条解耦链时取用。SpEL `condition` 的写法（如 `#processEvent.flowCode.startsWith('leave')`）也出自这里。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus QQ 群与 Issues_ — Gitee/GitHub](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「这个流程行为是 bug 还是设计如此」「我的业务该怎么接入」这类需要他人经验的问题时，在 Issues 搜索或提问。Warm-Flow 本身也在 Dromara 社区，引擎层问题可直接找 Warm-Flow 仓库。

## Gaps
- 暂无。所有 Success 项均有对应的一手资料或仓库源码支撑；引擎内部算法明确列为 Out of scope。
