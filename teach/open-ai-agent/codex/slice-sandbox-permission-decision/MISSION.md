# 使命：Sandbox 与权限 profile 的一次决策链路

## 为什么
理解 Codex 在一次工具调用中如何完成沙箱选择与权限裁决，是掌握其安全模型的核心。开发者需要追踪从 execpolicy 策略引擎到平台沙箱创建的完整数据流，以便在定制权限 profile、排查沙箱故障时能够精准定位问题层级。

## 成功的样子
- 能够画出从工具调用触发到沙箱就绪的完整时序图，说出每层决策的输入输出
- 能够解释 SandboxType 的四种类型（None/MacosSeatbelt/LinuxSeccomp/WindowsRestrictedToken）在什么条件下被选中
- 能够在 3 个源码文件中快速定位 execpolicy 决策、permissions 编译、sandboxing::select_initial 的关键代码

## 约束条件
- 需要已掌握 L1-module-sandbox-config 中的基础概念（sandbox 类型、权限 profile 继承机制、execpolicy 三态决策）
- 单次学习时间控制在 30 分钟以内（2 节 15 分钟短课）

## 不在范围内
- 具体平台沙箱（Seatbelt/Seccomp/Landlock/RestrictedToken）的内核级实现细节
- 网络代理（NetworkProxy）的 MITM 拦截和域名过滤
- 多 Agent 协作下的权限委派策略
