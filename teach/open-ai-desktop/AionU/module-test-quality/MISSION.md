# 使命：AionU 测试质量模块总览

## 为什么
学习者需要在阅读或修改 AionU 代码前，快速判断一个改动应该用哪一层测试证明：Vitest 单元 / DOM、集成测试、Playwright Electron E2E、还是 CI/构建烟测。这个 L1 主题把测试配置、测试目录、CI 闸门和已有业务模块测试证据收拢成一张可复用地图。

## 成功的样子
- 能说清 `vitest.config.ts`、`playwright.config.ts`、`tests/`、`.github/workflows/` 各自负责什么质量边界。
- 能根据改动类型选择最小但足够的验证命令，例如单个 Vitest 文件、指定 E2E spec、覆盖率或 CI 等价检查。
- 能从 reference 查到 Cron、Team Mode、Assistants / Skills 三个业务模块的测试证据入口。
- 能识别当前覆盖率目标与实际硬闸门之间的差异，避免把报告型检查误读成阻断型检查。

## 约束条件
- 本轮只生成 L1 模块总览，一节 15 分钟短课；完整接口、测试矩阵、CI 清单放入 reference。
- 源项目 `open-ai-desktop/AionU` 只读，不运行或修改源项目测试。
- 只写入 `teach/open-ai-desktop/AionU/module-test-quality/`，不更新项目级进度、索引或其他 worker 的目录。

## 不在范围内
- 不补写 AionU 源码测试，不修复 CI，不调整 coverage threshold。
- 不对每个业务测试逐行讲解；本主题只建立测试质量系统的导航和判断方法。
