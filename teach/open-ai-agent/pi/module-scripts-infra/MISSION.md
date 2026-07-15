# 使命：构建脚本与基础设施模块

## 为什么
Pi 是一个 5 包 monorepo，需要可靠的质量门禁来保证 lockstep 版本同步、npm 发布不引入脏数据和跨平台二进制构建不出错。学习 scripts/ 和 CI/CD 体系，你才能理解一个严肃的 TypeScript monorepo 是如何通过脚本自动化保障工程质量、发布一致性和开发者体验的。

## 成功的样子
- 能按职责给 scripts/ 下 20+ 个脚本分类（检查类、锁文件生成类、发布类、分析类）
- 能解释 `npm run check` 背后的 6 步流水线每一步在做什么
- 能看懂 release.mjs 的 9 步发布流程并说出每一步的防护目的
- 能画出从本地 pre-commit hook → CI → 二进制发布 → npm publish 的完整流水线

## 约束条件
- 具备 TypeScript/Node.js 基础，理解 npm workspaces 概念
- 学习时间碎片化，每节课不超过 15 分钟
- 以源码阅读和流程图理解为主，不要求在本地执行发布脚本

## 不在范围内
- Biome 配置项详解（由 TUI 渲染相关 slice 覆盖）
- tsconfig 的编译细节（由 pi-ai 模块覆盖）
- Bun 运行时内核原理
- npm registry 协议细节
