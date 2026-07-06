---
name: security-and-hardening
description: 加固代码以抵御漏洞。适用于处理用户输入、认证、数据存储或外部集成的场景。适用于构建任何接受不可信数据、管理用户会话或与第三方服务交互的功能。
---

# 安全与加固

## 概述

Web 应用的安全优先开发实践。将每个外部输入视为敌意的，将每个密钥视为神圣的，将每个授权检查视为强制性的。安全不是一个阶段——它是施加于每行触及用户数据、认证或外部系统的代码上的约束。

## 适用场景

- 构建任何接受用户输入的功能
- 实现认证或授权
- 存储或传输敏感数据
- 集成外部 API 或服务
- 添加文件上传、Webhook 或回调
- 处理支付或 PII 数据

## 流程：威胁模型优先

脱离威胁模型而附加的安全控制只是猜测。在加固之前，花五分钟以攻击者的角度思考：

1. **绘制信任边界。** 不可信数据在何处进入你的系统？HTTP 请求、表单字段、文件上传、Webhook、第三方 API、消息队列，以及 **LLM 输出**。每个边界都是攻击面。
2. **识别资产。** 什么值得窃取或破坏？凭证、PII、支付数据、管理员操作、资金转移。
3. **在每个边界上运行 STRIDE**——一个快速视角，而非繁琐仪式：

| 威胁 | 提问 | 典型缓解措施 |
|---|---|---|
| **S**poofing（仿冒） | 有人能冒充用户 / 服务吗？ | 认证、签名验证 |
| **T**ampering（篡改） | 数据在传输或静止时能被修改吗？ | 完整性校验、参数化查询、HTTPS |
| **R**epudiation（抵赖） | 操作事后能被否认吗？ | 安全事件的审计日志 |
| **I**nformation disclosure（信息泄露） | 数据可能泄漏吗？ | 加密、字段白名单、通用错误消息 |
| **D**enial of service（拒绝服务） | 系统能被压垮吗？ | 速率限制、输入尺寸上限、超时 |
| **E**levation of privilege（权限提升） | 用户能获得不应有的权限吗？ | 授权检查、最小权限 |

4. **在用例旁边编写滥用案例。** 对于每个功能，问"我会如何滥用它？"——然后将答案作为你的第一个测试。

如果你无法指出一个功能的信任边界，你就还没有准备好去保护它。这对应 OWASP **A04：Insecure Design**——大多数安全事故始于设计阶段，而非代码阶段。

## 三级边界体系

### 总是执行（无例外）

- **在系统边界验证所有外部输入**（API 路由、表单处理器）
- **参数化所有数据库查询**——绝不将用户输入拼接到 SQL 中
- **对输出进行编码**以防止 XSS（使用框架自动转义，不要绕过它）
- **所有外部通信使用 HTTPS**
- **使用 bcrypt/scrypt/argon2 哈希密码**（绝不存储明文）
- **设置安全头**（CSP、HSTS、X-Frame-Options、X-Content-Type-Options）
- **为会话使用 httpOnly、secure、sameSite Cookie**
- **每次发布前运行 `npm audit`**（或等效命令）

### 先询问（需要人类批准）

- 添加新的认证流程或修改认证逻辑
- 存储新类别的敏感数据（PII、支付信息）
- 添加新的外部服务集成
- 更改 CORS 配置
- 添加文件上传处理器
- 修改速率限制或节流策略
- 授予提升的权限或角色

### 禁止执行

- **绝不将密钥提交到版本控制**（API Key、密码、Token）
- **绝不记录敏感数据**（密码、Token、完整信用卡号）
- **绝不将客户端验证作为安全边界来信任**
- **绝不为了方便而禁用安全头**
- **绝不使用 `eval()` 或 `innerHTML`** 处理用户提供的数据
- **绝不将会话存储在客户端可访问的存储中**（localStorage 中的认证 Token）
- **绝不向用户暴露堆栈追踪**或内部错误细节

## OWASP Top 10 防范模式

以下为防范模式，而非排名。2021 版排序见 `references/security-checklist.md` 中的速查表。

### 注入（SQL、NoSQL、OS 命令）

```typescript
// BAD：通过字符串拼接造成的 SQL 注入
const query = `SELECT * FROM users WHERE id = '${userId}'`;

// GOOD：参数化查询
const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);

// GOOD：使用参数化输入的 ORM
const user = await prisma.user.findUnique({ where: { id: userId } });
```

### 认证失效

```typescript
// 密码哈希
import { hash, compare } from 'bcrypt';

const SALT_ROUNDS = 12;
const hashedPassword = await hash(plaintext, SALT_ROUNDS);
const isValid = await compare(plaintext, hashedPassword);

// 会话管理
app.use(session({
  secret: process.env.SESSION_SECRET,  // 来自环境变量，而非代码
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,     // 不可通过 JavaScript 访问
    secure: true,       // 仅 HTTPS
    sameSite: 'lax',    // CSRF 防护
    maxAge: 24 * 60 * 60 * 1000,  // 24 小时
  },
}));
```

