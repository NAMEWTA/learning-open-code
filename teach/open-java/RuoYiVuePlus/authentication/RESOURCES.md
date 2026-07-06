# RuoYi-Vue-Plus 全栈登录鉴权 Resources

> 本仓库已逐文件核对，**第一信任源是仓库代码本身**。以下外部资源用于补充框架原理与官方约定。

## Knowledge

- [官方文档: _Sa-Token 官方文档_ — click33（dev33.cn）](https://sa-token.cc/)
  认证授权框架的权威说明。需要理解 `StpUtil.login` / `StpInterface` / JWT 整合 / 注解鉴权 / Token-Session 时查阅。本项目认证内核全部建立在它之上。
- [官方文档: _RuoYi-Vue-Plus 官方文档_ — Lion Li（plus-doc）](https://plus-doc.dromara.org/)
  本项目的设计说明，含「客户端管理」「认证授权」「多租户」等章节。理解 sys_client、grantType、加解密设计意图时查阅。
- [代码: _AuthController / IAuthStrategy / *AuthStrategy_](RuoYi-Vue-Plus/ruoyi-admin/src/main/java/org/dromara/web/)
  登录链路第一现场。任何关于「登录怎么走」的问题，最终答案在这里。
- [官方文档: _JustAuth 文档_ — （justauth.cn）](https://www.justauth.cn/)
  第三方社交登录（OAuth2）的统一封装库。理解 `AuthRequest` / `AuthCallback` / social 回调时查阅。
- [官方文档: _JWT 介绍_ — （jwt.io）](https://jwt.io/introduction)
  理解 Sa-Token「JWT 简单模式」里 token 本身结构（header.payload.signature）时查阅。

## Wisdom (Communities)

- [社区: _Dromara 开源社区 / RuoYi-Vue-Plus QQ 群与 Gitee Issues_](https://gitee.com/dromara/RuoYi-Vue-Plus)
  遇到「为什么这样设计」「某版本行为变化」时，Issues 和讨论区是最贴近维护者意图的反馈源。

## Gaps
- 暂无显著缺口。所有 Success 项均可由仓库代码 + 上述官方文档支撑。
