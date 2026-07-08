# 使命：一次聊天消息的流式执行

## 为什么
用户在 DeerFlow 工作区发送一条消息后，界面会立刻出现流式回复。要调试「消息发不出去」「流式卡住」「停止无效」等问题，必须知道请求从前端输入框一路穿过 Gateway、RunManager、StreamBridge 到 lead agent 的完整路径。

## 成功的样子
- 能按层说出：ChatPage → useThreadStream → LangGraph SDK → thread_runs.stream → start_run → run_agent → make_lead_agent
- 能读懂 SSE 事件类型（metadata、values、messages-tuple、end）与 UI 状态的对应关系
- 能解释至少一条异常路径（例如并发 run 返回 409、客户端断开触发 cancel）

## 约束条件
- 以浏览器工作区聊天为主路径，不展开 IM channel 或定时任务变体
- 单节课 15 分钟内完成，细节查 reference 速查页

## 不在范围内
- 子 agent task 流、goal continuation 隐藏续跑
- 文件上传与 regenerate 的完整分支（仅在本切片中标注分叉点）