### 跨站脚本攻击（XSS）

```typescript
// BAD：将用户输入渲染为 HTML
element.innerHTML = userInput;

// GOOD：使用框架自动转义（React 默认如此）
return <div>{userInput}</div>;

// 如果你必须渲染 HTML，请先消毒
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(userInput);
```

### 访问控制失效

```typescript
// 总是检查授权，而不仅是认证
app.patch('/api/tasks/:id', authenticate, async (req, res) => {
  const task = await taskService.findById(req.params.id);

  // 检查已认证用户是否拥有此资源
  if (task.ownerId !== req.user.id) {
    return res.status(403).json({
      error: { code: 'FORBIDDEN', message: '无权修改此任务' }
    });
  }

  // 继续更新
  const updated = await taskService.update(req.params.id, req.body);
  return res.json(updated);
});
```

### 安全配置错误

```typescript
// 安全头（Express 使用 helmet）
import helmet from 'helmet';
app.use(helmet());

// 内容安全策略
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'"],
    styleSrc: ["'self'", "'unsafe-inline'"],  // 如有可能请收紧
    imgSrc: ["'self'", 'data:', 'https:'],
    connectSrc: ["'self'"],
  },
}));

// CORS — 限制为已知域名
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS?.split(',') || 'http://localhost:3000',
  credentials: true,
}));
```

### 敏感数据暴露

```typescript
// 绝不在 API 响应中返回敏感字段
function sanitizeUser(user: UserRecord): PublicUser {
  const { passwordHash, resetToken, ...publicFields } = user;
  return publicFields;
}

// 使用环境变量存储密钥
const API_KEY = process.env.STRIPE_API_KEY;
if (!API_KEY) throw new Error('STRIPE_API_KEY 未配置');
```

### 服务端请求伪造（SSRF）

任何时候服务端获取一个用户能影响的 URL——Webhook、"从 URL 导入"、图片代理、链接预览——攻击者就可以将其指向内部服务（云元数据、`localhost`、私有 IP）。

```typescript
// BAD：取用户给你的任何 URL
await fetch(req.body.webhookUrl);

// GOOD：白名单协议 + 主机，如果任何解析到的 IP 是私有的则拒绝，禁止重定向
import { lookup } from 'node:dns/promises';
import ipaddr from 'ipaddr.js';

const ALLOWED_HOSTS = new Set(['hooks.example.com']);

async function assertSafeUrl(raw: string): Promise<URL> {
  const url = new URL(raw);
  if (url.protocol !== 'https:') throw new Error('仅限 https');
  if (!ALLOWED_HOSTS.has(url.hostname)) throw new Error('主机不允许');
  // 解析所有记录；单个私有 / 保留地址即失败。
  const addrs = await lookup(url.hostname, { all: true });
  if (addrs.some((a) => ipaddr.parse(a.address).range() !== 'unicast')) {
    throw new Error('私有 / 保留 IP');
  }
  return url;
}

await fetch(await assertSafeUrl(req.body.webhookUrl), { redirect: 'error' });
```

`range() !== 'unicast'` 检查覆盖了 IPv4 和 IPv6 的环回地址、链路本地 `169.254.169.254`（云元数据，#1 SSRF 目标）、私有范围和唯一本地地址范围。

**注意——这仍存在 TOCTOU 竞态差距。** `fetch` 在检查之后会再次解析 DNS，因此使用短 TTL 记录的攻击者可以在验证和连接之间将域名重新绑定到内部 IP。对于高风险面，解析一次并连接到固定的 IP，或者在前端放置过滤 agent（`request-filtering-agent` / `ssrf-req-filter`）。

## 输入验证模式

### 在边界使用 Schema 验证

```typescript
import { z } from 'zod';

const CreateTaskSchema = z.object({
  title: z.string().min(1).max(200).trim(),
  description: z.string().max(2000).optional(),
  priority: z.enum(['low', 'medium', 'high']).default('medium'),
  dueDate: z.string().datetime().optional(),
});

// 在路由处理器中进行验证
app.post('/api/tasks', async (req, res) => {
  const result = CreateTaskSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(422).json({
      error: {
        code: 'VALIDATION_ERROR',
        message: '输入无效',
        details: result.error.flatten(),
      },
    });
  }
  // result.data 现在是类型化和已验证的
  const task = await taskService.create(result.data);
  return res.status(201).json(task);
});
```

### 文件上传安全

