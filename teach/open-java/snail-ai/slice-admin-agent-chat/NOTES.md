# 教学笔记：Admin 智能体流式对话

- 本主题按 L2 垂直切片组织：从 Admin HTTP/SSE 请求进入，穿过 Server 责任链、gRPC 分发、Agent Client 执行，再回到 Server 流式回写和持久化。
- lesson 只讲主路径和关键判断点；reference 承载长表格、边界条件和调试 checklist。
