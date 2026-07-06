# RuoYi-Vue-Plus 工作流模块（Warm-Flow）Glossary

记录学习者在课程中**真正理解**的核心术语。

## Terms

**Warm-Flow（国产工作流引擎）**：
本项目使用的工作流引擎（org.dromara.warm，版本 1.8.8）。提供 TaskService/InsService/DefService/NodeService/HisTaskService 五个核心 Service 和四张表（flow_definition / flow_instance / flow_task / flow_his_task），通过 warm-flow-mybatis-plus-sb3-starter 集成。
_Avoid_: 「Flowable」「Activiti」（这是不同的工作流引擎，本项目未使用）。

**@ConditionalOnEnable**：
自定义 Spring 条件注解，绑定了 `warm-flow.enabled` 配置属性。标注了此注解的类只在 `warm-flow.enabled=true` 时被 Spring 加载。是 ruoyi-workflow 模块的全局开关。定义在 `common/ConditionalOnEnable.java:26-29`。

**flow_definition（流程定义）**：
Warm-Flow 引擎表，存储设计器画出来的流程模板。关键字段：flow_code（流程编码，如 "leave1"）、flow_name、version、is_publish（是否已发布）。发起流程时通过 flowCode 查到对应的定义。

**flow_instance（流程实例）**：
每次发起流程时创建的一条记录，与业务单据（通过 business_id）一对一绑定。关键字段：business_id、flow_status（BusinessStatusEnum 状态）、definition_id。

**flow_task（待办任务）**：
当前审批流程中正在等待办理的任务。每个审批节点生成一条。关键字段：instance_id、node_code、node_name。任务被办理后移入 flow_his_task。

**flow_his_task（历史任务）**：
已办结的任务记录。关键字段：task_id（原 flow_task.id）、task_status（TaskStatusEnum，如 pass/back/depute/copy）、node_code、target_node_code。

**BusinessStatusEnum（流程业务状态）**：
定义在 `ruoyi-common-core/.../BusinessStatusEnum.java`。描述整个单据所处的审批阶段：draft / waiting / finish / cancel / back / invalid / termination。存在 `flow_instance.flow_status`。提供状态校验方法（checkStartStatus / checkBackStatus 等）防止并发重复操作。

**TaskStatusEnum（任务状态）**：
定义在 `ruoyi-workflow/.../TaskStatusEnum.java`。描述具体的审批动作：pass / back / depute / transfer / sign / sign_off / copy / cancel / invalid / termination / timeout。存在 `flow_his_task.task_status`。

**StartProcessBo（发起流程入参）**：
包含 businessId、flowCode、handler、variables、bizExt 五个字段。前端提交后由 FlwTaskController.startWorkFlow() 接收，转发给 FlwTaskServiceImpl.startWorkFlow()。

**CompleteTaskBo（办理任务入参）**：
包含 taskId、message（审批意见）、messageType（消息类型 1/2/3）、notice、flowCopyList（抄送人）、assigneeMap（弹窗选人）、handler、variables。由 CompleteTaskBo → completeTask → FlowParams → taskService.skip()。

**FlowParams（Warm-Flow 流转参数）**：
Warm-Flow 引擎的核心参数对象，包含 skipType（PASS/REJECT/NONE）、flowStatus、hisStatus、variable、message、handler 等。所有任务操作（办理/驳回/终止/委派/转办/加减签）都通过构建不同的 FlowParams 调引擎 API。

**TaskOperationEnum（任务操作类型）**：
delegateTask（委派）/ transferTask（转办）/ addSignature（加签）/ reductionSignature（减签）。前端通过 `POST /workflow/task/taskOperation/{code}` 调用，后端 FlwTaskServiceImpl.taskOperation() switch 分发。

**TaskAssigneeEnum（办理人类型）**：
USER / ROLE / DEPT / POST / SPEL。在流程设计器里选办理人时，每种类型通过不同的 storageId 前缀编码（如 "role:123"），在引擎分派任务时由 FlwTaskAssigneeServiceImpl 解析查出具体用户。

**FlowProcessEventHandler（流程事件处理器）**：
定义在 `handler/FlowProcessEventHandler.java:24-89`。负责把引擎数据包装成 ProcessEvent / ProcessTaskEvent / ProcessDeleteEvent 三种 Spring 事件，通过 `SpringUtils.context().publishEvent()` 广播。业务模块通过 `@EventListener` 接收。

**ProcessEvent（流程状态事件）**：
跨模块事件 DTO（ruoyi-api），在流程实例状态变化时（完成/退回/撤销/作废/终止）发出。包含 flowCode、businessId、status、nodeCode、params。业务模块按 `@EventListener(condition = "#processEvent.flowCode == 'xxx'")` 过滤接收。

**WorkflowGlobalListener（全局监听器）**：
实现 Warm-Flow 的 `GlobalListener` 接口，在 create/start/assignment/finish 四个引擎回调中完成节点扩展解析、动态办理人处理、事件发布和消息通知。定义在 `listener/WorkflowGlobalListener.java:51-329`。

**WorkflowService（跨模块 API）**：
定义在 `ruoyi-api/.../api/WorkflowService.java`。供其他业务模块调用的工作流服务接口，包含 startWorkFlow / completeTask / startCompleteTask / deleteInstance / getBusinessStatus 等方法。实现类为 WorkflowServiceImpl，底层全部转发给 workflow 模块的内部 Service。

**SpelRuleComponent（SpEL 规则组件）**：
Spring Bean，提供可在流程设计器 SpEL 表达式中引用的方法（如 `selectDeptLeaderById`）。表达式如 `#{@spelRuleComponent.selectDeptLeaderById(initiatorDeptId)}` 可在运行时动态获取部门负责人作为办理人。

**NodeExtVo（节点扩展视图）**：
每个流程节点的 ext（JSON）解析后的对象，包含 buttonPermissions（按钮权限）、copySettings（抄送配置）、variables（节点变量）。前端审批弹窗通过 getTask() 接口拿到这些配置来控制界面。

**FlowInstanceBizExt（实例业务扩展）**：
存在 `flw_instance_biz_ext` 表。记录流程实例的业务展示信息（businessTitle 标题、businessCode 编号），供审批列表显示。与 flow_instance 一对一关联。

## 待收录（课程推进后补全定义）
- 条件网关（condition gateway）、会签/票签语义
- Warm-Flow 的 Skip 数据结构与节点跳转算法

## Rules
- 仅在用户**真正理解**术语后才收录。
- 有自己的观点：当多个词指向同一概念时，选最佳者，其余标为避免使用。
- 使用术语表自身的术语定义新术语。
- 理解加深时在原文上修订。
