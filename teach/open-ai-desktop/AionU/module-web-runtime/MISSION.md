# 使命：WebHost 与 WebCLI 运行时

## 为什么
用户已经读过 AionU 的桌面主入口、process 基础设施、preload 与 renderer 核心，下一步需要补上“脱离 Electron 窗口后，WebUI 是怎样独立跑起来”的那一段运行时视角。掌握本主题后，用户可以把 `--webui`、独立 `aionui-web`、backend 生命周期、静态资源服务和浏览器启动行为串成一条完整链路，而不是把它们误看成分散脚本。

## 成功的样子
- 能解释 `startWebHost()` 为什么只是组合器，以及 backend 生命周期和静态服务器分别由谁负责
- 能说清 `packages/web-cli/src/index.ts` 如何解析参数、定位资源目录、启动 WebHost，并在首启时补齐管理员密码
- 能从“浏览器能打开但 API 失败”“只想独立启动 WebUI”“需要 resetpass”三类现象反推应该先读哪个源码文件

## 约束条件
- 本轮只做 L1 模块总览，保留 15 分钟短课形态；lesson 只聚焦一条启动主线，长表格与完整接口清单下沉到 `reference/`
- 只允许修改 `teach/open-ai-desktop/AionU/module-web-runtime/`，不修改源项目、不更新项目级进度台账
- 不展开 aioncore Rust 内部实现，也不把 WebUI 登录协议写成单独安全课程

## 不在范围内
- 不讲 Electron main process 如何决定进入 WebUI 模式；那属于 `module-main-entry`
- 不细拆 renderer React 路由和页面壳层；那属于 `module-renderer-core`
- 不把每个 backend 启动异常和 agent 进程注册细节展开成逐条故障考古
