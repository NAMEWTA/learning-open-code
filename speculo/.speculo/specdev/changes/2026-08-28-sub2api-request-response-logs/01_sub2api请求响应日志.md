# sub2api-plus 会记录所有模型请求与响应吗？

## 先看全图

```text
[你的应用]
    |
    | 模型请求
    v
[sub2api-plus 中转站]
    |
    +---> [用量记录]
    |       记录：模型名、Token 数、费用、耗时、请求编号等
    |       不记录：正常请求正文、正常回答正文
    |
    +---> [提示词审计：默认关闭]
    |       开启后：可能保存用户提示词原文
    |       不保存：模型正常回答正文
    |
    +---> [错误监控]
    |       失败时：可能保存脱敏、截断后的错误响应摘要
    |
    v
[上游模型] ---> [模型回答] ---> [sub2api-plus] ---> [你的应用]
```

一句话结论：**它不会默认、无条件地保存所有请求正文和所有响应正文。**

不过，“完全不会保存聊天内容”也不准确。管理员如果开启提示词审计，系统可能把用户提示词原文写入数据库；这取决于运行时配置和审计结果。

## 一步一步看

### 第一步：请求先经过中转站

```text
[用户输入]
    |
    v
[认证和基础检查]
    |
    v
[可选的安全审计]
    |
    v
[选择上游账号] -> [发送给模型]
```

为了把请求发给上游模型，程序运行时必然会读到请求内容。但“程序处理过”不等于“永久写入日志”。要判断是否留存，需要分别看下面三套记录。

### 第二步：用量记录只保存账单和运行信息

```text
[一次已处理的模型调用]
    |
    +-- 模型名
    +-- 输入和输出 Token 数
    +-- 费用与倍率
    +-- 耗时和是否完成
    +-- 请求编号、用户、API Key、账号、IP
    |
    v
[usage_logs 表]
```

`usage_logs` 的字段定义位于 `<Path>open-ai-agent/sub2api-plus/backend/ent/schema/usage_log.go</Path>`。其中没有“完整请求正文”或“完整正常响应正文”字段。

它主要服务于计费、统计和排障。它也不能被理解成“所有进入服务器的请求清单”：认证失败、基础校验失败或尚未进入用量结算的请求，不等同于一条正常用量记录；日志写入本身也可能失败。

### 第三步：提示词审计可能保存用户输入原文

```text
[运行时总开关]
    |
    +-- 关闭 ------------------------------> [不做 Prompt Audit]
    |
    +-- 开启
          |
          +-- 不在指定分组 ----------------> [跳过]
          |
          +-- 无可识别的用户提示词 --------> [跳过]
          |
          +-- 识别成功 -> [风险扫描]
                              |
                              +-- 命中风险 -> [保存审计事件和提示词原文]
                              |
                              +-- 正常通过
                                     |
                                     +-- store_pass_events=false -> [不保存事件]
                                     +-- store_pass_events=true  -> [保存事件和提示词原文]
```

代码默认值是：

- `risk_control_enabled=false`；
- Prompt Audit 的 `enabled=false`；
- `store_pass_events=false`。

因此，新部署按默认配置运行时，不会把每条正常提示词都保存为 Prompt Audit 事件。

管理员开启该功能后，审计范围仍不是“原始请求体的完整副本”。系统主要选择用户撰写的提示词；system/developer 指令、模型回复、推理内容、工具定义、工具参数和工具输出等会被排除。无法识别的新结构也可能直接放行。

审计事件中的 `full_prompt` 是**未脱敏的用户提示词文本**，最多保存 65,536 个字符。默认只保留风险结果；如果管理员同时开启 `store_pass_events`，正常通过的提示词也会保存。相关实现位于：

- `<Path>open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_config.go</Path>`；
- `<Path>open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_snapshot.go</Path>`；
- `<Path>open-ai-agent/sub2api-plus/backend/internal/securityaudit/prompt_repository.go</Path>`；
- `<Path>open-ai-agent/sub2api-plus/backend/migrations/182_prompt_audit_full_prompt.sql</Path>`。

异步审计时，待扫描文本还会暂存在 Redis，默认最长 30 分钟；处理完成后程序会删除它。PostgreSQL 的待处理任务行只保存脱敏摘要，最终审计事件才可能保存 `full_prompt`。

### 第四步：正常模型回答没有完整正文日志

```text
[上游正常回答]
    |
    +---> [返回给用户]
    |
    +---> [提取 Token、模型名、耗时等统计]
    |
    X     没有写入“完整正常回答正文”日志表
```

Prompt Audit 检查的是进入中转站的用户提示词，不是上游模型的正常输出。`usage_logs` 也只保存统计字段。因此，从当前代码看，普通成功响应的完整文本不会被这两套机制持久化。

### 第五步：错误响应是一个例外

```text
[上游返回错误]
    |
    v
[去除敏感信息]
    |
    v
[截断长度]
    |
    v
[系统日志或 ops_error_logs]
```

`gateway.log_upstream_error_body` 默认是 `true`，默认最多记录 2,048 字节的上游错误响应摘要。它只针对错误响应，并会经过脱敏与截断；不是对所有正常模型回答做全文存档。配置来源位于 `<Path>open-ai-agent/sub2api-plus/backend/internal/config/config.go</Path>` 和 `<Path>open-ai-agent/sub2api-plus/deploy/config.example.yaml</Path>`。

### 第六步：源码默认值不代表某个线上实例的实际配置

```text
[源码默认值]
    |
    +-- 只能说明新配置默认怎样
    |
    v
[实际部署]
    |
    +-- 管理员可能开启 Prompt Audit
    +-- 管理员可能开启 store_pass_events
    +-- 反向代理或云平台也可能另加访问日志
```

要判断你正在使用的那个实例是否留存提示词，需要在管理员页面 `/admin/prompt-audit` 检查：

1. 风控总开关是否开启；
2. Prompt Audit 是否开启；
3. 生效模式是关闭、异步审计还是同步阻断；
4. `store_pass_events` 是否开启；
5. 审计覆盖全部分组还是指定分组；
6. `prompt_audit_events` 中是否存在带 `full_prompt` 的记录。

仅看客户端的中转地址，无法证明服务端采用了源码默认配置。

## 术语小词典

- **中转站（API 网关）**：接收你的模型请求，再替你选择账号并发给真正的模型服务。
- **正文（Body/Payload）**：请求或响应里真正的内容，例如问题、system 指令和模型回答。
- **附属信息（元数据）**：描述一次调用的信息，例如模型名、时间、Token 数、费用和请求编号。
- **提示词审计（Prompt Audit）**：把用户输入交给安全模型检查，并按配置保存检查事件。
- **脱敏（Redaction）**：把密钥、邮箱、手机号等敏感片段替换或隐藏。
- **截断（Truncation）**：内容过长时只保留前面一部分。
- **运行时配置**：服务器当前真正采用的设置；它可以与源码默认值不同。

## 你现在能复述什么

1. `sub2api-plus` 会记录模型、Token、费用、耗时等用量信息，但用量记录不含完整请求和正常回答正文。
2. Prompt Audit 默认关闭；管理员开启后，风险提示词会保存原文，开启 `store_pass_events` 后正常提示词也可能保存，但它仍不是完整原始请求体。
3. 正常模型回答没有全文持久化机制；上游错误响应摘要默认可能被脱敏、截断后记录。
4. 是否真的留存你的提示词，最终要看所用实例的运行时配置，而不能只看源码默认值。