```typescript
// 限制文件类型和大小
const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];
const MAX_SIZE = 5 * 1024 * 1024; // 5MB

function validateUpload(file: UploadedFile) {
  if (!ALLOWED_TYPES.includes(file.mimetype)) {
    throw new ValidationError('文件类型不允许');
  }
  if (file.size > MAX_SIZE) {
    throw new ValidationError('文件过大（最大 5MB）');
  }
  // 不要信任文件扩展名——如果至关重要，检查魔数（magic bytes）
}
```

## npm audit 结果分级处理

并非所有审计发现都需要立即处理。使用此决策树：

```
npm audit 报告了一个漏洞
├── 严重级别：critical 或 high
│   ├── 漏洞代码在你的应用中是否可达？
│   │   ├── 是 --> 立即修复（更新、打补丁或替换该依赖）
│   │   └── 否（仅开发依赖、未使用的代码路径）--> 尽快修复，但不阻塞
│   └── 是否有可用的修复版本？
│       ├── 是 --> 更新到已修复的版本
│       └── 否 --> 检查变通方案，考虑替换该依赖，或将其加入白名单并设置复审日期
├── 严重级别：moderate
│   ├── 在生产环境中可达？--> 在下一个发布周期中修复
│   └── 仅开发依赖？--> 方便时修复，加入待办项跟踪
└── 严重级别：low
    └── 跟踪并在常规依赖更新时修复
```

**关键问题：**
- 漏洞函数是否在你的代码路径中实际被调用？
- 该依赖是运行时依赖还是仅开发依赖？
- 考虑你的部署上下文，该漏洞是否可被利用（例如，一个仅限于客户端的应用中的服务端漏洞）？

当你推迟修复时，记录原因并设置复审日期。

### 供应链卫生

`npm audit` 能捕获已知的 CVE；它无法捕获恶意或拼写抢注的包。此外：

- **提交 lockfile** 并在 CI 中使用 `npm ci`（而非 `npm install`）安装——可复现构建，无静默版本漂移。
- **在添加之前评审新依赖**——维护情况、下载量，以及它们是否确实值得引入。每个依赖都是攻击面（OWASP **A06：Vulnerable Components**、**LLM03：Supply Chain**）。
- **警惕陌生包中的 `postinstall` 脚本**——它们在安装时运行任意代码。
- **注意拼写抢注**——`cross-env` vs `crossenv`、`react-dom` vs `reactdom`。

## 速率限制

```typescript
import rateLimit from 'express-rate-limit';

// 通用 API 速率限制
app.use('/api/', rateLimit({
  windowMs: 15 * 60 * 1000, // 15 分钟
  max: 100,                   // 每个窗口 100 次请求
  standardHeaders: true,
  legacyHeaders: false,
}));

// 认证端点更严格的限制
app.use('/api/auth/', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10,  // 每 15 分钟 10 次尝试
}));
```

## 密钥管理

```
.env 文件：
  ├── .env.example  → 已提交（带占位值的模板）
  ├── .env          → 不提交（包含真实密钥）
  └── .env.local    → 不提交（本地覆盖）

.gitignore 必须包含：
  .env
  .env.local
  .env.*.local
  *.pem
  *.key
```

**提交前总是检查：**
```bash
# 检查是否意外暂存了密钥
git diff --cached | grep -i "password\|secret\|api_key\|token"
```

**如果某个密钥被提交过，立即轮换它。** 删除那行代码或重写历史是不够的——假设它到达远端的那一刻就已经泄露。先撤销并重新签发密钥，再从历史中清除它。

## 保护 AI / LLM 功能

