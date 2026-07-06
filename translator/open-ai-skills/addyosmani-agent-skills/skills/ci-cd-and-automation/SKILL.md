---
name: ci-cd-and-automation
description: 自动化 CI/CD 流水线设置。适用于搭建或修改构建和部署流水线，自动化质量门禁，在 CI 中配置测试运行器，或建立部署策略。
---

# CI/CD 与自动化

## 概述

自动化质量门禁，确保没有任何变更能在未通过测试、lint、类型检查和构建的情况下到达生产环境。CI/CD 是其他所有技能的强制执行机制 —— 它能捕捉人类和 agent 遗漏的问题，并在每次变更中都一致地执行。

**左移（Shift Left）：** 尽可能在流水线早期发现问题。在 lint 阶段捕获的 bug 修复成本以分钟计；同样的 bug 在生产环境中修复成本以小时计。将检查前移 —— 静态分析在测试之前，测试在 staging 之前，staging 在生产环境之前。

**更快即更安全：** 更小的批次和更频繁的发布降低风险而非增加风险。包含 3 个变更的部署比包含 30 个变更的更容易调试。频繁发布能增强对发布流程本身的信心。

## 适用场景

- 搭建新项目的 CI 流水线
- 添加或修改自动化检查
- 配置部署流水线
- 当某个变更需要触发自动化验证时
- 调试 CI 故障

## 质量门禁流水线

每个变更在合并前都要经过以下门禁：

```
Pull Request 已创建
    │
    ▼
┌─────────────────┐
│   代码规范检查    │  eslint、prettier
│   ↓ 通过         │
│   类型检查        │  tsc --noEmit
│   ↓ 通过         │
│   单元测试        │  jest/vitest
│   ↓ 通过         │
│   构建            │  npm run build
│   ↓ 通过         │
│   集成测试        │  API/DB 测试
│   ↓ 通过         │
│   E2E（可选）     │  Playwright/Cypress
│   ↓ 通过         │
│   安全审计        │  npm audit
│   ↓ 通过         │
│   包体积检查      │  bundlesize 检查
└─────────────────┘
    │
    ▼
  准备就绪，可进行代码审查
```

**任何门禁都不能跳过。** 如果 lint 失败，修复 lint —— 不要禁用规则。如果测试失败，修复代码 —— 不要跳过测试。

## GitHub Actions 配置

### 基础 CI 流水线

```yaml
# .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npx tsc --noEmit

      - name: Test
        run: npm test -- --coverage

      - name: Build
        run: npm run build

      - name: Security audit
        run: npm audit --audit-level=high
```

### 带数据库集成测试

```yaml
  integration:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: testdb
          POSTGRES_USER: ci_user
          POSTGRES_PASSWORD: ${{ secrets.CI_DB_PASSWORD }}
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - run: npm ci
      - name: Run migrations
        run: npx prisma migrate deploy
        env:
          DATABASE_URL: postgresql://ci_user:${{ secrets.CI_DB_PASSWORD }}@localhost:5432/testdb
      - name: Integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://ci_user:${{ secrets.CI_DB_PASSWORD }}@localhost:5432/testdb
```

> **注意：** 即使是仅供 CI 使用的测试数据库，也应使用 GitHub Secrets 存储凭证，而非硬编码值。这能培养良好习惯，并防止在其他上下文中意外重复使用测试凭证。

### E2E 测试

```yaml
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: 'npm'
      - run: npm ci
      - name: Install Playwright
        run: npx playwright install --with-deps chromium
      - name: Build
        run: npm run build
      - name: Run E2E tests
        run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

## 将 CI 失败反馈给 Agent

CI 与 AI agent 结合的威力在于反馈循环。当 CI 失败时：

```
CI 失败
    │
    ▼
复制失败输出
    │
    ▼
将其反馈给 agent：
"CI 流水线失败，错误如下：
[粘贴具体错误]
修复问题并在再次推送前本地验证。"
    │
    ▼
Agent 修复 → 推送 → CI 再次运行
```

**关键模式：**

```
代码规范失败 → Agent 运行 `npm run lint --fix` 并提交
类型错误     → Agent 读取错误位置并修复类型
测试失败     → Agent 遵循 debugging-and-error-recovery 技能
构建错误     → Agent 检查配置和依赖
```

## 部署策略

### 预览部署

每个 PR 获得一个预览部署用于手动测试：

```yaml
# 为 PR 部署预览（Vercel/Netlify 等）
deploy-preview:
  runs-on: ubuntu-latest
  if: github.event_name == 'pull_request'
  steps:
    - uses: actions/checkout@v4
    - name: Deploy preview
      run: npx vercel --token=${{ secrets.VERCEL_TOKEN }}
