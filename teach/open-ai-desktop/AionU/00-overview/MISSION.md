# 使命：AionU 项目总览

## 为什么
学习者希望从零建立 AionU 的全局架构地图，后续能沿着入口、模块、垂直切片和关键实现逐层读懂这个 TypeScript / Electron / React 桌面项目。L0 的使命不是解释每个功能细节，而是让后续 L1-L4 课程都有可靠锚点。

## 成功的样子
- 能用一句话说明 AionU 的产品定位和核心运行形态。
- 能区分 Electron main、preload、renderer、WebHost、WebCLI 与 aioncore backend 的职责。
- 能根据顶层目录判断某个功能大概率落在哪个包或源码层。
- 能说出后续最值得拆解的 L1 模块、L2 垂直切片和 L4 深挖主题。

## 约束条件
- 本主题是批量生成模式，不等待额外交互，默认读者具备 TypeScript、Electron、React 基础。
- 每节 lesson 必须是 15 分钟内完成的短课；长表格、完整目录和候选清单放入 reference。
- 所有持久化产出只写入 `teach/open-ai-desktop/AionU/00-overview/`。

## 不在范围内
- 不逐行讲解 aioncore Rust 后端实现。
- 不深入讲解 Team Mode、Cron、ACP、Office 生成等具体功能链路；这些留给后续 L1/L2/L4。
- 不修改源项目 `open-ai-desktop/AionU/` 下任何文件。
