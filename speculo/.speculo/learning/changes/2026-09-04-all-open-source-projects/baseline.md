# 未教学基线：Sub2API Plus

## 采集方式

用户在未查阅项目源码的情况下，基于已有理解回答入口、用途和请求链路问题。以下内容按原意保存，不作为已验证的项目事实。

## 学习者原始回答

> 解决的是将多个不同的大模型厂商的订阅 CodingPlan 转化为可以多人调用的 APIKey，同时收敛了相关的设备指纹等，让上游发现不了是多设备使用。可能的程序入口是/Users/wta/Documents/01-Code/learning-open-code/open-ai-agent/sub2api-plus/backend/cmd /Users/wta/Documents/01-Code/learning-open-code/open-ai-agent/sub2api-plus/frontend/index.html 。不知道会经过哪些模块返回什么结果，我不知道有哪些模块。

## 基线判读

- 已有基础：能描述“上游 Provider → 网关 → 多个调用方”的产品形态，并能指出后端 `backend/cmd` 与前端入口线索。
- 未建立：Go 启动生命周期、Gin 路由、中间件、handler/service/repository 分层、Ent 数据模型、Redis/PostgreSQL 职责、Provider 适配、账户调度/故障转移、流式响应、计费与审计链路。
- 待核实命题：设备指纹、会话绑定与上游身份策略的实际实现和合规边界。教学只解释代码中的合法认证、会话安全和供应商兼容机制，不指导规避上游检测或滥用订阅凭证。
- 基线不降低目标：后续目标仍要求能够独立定位源码、解释因果链路、引用测试证据并完成新情境迁移。
