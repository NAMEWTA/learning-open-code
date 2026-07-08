# 主进程 IPC 边界模块资源

## 知识

- [src/preload/index.ts](../../../../open-ai-desktop/orca/src/preload/index.ts)  
  renderer 可见 API 的唯一集中暴露层，封装 `ipcRenderer.invoke/send/on` 与 `contextBridge.exposeInMainWorld()`。
- [src/main/ipc/register-core-handlers.ts](../../../../open-ai-desktop/orca/src/main/ipc/register-core-handlers.ts)  
  main IPC 总注册入口，负责一次性注册大量 domain handler，并更新当前窗口的 trusted webContents ID。
- [src/main/ipc/pty.ts](../../../../open-ai-desktop/orca/src/main/ipc/pty.ts)  
  终端 IPC 边界，处理 `pty:spawn`、write、resize、kill、renderer delivery、SSH/local/daemon provider 路由。
- [src/main/ipc/filesystem.ts](../../../../open-ai-desktop/orca/src/main/ipc/filesystem.ts)  
  文件与 Git IPC 的主实现文件，当前版本的 `git:*` channel 在这里注册，而不是单独的 `git.ts`。
- [src/main/ipc/mobile.ts](../../../../open-ai-desktop/orca/src/main/ipc/mobile.ts)  
  移动端 pairing、runtime access grant、设备撤销和 WebSocket ready 状态的 IPC handler。
- [src/main/ipc/register-core-handlers.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/register-core-handlers.test.ts)  
  验证总注册只注册一次，但 trusted renderer ID 每次窗口重绑都会更新。
- [src/main/ipc/pty.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/pty.test.ts)  
  验证 PTY 环境注入、daemon 路径、sessionId、renderer delivery 和 provider 路由。
- [src/main/ipc/filesystem.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/filesystem.test.ts)  
  验证 Git IPC 的本地/SSH 分流、commit message 校验和路径校验。
- [src/main/ipc/mobile.test.ts](../../../../open-ai-desktop/orca/src/main/ipc/mobile.test.ts)  
  验证移动端 QR、tailnet 地址优先、runtime access grants 和 revoke 行为。

## 智慧（社区）

- [Electron contextBridge 文档](https://www.electronjs.org/docs/latest/api/context-bridge)  
  用于理解为什么 Orca 通过 preload 暴露受控 API，而不是让 renderer 直接访问 Node 能力。

## 空白

- 本主题以 Orca 仓库内源码和测试为主；不引入通用 IPC 教程的长篇背景，避免冲淡项目边界。
