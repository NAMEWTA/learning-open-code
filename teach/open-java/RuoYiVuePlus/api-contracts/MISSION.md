# Mission: 读懂 RuoYi-Vue-Plus 的 ruoyi-api 模块——模块间解耦的契约层

## Why
`ruoyi-api` 是整个 RuoYi-Vue-Plus 系统中**最不起眼却最关键的模块**——它只有 1890 行代码、34 个文件、9 个接口、20 个模型类，但它是 11 个模块之间互通的「宪法」。学习者需要理解：当一个模块需要查用户名时，为什么不能直接 `@Autowired SysUserMapper`，而要经过 `ruoyi-api` 定义的一个接口？这套依赖倒置设计为什么能避免「模块循环依赖」？为什么它不仅是 Java SPI，还承载了事件解耦和 DTO 契约的角色？目标是**看懂设计格局**，不是背 API 列表。

## Success looks like
- 能用一句话讲清 `ruoyi-api` 在这个项目里的角色：「它是所有模块的公共契约层——上层模块只依赖接口，不依赖实现；实现模块在运行时注入」
- 能画出 `ruoyi-api` 的包结构树：`system.api`（8 个服务接口 + 模型/DTO）与 `workflow.api`（1 个服务接口 + DTO/事件），并说出两者的设计边界
- 能解释「为什么 `common-core` 不依赖 `ruoyi-api`，但 `common-translation` 依赖它」——并说出这种依赖方向的设计原则
- 能讲清 `UserService` 接口在 `ruoyi-api` 定义、在 `ruoyi-system` 实现、在 `ruoyi-workflow` 和 `common-translation` 消费的完整三方协作链路
- 能讲清 `ConfigService` 为什么既有抽象方法又有 `default` 方法，以及这种「接口默认方法 + 类型转换」模式对消费者的好处
- 能讲清 `LoginUser` / `XcxLoginUser` 的继承关系、`getLoginId()` 方法的设计意图，以及它们为什么放在 api 模块而非 system 模块
- 能讲清 workflow 的事件模型——`ProcessEvent` / `ProcessTaskEvent` / `ProcessDeleteEvent` 三类事件如何通过 Spring `@EventListener` 实现「流程内核与业务逻辑完全解耦」
- 能说出 `StartProcessReturnDTO` 为什么用 Java `record` 而不是 `@Data class`，以及这个选择在项目中的一致性

## Constraints
- 学习者已有 `2026-06-30-teach-ruoyi-auth` 的登录链路知识，可引用 auth 课程中的 `LoginUser`、`grantType`、策略模式等概念
- 目标是「读懂设计格局」，课程以追踪真实代码结构、解释设计动机为主
- 全部讲解基于仓库真实代码，引用具体文件路径与类名
- 交互语言：简体中文
- 每节课短小（几分钟内可完成），有一个具体胜利

## Out of scope
- 每个 Service 接口每个方法的逐行实现细节——讲清「谁定义、谁实现、谁消费」即可
- `ruoyi-common-core` 模块的内部实现（`LoginBody`、`SpringUtils` 等——仅在 api 模型继承/调用它们时提及）
- `ruoyi-modules` 各模块的业务逻辑
- Dubbo RPC 的远程调用原理（本项目单体版使用纯 Spring，不涉及 Dubbo 远程）
- 前端代码
