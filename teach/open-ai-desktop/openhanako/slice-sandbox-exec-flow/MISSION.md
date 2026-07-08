# 使命：安全沙盒命令执行全链路

## 为什么
理解 HanaAgent 如何通过双层沙盒模型（应用层 PathGuard + OS 级 Bubblewrap/Seatbelt/Restricted Token）安全地执行 Agent 发起的任意 Shell 命令，从而评估其安全架构的完整性并在实际开发中正确配置沙盒策略。

## 成功的样子
- 能够画出从 Agent tool_use → exec_command → 命令分类 → PathGuard → OS 沙盒 → 结果回传的完整数据流图
- 能够解释 PathGuard 的 11 级级联判定逻辑和四级访问级别（BLOCKED/READ_ONLY/READ_WRITE/FULL）的含义
- 能够说明三种命令执行路径（Direct/Once/TTY）的选择逻辑和适用场景
- 能够识别 7 种异常路径（路径越权、命令注入、沙盒逃逸、配置保护、超时中断、Shell 不兼容、CWD 失效）的拦截机制

## 约束条件
- 基于实际源码分析，不凭空推演
- 内容适用于 TypeScript/Node.js 开发者
- 不深入 Bubblewrap/Seatbelt 的 OS 内核实现细节

## 不在范围内
- 插件如何注册自定义 exec_command 处理器
- Pi SDK 的工具注册框架内部实现
- LLM 如何生成 exec_command 调用的 prompt engineering