如果你的应用调用 LLM——聊天机器人、摘要器、agent、RAG——它继承了一个新的攻击面。对照 [OWASP Top 10 for LLM Applications (2025)](https://genai.owasp.org/llm-top-10/) 进行映射：

- **将所有模型输出视为不可信输入（LLM05：Improper Output Handling）。** 绝不要将 LLM 输出直接传入 `eval`、SQL、Shell、`innerHTML` 或文件路径。像处理原始用户输入一样验证和编码它。
- **假设提示可被劫持（LLM01：Prompt Injection）。** 上下文窗口中的不可信文本——用户消息、获取的网页、PDF——可能携带指令。系统提示不是安全边界；在代码中实施权限，而非在提示中。
- **将密钥和其他用户的数据排除在提示之外（LLM02 / LLM07）。** 上下文中的任何内容都可能被回显。不要将 API Key、跨租户数据或完整系统提示放在模型可以重复的地方。
- **约束工具和 agent 的权限（LLM06：Excessive Agency）。** 将工具范围限制到最小，对破坏性或不可逆操作要求确认，并验证每个工具参数。
- **限制资源消耗（LLM10：Unbounded Consumption）。** 对 Token、请求速率和循环 / 递归深度设置上限，以防止精心构造的输入耗尽成本或挂起系统。
- **隔离检索数据（LLM08：Vector and Embedding Weaknesses）。** 在 RAG 中，将向量存储视为信任边界：按租户分区嵌入，使得一个用户无法检索到另一个用户的数据，并在索引之前验证文档，以防中毒内容操控回答。

```typescript
// BAD：将模型输出当做命令或标记来信任
const sql = await llm.generate(`Write SQL for: ${userQuestion}`);
await db.query(sql);                                   // 任意 SQL 执行
container.innerHTML = await llm.reply(userMessage);   // 存储型 XSS，通过模型注入

// GOOD：模型输出是数据——防御性地解析，然后验证，然后编码
let intent;
try {
  intent = CommandSchema.parse(JSON.parse(await llm.replyJson(userMessage)));
} catch {
  throw new ValidationError('意外的模型输出'); // JSON.parse 或 schema 失败
}
await runAllowlistedAction(intent.action, intent.params);
container.textContent = await llm.reply(userMessage);
```

## 安全评审检查清单

```markdown
### 认证
- [ ] 密码使用 bcrypt/scrypt/argon2 哈希（salt 轮次 ≥ 12）
- [ ] 会话 Token 为 httpOnly、secure、sameSite
- [ ] 登录有速率限制
- [ ] 密码重置 Token 会过期

### 授权
- [ ] 每个端点检查用户权限
- [ ] 用户仅能访问自己的资源
- [ ] 管理员操作需要管理员角色验证

### 输入
- [ ] 所有用户输入在边界进行验证
- [ ] SQL 查询已参数化
- [ ] HTML 输出已编码 / 转义
- [ ] 服务端 URL 获取已白名单化（防止 SSRF 访问内部服务）

### 数据
- [ ] 代码或版本控制中无密钥
- [ ] 敏感字段已从 API 响应中排除
- [ ] PII 在静止状态下已加密（如适用）

### 基础设施
- [ ] 安全头已配置（CSP、HSTS 等）
- [ ] CORS 限制为已知域名
- [ ] 依赖项已审计漏洞
- [ ] 错误消息不暴露内部信息

### 供应链
- [ ] Lockfile 已提交；CI 使用 `npm ci` 安装
- [ ] 新依赖已评审（维护情况、下载量、postinstall 脚本）

### AI / LLM（如适用）
- [ ] 模型输出被视为不可信（不使用 eval/SQL/innerHTML/shell）
- [ ] 密钥和其他用户的数据排除在提示之外
- [ ] 工具 / agent 权限已限定范围；破坏性操作需要确认
```
## 参见

详细的安全检查清单和提交前验证步骤，参见 `references/security-checklist.md`。

## 常见借口

| 借口 | 现实 |
|---|---|
| "这是内部工具，安全不重要" | 内部工具同样会被攻陷。攻击者总是瞄准最薄弱的环节。 |
| "以后再添加安全措施" | 事后安全加固的成本是内置式的 10 倍。现在就添加。 |
| "没人会尝试利用这个漏洞" | 自动化扫描器会找到它。安全靠隐匿不是安全。 |
| "框架会处理安全问题" | 框架提供的是工具，而非保证。你仍需正确使用它们。 |
| "这只是一个原型" | 原型会变成生产环境。从第一天就养成安全习惯。 |
| "威胁建模在这里是过度工程" | 五分钟的"我如何攻击它？"可以防止后续任何控制都无法修复的设计缺陷。 |
| "这只是 LLM 输出，只是文本而已" | 那"文本"可能是一条 SQL 语句、一个 script 标签，或一条 Shell 命令。像对待任何不可信输入一样对待它。 |

## 红旗信号

- 用户输入直接传入数据库查询、Shell 命令或 HTML 渲染
- 源代码或提交历史中存在密钥
- API 端点缺少认证或授权检查
- CORS 配置缺失或使用通配符（`*`）来源
- 认证端点无速率限制
- 堆栈追踪或内部错误暴露给用户
- 依赖项存在已知的严重漏洞
- 服务端获取用户提供的 URL 无白名单（SSRF）
- LLM / 模型输出传入查询、DOM、Shell 或 `eval`
- 密钥、PII 或完整系统提示被放入 LLM 上下文窗口

## 验证

实现安全相关代码后：

- [ ] `npm audit` 无 critical 或 high 漏洞
- [ ] 源代码或 git 历史中无密钥
- [ ] 所有用户输入在系统边界进行了验证
- [ ] 每个受保护的端点均检查了认证和授权
- [ ] 响应中存在安全头（使用浏览器 DevTools 检查）
- [ ] 错误响应不暴露内部细节
- [ ] 认证端点激活了速率限制
- [ ] 服务端 URL 获取已对照白名单验证（无 SSRF）
- [ ] LLM / 模型输出在使用前已验证和编码（如果存在 AI 功能）
