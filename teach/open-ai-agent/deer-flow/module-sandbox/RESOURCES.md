# Sandbox 与文件系统资源

## 知识

- `backend/packages/harness/deerflow/sandbox/sandbox.py`
  `Sandbox` 抽象接口，是命令执行、文件读写、目录搜索和二进制下载的公共契约。
- `backend/packages/harness/deerflow/sandbox/sandbox_provider.py`
  provider 单例、acquire/get/release 生命周期和线程安全边界。
- `backend/packages/harness/deerflow/sandbox/local/local_sandbox_provider.py`
  Local provider 的线程级虚拟路径映射、技能目录挂载、LRU cache 与本地模式限制。
- `backend/packages/harness/deerflow/sandbox/tools.py`
  `bash`、`ls`、`glob`、`grep`、`read_file`、`write_file`、`str_replace` 等 agent 可见工具，以及虚拟路径和 host path 的安全校验。
- `backend/packages/harness/deerflow/agents/middlewares/thread_data_middleware.py`
  线程 workspace、uploads、outputs host 路径进入 `ThreadState.thread_data` 的入口。
- `backend/packages/harness/deerflow/sandbox/middleware.py`
  sandbox lazy init、`ThreadState.sandbox` 写回和 tool call 包装逻辑。
- `backend/packages/harness/deerflow/agents/middlewares/sandbox_audit_middleware.py`
  bash 命令风险分类、审计日志、阻断和告警逻辑。
- `backend/packages/harness/deerflow/community/aio_sandbox/`
  AIO Docker/remote sandbox provider 与容器内文件 API 实现。
- `backend/packages/harness/deerflow/community/e2b_sandbox/`
  E2B cloud sandbox provider、`/mnt/user-data` 到 remote home 的映射和输出同步线索。
- `backend/app/gateway/routers/uploads.py`、`backend/app/gateway/routers/artifacts.py`
  用户上传文件进入 uploads 目录、agent 产物从 outputs 目录暴露为 artifact 的 Gateway 边界。
- `backend/tests/test_local_sandbox_virtual_path_contract.py`
  最重要的回归测试：`LocalSandbox` 直接通过公共 `Sandbox` API 也必须接受 `/mnt/user-data/...`。
- `backend/docs/CONFIGURATION.md` 与 `config.example.yaml`
  sandbox provider 选择、`allow_host_bash`、mounts、AIO/E2B 配置和安全提示。

## 智慧（社区）

- 本主题当前以本地源码、配置文档和测试作为主要证据。后续做部署实战时，可补充 DeerFlow 上游 issue/PR 讨论和 AIO sandbox 镜像发布说明。

## 空白

- 未联网核验 AIO sandbox 镜像最新版本和 E2B SDK 当前限制；本轮只依据仓库内源码与文档生成教学内容。
