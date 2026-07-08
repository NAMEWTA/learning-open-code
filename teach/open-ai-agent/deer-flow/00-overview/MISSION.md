# 使命：deer-flow 项目总览与学习地图

## 为什么
用户希望系统掌握 deer-flow 的整体架构、Agent 工作流以及前后端协作方式。这个主题的使命是先建立一张可靠的项目地图，让后续 L1/L2/L3/L4 学习都能挂到同一组入口、边界和源码证据上。

## 成功的样子
- 能用一句话说明 deer-flow 是什么，以及它和普通聊天应用的区别。
- 能从根目录定位 Gateway、agent harness、前端工作区、配置、部署和技能库各自在哪里。
- 能解释一次用户请求大致如何经过前端、Gateway、LangGraph lead agent、tools、sandbox、memory 和 streaming 回到界面。
- 能识别后续应拆出的 L1 模块候选与 L2 垂直切片候选。

## 约束条件
- 本次是批量生成模式，不等待访谈确认，采用自动生成的默认使命。
- lesson 必须是 15 分钟内完成的短课，长清单放入 reference。
- 教学内容基于源项目当前快照 `eb5eb9c5743997ac60cbd8d902e49a44f94120ff`。
- 持久化内容只写入 `teach/open-ai-agent/deer-flow/00-overview/`。

## 不在范围内
- 不逐行讲解 lead agent、中间件、subagent、sandbox 或前端 hooks 的内部实现。
- 不运行 deer-flow 服务、不验证真实模型调用或外部 API 凭据。
- 不替代后续 L1 模块课、L2 垂直切片课、L3 API 参考和 L4 深度剖析。
