# IP 质量检测快速参考清单

> 一份精炼的 IP 检测工具与手段速查表，方便快速判断 IP 质量。

---

## 一、仅检测 IP 质量（无使用权限）

以下工具只需 IP 地址即可查询，无需拥有该 IP 的使用权。

### 1. IP2Location

- **地址**：<https://www.ip2location.com/>
- **用途**：确认 IP 的地理位置和 IP 类型（机房/家宽/移动/商业 IP）
- **关键参数**：

  | 参数 | 说明 |
  |------|------|
  | Region | 地区 |
  | Usage Type | 用途类型 |
  | AS Usage Type | AS 用途类型 |
  | ASN | 自治系统号 |

- **严重扣分项**：`Proxy Data` 中显示 **VPN / Abuse** 标记 ❌

---

### 2. IPQS (IP Quality Score)

- **地址**：<https://www.ipqualityscore.com/user/search>
- **用途**：查看 IP 风控情况，该库对 IP 滥用检测嗅觉灵敏，**易误判**
- **注意**：✅ 标记干净的 IP 基本是真干净，但 ⚠️ 标记危险的不一定真危险
- **关键参数**：

  | 参数 | 说明 |
  |------|------|
  | Proxy Status | 代理状态 |
  | VPN Status | VPN 状态 |
  | TOR Status | TOR 状态 |
  | Fraud Score | 欺诈分数 |
  | Recent Abuse | 近期滥用记录 |
  | Bot Activity | 机器人活动 |

---

### 3. Ping0

- **地址**：<https://ping0.cc/>
- **用途**：**仅**用于查看 ASN 所属 和 原生/广播 IP
- **⚠️ 不可信的数据（完全不用看）**：
  - IP 类型
  - ASN 属性
  - 风控值
  - 共享人数
  - 大模型检测信息

> 以上数据均不精确，无参考价值！

---

### 4. IPData

- **地址**：<https://ipdata.co/>
- **用途**：主要查看滥用情况
- **关注栏位**：`Threats` —— 查看有无 `abuse` / `tor` / `proxy` 等标记
- **扣分项**：出现滥用标记 ❌

---

### 5. Scamalytics（IP 欺诈检测）

- **地址**：<https://scamalytics.com/>
- **用途**：查看 IP 滥用/欺诈情况
- **判断逻辑**：
  - 分数低 ≠ 没有滥用
  - 低分不一定好，但**高分基本烂完**
- **严重扣分项**：滥用分值高 ❌

---

### 6. Cloudflare Radar

- **地址**：<https://radar.cloudflare.com/zh-cn>
- **用途**：搜索框输入 ASN，查看人机流量占比
- **影响**：测试结果会大幅度影响 Cloudflare 跳盾情况
- **严重扣分项**：机器人流量占比较高 → 导致 CF 频繁跳盾 ❌

---

## 二、有 IP 使用权时的检测手段

以下检测需要你实际拥有该 IP 的使用权（即能通过该 IP 访问网络）。

### 1. IP 质量检测脚本

```bash
bash <(curl -Ls IP.Check.Place)
```

- **用途**：一站式查看常见库检测结果和流媒体解锁情况
- **关键判断**：**四绿一红铁定机房 IP** —— 指 IP2Location 显示为机房，其他库均为绿色，则该 IP 绝对是机房 IP ⚠️

---

### 2. Google 搜索测试

- **地址**：<https://www.google.com/>
- **方法**：**无痕模式 + 不登录** 访问，随意搜索内容
- **严重** ⚠️：跳出人机验证或被检测到异常流量 → **完全宣告该 IP 死刑，最肮脏！** ❌

---

### 3. Reddit 访问测试

- **方法**：**无痕 + 不登录** 直接访问
- **中等严重**：被禁止访问、要求登录 ❌

---

### 4. YouTube 视频播放测试

- **地址**：<https://www.youtube.com/watch?v=dQw4w9WgXcQ>
- **方法**：**无痕 + 不登录** 打开 YouTube 视频
- ✅ **通过**：可以直接打开播放视频，无需验证
- **中等严重**：不能直接播放视频，跳出验证 ❌

---

### 5. Claude 访问测试

- **地址**：<https://claude.ai/login>
- **方法**：查看是否能打开且不跳验证
- ✅ **优秀**：注册账号无需接码！

---

### 6. ChatGPT 访问测试

- **地址**：<https://chatgpt.com/>
- ✅ **通过**：无需人机验证，无需登录即可对话！

---

## 速查总结

| 严重程度 | 现象 |
|----------|------|
| 🔴 致命 | Google 跳人机验证 / 异常流量检测；IP2Location 显示 VPN/Abuse |
| 🟠 严重 | 滥用分值高；Cloudflare 频繁跳盾；Threats 有滥用标记 |
| 🟡 中等 | Reddit 禁止访问需登录；YouTube 跳验证无法播放 |
| 🟢 优秀 | Claude 注册无需接码；ChatGPT 无需登录可对话；IPQS 标记干净 |
