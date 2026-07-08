# 上传 → sandbox → artifact 资源

## 知识

- `open-ai-agent/deer-flow/backend/docs/FILE_UPLOAD.md` — 上传 API、虚拟路径、`artifact_url` 字段语义与存储布局
- `open-ai-agent/deer-flow/backend/docs/PATH_EXAMPLES.md` — `/mnt/user-data/{workspace,uploads,outputs}` 与物理目录映射
- `open-ai-agent/deer-flow/frontend/AGENTS.md` — Data Flow 中 thread hooks 负责「先上传再 submit」的说明
- `open-ai-agent/deer-flow/backend/AGENTS.md` — Gateway Uploads / Artifacts 路由表与 sandbox chmod 设计摘要

## 智慧（社区）

- [DeerFlow Issues](https://github.com/bytedance/deer-flow/issues) — 搜索 `upload`、`artifact`、`sandbox` 可找到权限与预览相关故障案例
- [DeerFlow Discussions](https://github.com/bytedance/deer-flow/discussions) — 部署模式下 bind-mount 与 AIO sandbox 行为差异

## 空白

- 暂无专门讲解「upload artifact_url 与 workspace 预览组件」的中文教程；本仓库 `teach/` 切片与 L1 模块文档填补此缺口