```

### 功能标志（Feature Flags）

功能标志将部署与发布解耦。将未完成或有风险的功能放在标志后面，以便：

- **在不启用的前提下发布代码。** 提前合并到 main，准备好时再启用。
- **不回滚代码即可回滚功能。** 禁用标志而非回退代码。
- **灰度发布新功能。** 对 1% 用户启用，然后 10%，再 100%。
- **运行 A/B 测试。** 对比有功能和无功能时的行为差异。

```typescript
// 简单的功能标志模式
if (featureFlags.isEnabled('new-checkout-flow', { userId })) {
  return renderNewCheckout();
}
return renderLegacyCheckout();
```

**标志生命周期：** 创建 → 为测试启用 → 灰度 → 全量上线 → 移除标志和死代码。永远存在的标志会变成技术债务 —— 创建时就设定清理日期。

### 分阶段上线

```
PR 合并到 main
    │
    ▼
  Staging 部署（自动）
    │ 手动验证
    ▼
  生产环境部署（手动触发或在 staging 之后自动触发）
    │
    ▼
  监控错误（15 分钟观察窗口）
    │
    ├── 检测到错误 → 回滚
    └── 一切正常 → 完成
```

### 回滚方案

每次部署都应该是可逆的：

```yaml
# 手动回滚工作流
name: Rollback
on:
  workflow_dispatch:
    inputs:
      version:
        description: '要回滚到的版本'
        required: true

jobs:
  rollback:
    runs-on: ubuntu-latest
    steps:
      - name: Rollback deployment
        run: |
          # 部署指定的先前版本
          npx vercel rollback ${{ inputs.version }}
```

## 环境管理

```
.env.example       → 已提交（供开发人员参考的模板）
.env                → 不提交（本地开发）
.env.test           → 已提交（测试环境，无真实密钥）
CI secrets          → 存储在 GitHub Secrets / vault 中
Production secrets  → 存储在部署平台 / vault 中
```

CI 绝不应持有生产环境密钥。为 CI 测试使用独立的密钥。

## CI 之外的自动化

### Dependabot / Renovate

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
    open-pull-requests-limit: 5
```

### 构建值班角色（Build Cop）

指定某人负责保持 CI 绿色。当构建失败时，Build Cop 的职责是修复或回滚 —— 而非由造成失败的人来修复。这能防止在每个人都认为别人会修复时构建持续处于失败状态。

### PR 检查

- **必要审查：** 合并前至少需要 1 个审批
- **必要状态检查：** 合并前 CI 必须通过
- **分支保护：** 禁止对 main 进行 force-push
- **自动合并：** 所有检查通过且已审批时自动合并

## CI 优化

当流水线超过 10 分钟时，按影响大小依次应用以下策略：

```
CI 流水线太慢？
├── 缓存依赖
│   └── 为 node_modules 使用 actions/cache 或 setup-node 的 cache 选项
├── 并行运行任务
│   └── 将 lint、typecheck、test、build 拆分为独立的并行任务
├── 仅运行变更相关的内容
│   └── 使用路径筛选跳过不相关的任务（例如，对于仅文档变更的 PR 跳过 e2e）
├── 使用矩阵构建
│   └── 将测试套件分片到多个 runner 上
├── 优化测试套件
│   └── 将慢速测试从关键路径移除，改为按计划运行
└── 使用更大的 runner
    └── GitHub 托管的大型 runner 或自托管用于 CPU 密集型构建
```

**示例：缓存与并行**
```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: 'npm' }
      - run: npm ci
      - run: npm run lint

  typecheck:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: 'npm' }
      - run: npm ci
      - run: npx tsc --noEmit

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22', cache: 'npm' }
      - run: npm ci
      - run: npm test -- --coverage
```

## 常见借口

| 借口 | 现实 |
|---|---|
| "CI 太慢了" | 优化流水线（参见下方 CI 优化），不要跳过它。一个 5 分钟的流水线能防止数小时的调试。 |
| "这个改动很简单，跳过 CI 吧" | 简单的改动也会破坏构建。而且简单改动的 CI 本来就很快。 |
| "这个测试不稳定，重新运行就行" | 不稳定的测试掩盖了真实 bug，浪费所有人的时间。修复不稳定性。 |
| "我们以后再添加 CI" | 没有 CI 的项目会积累各种破坏状态。从第一天就设置好。 |
| "手动测试就够了" | 手动测试不可扩展且不可重复。尽可能自动化。 |

## 红旗警示

- 项目中没有 CI 流水线
- CI 失败被忽略或静默处理
- 为了让流水线通过而在 CI 中禁用测试
- 生产环境部署前没有 staging 验证
- 没有回滚机制
- 密钥存储在代码或 CI 配置文件中（而非密钥管理器）
- CI 时间过长且未做优化努力

## 验证

设置或修改 CI 之后：

- [ ] 所有质量门禁均已就位（lint、类型、测试、构建、审计）
- [ ] 流水线在每个 PR 和到 main 的推送时运行
- [ ] 失败阻止合并（已配置分支保护）
- [ ] CI 结果反馈到开发循环中
- [ ] 密钥存储在密钥管理器中，而非代码中
- [ ] 部署有回滚机制
- [ ] 流水线测试套件在 10 分钟内运行完毕
