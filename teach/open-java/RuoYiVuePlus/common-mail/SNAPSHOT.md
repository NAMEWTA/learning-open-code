# 课程快照：common-mail

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
- **快照时间**：2026-07-06T15:39:55+08:00

## 课程引用的源文件

| 源文件路径 | 用途 | 关键度 |
|-----------|------|--------|
| `// ruoyi-workflow/FlwCommonServiceImpl.java:160
case EMAIL_MESSAGE -> MailBuilder.of().to(emails).subject(subject).text(message).send();
case SMS_MESSAGE -> {
    // 短信分支...
}` | 课程分析引用 | 🟡 辅助 |
| `MailBuilder.java:370 — ObjectUtil.clone(account)` | 课程分析引用 | 🟡 辅助 |
| `config/MailConfig.java` | 课程分析引用 | 🟡 辅助 |
| `config/properties/MailProperties.java` | 课程分析引用 | 🟡 辅助 |
| `core/MailBuilder.java` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-admin/src/main/resources/application-dev.yml` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common-core` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common-mail` | 课程分析引用 | 🟡 辅助 |
| `ruoyi-common-sms` | 课程分析引用 | 🟡 辅助 |

## 已生成课程

| 编号 | 课程文件 | 描述 |
|------|---------|------|
| 0001 | `lessons/0001.html` | 第 1 课 · 鸟瞰：三层架构如何封装 Jakarta Mail |
| 0002 | `lessons/0002.html` | 第 2 课 · MailConfig 与 MailProperties：从 yml 到 MailAccount Bean |
| 0003 | `lessons/0003.html` | 第 3 课 · MailBuilder：400 行 Builder 模式的精妙实现与实战 |
| 01-MailBuilder与条件装配 | `lessons/01-MailBuilder与条件装配.html` | 第1课 · MailBuilder与条件装配：三层架构的设计密码 |
| 02-发送链路与实战 | `lessons/02-发送链路与实战.html` | 第2课 · 发送链路与实战：从 of() 到 SMTP 的每一步 |

## 参考资料

- `reference/0001.html`
- `reference/0002.html`
- `reference/0003.html`
- `reference/index.html`

## 快照摘要
- 课程数：5
- 引用源文件数：9
- 学习记录数：0
- 参考资料数：4
- 资产文件数：0
