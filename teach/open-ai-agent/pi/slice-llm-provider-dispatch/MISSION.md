# 使命：多 Provider LLM 统一调度全链路

## 为什么
pi-ai 封装了 35 个 LLM 服务商的差异，但仅仅知道"有哪些 Provider"还不够。我需要深入理解一条 LLM 请求如何从模型发现、Provider 匹配、认证解析、SDK 懒加载到流式响应的完整路径——这是我后续调试 Provider 适配问题、添加自定义 Provider 或理解 Agent 运行时与 LLM 交互机制的必备基础。

## 成功的样子
- 能画出从 builtinModels() 到 streamSimple() 的完整调用时序图，标出每一层的入口函数
- 能解释 lazyStream 为什么能同步返回流而异步执行初始化
- 能说出 resolveProviderAuth 的三种认证来源及其优先级顺序
- 能追踪认证失败时的错误传播路径，并定位到具体的 catch 点

## 约束条件
- 已学完 L1 module-ai 模块总览，了解 pi-ai 的整体分包结构
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读和链路追踪为主，不要求实际运行

## 不在范围内
- 各 Provider 具体 SDK 的 HTTP 请求构造细节（如 OpenAI Completions 的请求体格式）
- OAuth 2.0 完整授权码流程（仅关注 token refresh 的重试机制）
- 图像生成 API（images）的调度链路
- 模型元数据生成脚本（generate-models.ts）的代码生成逻辑
