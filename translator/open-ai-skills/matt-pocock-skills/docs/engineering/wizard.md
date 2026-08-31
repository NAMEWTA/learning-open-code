## 功能说明

`wizard` 生成一个交互式 bash 脚本，带着一个人一步步走完一个手工流程——接第三方服务、跑一次性的迁移、把项目从状态 A 挪到状态 B。它打开每个 URL、说要点什么、复制什么、捕获回来的东西，写进 `.env` 文件和 GitHub Actions secrets。

[Agent](https://www.aihero.dev/ai-coding-dictionary/agent) 写脚本；它从不运行脚本。你在你自己的机器上运行。所以 wizard 不是一份你照着做的指令清单——它是一个驱动流程、持有状态的程序，而你的部分是点击、粘贴、按回车。

## 何时使用

你可以输入 `/wizard`，Agent 也可以自行调用它。当它撞上一个必须由你执行的步骤——一个它铸造不了的 key、一个它点不了的仪表盘——它为你构建一个 wizard，而不是把指令写进聊天里、任它们滚走。

当阻塞你的下一件事是一趟穿仪表盘的行程时使用它：

| 情况 | wizard 做什么 |
| --- | --- |
| 一个新开发者需要配好六个服务应用才能启动 | 按顺序打开每个仪表盘，捕获 keys，写进 `.env` 和 CI |
| 一次一次性迁移需要在特定顺序里翻开关 | 把不可逆的步骤排在确认闸门后面 |
| 一个项目必须从状态 A 一次性挪到状态 B | 走完过渡，报告它做不到的部分 |
| 你正要把那些步骤写进 README | 改写成可执行版本，它不会那么安静地腐烂 |

不要用它来*决定*要构建什么；那要用 [grill-with-docs](https://aihero.dev/skills-grill-with-docs) 和 [to-spec](https://aihero.dev/skills-to-spec)。

## 前置条件

生成一个不需要前置条件。它写的 wizard 跑在 bash 上，某个阶段要设 GitHub secret 或 variable 时用 `gh`。如果 `gh` 缺失或未认证，那个阶段变成一条警告，收尾总结告诉你该手工设什么，而不是让运行失败。

## 阶段

**阶段**是一个屏幕上的一个聚焦任务。脚本在阶段之间清空终端，所以一个溢出屏幕的阶段会丢掉滚走的那部分。你按依赖顺序编写阶段，设置 `TOTAL_STAGES` 和 `TOTAL_MINUTES`——它们驱动剩余时间显示——把估计做诚实，因为运行它的人会拿你说话算话。

范围界定发生在写一行之前。[skill](https://www.aihero.dev/ai-coding-dictionary/skill) 读仓库而不是冷启动提问：`.env*`、`docker-compose*`、框架配置，以及 `.github/workflows/` 里每个 `secrets.*` / `vars.*` 引用——每一个都是一个 wizard 必须产出的值。然后它把排好序的阶段列表给你确认，之后才把每个阶段映射到人实际走的路径（"Dashboard → Developers → API keys → Reveal test key → copy"）。遇到它不知道的当前 UI，它问你或查文档，而不是编点击。

对每个捕获的值，范围界定定下它落到哪：

| 目的地 | 何时 |
| --- | --- |
| 只 `.env` | 本地开发需要，CI 不需要 |
| GitHub secret | CI 读它，而且它敏感 |
| GitHub variable | CI 读它，而且它公开 |
| `.env` 和 secret 都要 | 本地开发和 CI 都需要 |
| 哪里都不去 | 阶段是纯动作——翻了个开关、升级了个计划 |

## 模板已经解决了 UX

[模板](https://github.com/mattpocock/skills/blob/main/skills/engineering/wizard/template.sh) 发布整套体验：带剩余时间的进度、确认闸门、含 WSL 的跨平台 URL 打开、secrets 的隐藏输入、幂等的 `.env` 增改、`gh secret` / `gh variable` 写入，以及一份它不得不跳过的一切的收尾总结。`STAGES` 标记之上的一切是一个固定库，在每个 wizard 里都相同、从不用手编辑。一致性正是要点。你的工作只是界定流程范围、编写它的阶段。

写 wizard 的 Agent 从不端到端运行它，因为它开浏览器、等人类输入。它改为静态验证：`bash -n`、有则 `shellcheck`，以及一次轨迹检查确认每个值都落在范围界定说的地方，每个 `set_secret` 名字都匹配 CI 里一个真实的 `secrets.*` 引用。据此设定预期——第一次运行是你的，而那次运行就是测试。

## 默认短暂

| 你拥有什么 | 拿脚本怎么办 |
| --- | --- |
| 一次性迁移、个人设置、一次你再也不会重复的过渡 | 存到 scratch 或 `scripts/` 路径，运行，删除 |
| 仓库下一个人也会需要的设置路径 | 提交它并从 README 链接，让他们跑脚本而不是重新问 Agent |

## 常见问题

**我的 API keys 会进模型的上下文吗？**

不会。Agent 写脚本；它不运行脚本。你自己运行脚本，它用隐藏终端输入捕获 key，直接写进 `.env` 或 `gh secret`。Wizard 是一个 CLI，模型没连到它。一条告诫：那只对 wizard 在运行时捕获的值成立。如果你在界定范围时把 key 贴进聊天，它就像任何其他被贴进的文本一样进了 [上下文](https://www.aihero.dev/ai-coding-dictionary/context)。

**我能回去修一个打错的值吗？**

运行中不行。没有后退按钮——阶段只向前跑，第 3 阶段答错意味着 Ctrl-C 重跑。重跑按设计很便宜：任何已经写进 `.env` 的值都被当作默认值提供回来，所以你在答对的那些阶段一路按回车，只重打错的那个。这问题在发布周就出现过，至今没关闭："loved it! One thing though——is there a way to go back and correct what you've entered?"

有一个相关的开放 bug。`ask` 提示里的方向键插入 `^[[D` / `^[[C` 而不是移动光标，因为提示用 `read -r` 而不是 Readline（[issue #741](https://github.com/mattpocock/skills/issues/741)）。退格键可用；方向键不可用。删回到错处，而不是把光标移进去。

**它知道我已完成什么吗？**

部分知道，而且比发布反应假设的少。它在问之前读仓库——你的 `.env` 文件、`docker-compose`、框架配置、CI 里的 `secrets.*` 引用——所以它界定到真正缺失的值，而不是像 README 那样从零开始。它不做的是检查第三方服务。如果一个 key 在你的 `.env` 里，wizard 提供它回来、回车保留它；如果你已经创建了 Stripe 账户但从没保存 key，wizard 照样送你去它的仪表盘。

**它坐在工作流的哪里——grilling 和规格之后？**

不特别在哪。它是独立工具，不是链条步骤。常见的猜测是 `/grill-with-docs → /to-spec → /wizard`，那个顺序没问题，但触发条件是出现了一个手工流程，那可以在任何时刻发生：开始之前、构建中途、或上线很久之后。它还能当发现工具用——范围界定会浮出一项任务的隐藏前置条件，比如你没想到的三把 API keys——在你承诺工作之前。

**它在 Claude Code 之外能用吗？**

工件无条件能用：它是一个纯 bash 脚本，不在乎是哪个 [工具链](https://www.aihero.dev/ai-coding-dictionary/harness) 生成的。skill 本身是模型调用的，所以到处都有列名——在 Claude Code 里输入 `/wizard`，或在 Codex 里输入 `$wizard`，或直接描述你卡住的设置。作为模型调用的，它也避开了 [#693](https://github.com/mattpocock/skills/issues/693)——Claude 的桌面和网页界面会把*用户调用*的 skills 从 [模型](https://www.aihero.dev/ai-coding-dictionary/model) 的列表里丢掉并报告为未安装。

**它不是以前是用户调用的吗？**

确实。它现在是模型调用的，所以 Agent 撞上必须由你执行的步骤时会不请自来地够它。你以前能做的没有一样停摆——模型调用*增加* Agent 的触达，从不移除你的，所以 `/wizard` 表现得和以前一模一样。变的是它退役的失败模式：Agent 在构建中途撞上凭据墙，把六条编号步骤倒进聊天里让你手工照做。

**它以前在 `in-progress/`——现在在哪？**

`engineering/`，自 v1.2 起。它从 beta 分类毕业，现在随插件发布，所以它和其余推广集合一起来，而不是需要单独安装。毕业时它的行为没变。

## 有效的标志

- 在任何脚本存在之前，你看到一份排好序的阶段列表、每个阶段产出的值，并被要求确认。
- 每个 URL 都在那个页面的值被索取之前打开。你从不会被告知粘贴一个你还没被派去取的东西。
- Secrets 盲打输入。没有敏感内容回显进你的滚动历史。
- 每个阶段恰好一屏。任何你还需要的东西都没有滚走。
- Ctrl-C 重跑从你离开的地方接上，把已保存的值作为默认值提供。
- 最后一屏列出它写了什么，并分开列出它做不到、必须由你手工完成的部分。

## 在系统中的位置

`wizard` 是一个随时可取的独立工具，坐在自动化停止、人必须点击的那条线上。它最近的邻居是 [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills)，因为两者都是为了让仓库进入可工作状态——那个配置这套 skills，而 `wizard` 为其他一切生成设置路径。它也和 [implement](https://aihero.dev/skills-implement) 搭配：当一次构建落地一个需要凭据或手工切换的功能时，wizard 就是人的那一半被做完的方式。拿不准此刻哪个 skill 合适时，[ask-matt](https://aihero.dev/skills-ask-matt) 为你路由。
