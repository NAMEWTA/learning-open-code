# 使命：模型工具调用到执行结果回写的垂直切片

## 为什么
理解 Codex 如何将模型输出的 tool_use 转化为真实的 shell 命令执行、文件 patch 应用，并将结果回写给模型继续生成。掌握这条链路后，就能定位工具执行中任何环节的问题——无论是模型调用了不存在的工具、权限策略拒绝了命令、沙箱执行超时，还是结果序列化格式不对导致模型无法理解。

## 成功的样子
- 能画出从模型 FunctionCall 到 ResponseInputItem::FunctionCallOutput 的完整 7 步时序图
- 能说出 ToolRouter、ToolRegistry、ToolOrchestrator 三者的分工与调用关系
- 能解释一次 bash 命令如何经过审批→沙箱选择→exec-server 执行→输出截断→回写 turn context
- 能分析权限拒绝、命令超时、沙箱降级重试三条异常路径的代码位置和处理逻辑

## 约束条件
- 学习者已通过 L1-module-tools-execution 了解 FunctionTool trait、ToolRegistry、exec policy 与 tool outcome 回写机制
- 学习者已通过 L1-module-core-runtime 了解 turn 中的 tool_use 事件处理流程
- 单节课不超过 15 分钟阅读量

## 不在范围内
- 模型端 tool_use 的生成机制（属于模型推理范畴）
- MCP 远程工具的注册与代理细节（属于 L1-module-extensions-skills-mcp）
- TUI 端的审批 UI 渲染细节（属于 L1-module-tui）
- Code mode 下的嵌套工具调用（属于另一个垂直切片）
