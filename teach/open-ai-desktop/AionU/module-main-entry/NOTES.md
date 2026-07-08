# 教学笔记：Electron 主入口与生命周期

- 本主题定位为 AionU 桌面端入口导览，重点解释 `packages/desktop/src/index.ts` 如何按 `--version`、backend 启动、resetpass、webui 和 desktop 模式分流。
- 课程正文聚焦启动顺序，reference 承接 CLI 分支、退出收尾和关键依赖清单。
