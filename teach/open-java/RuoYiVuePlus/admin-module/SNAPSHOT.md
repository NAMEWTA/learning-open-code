# 课程快照：admin-module

## 源项目信息
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue-plus`
  - **Git Commit**：`348141427d86fbe39041ffafbc5b26473722cd63`
  - **短 Commit**：`3481414`
  - **分支**：`6.X`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-vue`
  - **Git Commit**：`728fdbfe0eae5b5b4ed186801ea9e96e8365ced7`
  - **短 Commit**：`728fdbf`
  - **分支**：`6.X-Vue`
- **源仓库**：`open-java/RuoYiVuePlus/ruoyi-react`
  - **Git Commit**：`e74984e0e05d8807eda19d0a3f7fb9e23771619d`
  - **短 Commit**：`e74984e`
  - **分支**：`6.X-React`
- **快照时间**：2026-07-06T15:39:54+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `IAuthStrategy.java` | 策略接口与工厂路由、buildLoginParameter | 🔴 核心 |
| `SysLoginService.java` | checkLogin 模板方法、Supplier 回调、buildLoginUser | 🔴 核心 |
| `LoginHelper.java` | 外观模式封装 Sa-Token、fillRequestContext、extra 数据读写 | 🔴 核心 |
| `UserActionListener.java` | SaTokenListener 钩子实现、doLogin/doLogout/doKickout/doReplaced | 🔴 核心 |
| `UserLoginSuccessListener.java` | Spring 事件监听器、在线用户缓存、设备类型 | 🔴 核心 |
| `UserLoginSuccessEvent.java` | Java 17 record 事件对象 | 🟡 辅助 |
| `LoginUser.java` | 用户上下文对象、deviceType 字段、getLoginId() | 🔴 核心 |
| `SocialAuthStrategy.java` | 第三方登录策略、JustAuth 集成 | 🔴 核心 |
| `PasswordAuthStrategy.java` | 密码认证策略、BCrypt + 验证码校验 + Supplier | 🔴 核心 |
| `XcxAuthStrategy.java` | 微信小程序认证策略 | 🟡 辅助 |
| `AuthController.java` | 认证入口控制器、social 绑定/回调接口 | 🟡 辅助 |
| `SysClient.java` / `SysClientVo.java` | 客户端配置数据源 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 01-springboot-startup | `lessons/01-springboot-startup.html` | 第 1 课 · Spring Boot 启动入口与配置全景 |
| 02-strategy-pattern | `lessons/02-strategy-pattern.html` | 第 2 课 · 认证策略工厂 — IAuthStrategy 与路由分发 |
| 03-five-strategies | `lessons/03-five-strategies.html` | 第 3 课 · 五种认证策略深度对比 |
| 04-event-listener | `lessons/04-event-listener.html` | 第 4 课 · 事件监听 — 登录后的副作用处理 |
| 05-device-type | `lessons/05-device-type.html` | 第 5 课 · deviceType 设备类型 — 多端登录隔离机制 |
| 06-social-auth-strategy | `lessons/06-social-auth-strategy.html` | 第 6 课 · SocialAuthStrategy 第三方登录与微信认证接入实战 |
| 07-sa-token-hooks | `lessons/07-sa-token-hooks.html` | 第 7 课 · Sa-Token 钩子机制 — UserActionListener 深度解析 |
| 08-record-event | `lessons/08-record-event.html` | 第 8 课 · Java record 事件对象 — UserLoginSuccessEvent 详解 |
| 09-build-login-parameter | `lessons/09-build-login-parameter.html` | 第 9 课 · buildLoginParameter — Sa-Token 登录参数构建器 |
| 10-supplier-pattern | `lessons/10-supplier-pattern.html` | 第 10 课 · Supplier&lt;Boolean&gt; 延迟执行与模板回调模式 |
| 11-design-patterns | `lessons/11-design-patterns.html` | 第 11 课 · admin-module 认证设计模式全景总结 |
| 12-session-architecture | `lessons/12-session-architecture.html` | 第 12 课 · 会话存储架构 — SaLoginParameter、LoginUser、TokenSession 三者关系 |

## 参考资料

- `reference/01.html`
- `reference/02.html`
- `reference/03.html`
- `reference/04.html`

## 快照摘要
- 课程数：12
- 引用源文件数：12
- 学习记录数：0
- 参考资料数：4
- 资产文件数：0
