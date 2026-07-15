# 使命：pi-ai — 多 Provider 统一 LLM API 模块总览

## 为什么
pi-ai 是 Pi Agent Harness 的 LLM API 基础层，屏蔽了 30+ 个服务商的接口差异，让上层 Agent 运行时只需要关心"调哪个模型"，而不需要知道底层是 OpenAI、Anthropic 还是 Google 的 SDK。掌握 pi-ai 的架构，你才能理解 Pi 是如何做到 Provider 无关的，也为后续学习 pi-agent-core 的传输抽象打下基础。

## 成功的样子
- 能一句话说清 pi-ai 在整个 Pi monorepo 中的定位——它是被依赖的基础层，不依赖任何其他 pi 包
- 能列出 pi-ai 对外暴露的全部 exports 子路径和 bin 命令
- 能画出内部分层结构：src/api/（统一接口）→ src/providers/（Provider 适配）→ src/auth/（认证）→ src/utils/（工具）
- 能说出 pi-ai 依赖的 5 大外部 LLM SDK 名称及其对应 Provider

## 约束条件
- 具备 TypeScript/Node.js 编程基础
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读为主，理解架构和设计意图
- 不要求实际运行 pi-ai 或配置 API Key

## 不在范围内
- 各 Provider 的具体 API 实现细节（如 OpenAI Completions 的请求体拼接、流解析）
- OAuth 认证的完整 OAuth 2.0 流程
- 模型元数据自动生成脚本（generate-models.ts）的实现细节
- 图像生成（images）相关代码
