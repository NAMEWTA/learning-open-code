# 使命：自定义 agent 创建与更新

## 为什么
我想在 DeerFlow 里创建、保存并持续调整自己的自定义 agent，而不是只用默认 lead agent。需要弄清从 workspace UI 到 Gateway REST、再到 harness 工具与磁盘文件的完整链路，以便排查「保存失败」「列表为空」「更新被 409 拒绝」等问题。

## 成功的样子
- 能画出「创建 agent」与「更新 agent」两条主路径，并指出各自经过的前端、Gateway、harness 与存储层文件
- 看到 `agents_api.enabled=false` 或 legacy 布局冲突时，能判断是哪一层返回的错误以及下一步该改配置还是跑迁移脚本
- 知道 bootstrap 向导依赖 `setup_agent` 工具，而 REST 与聊天内自更新分别走 Gateway `agents.py` 与 `update_agent` 工具

## 约束条件
- 以当前 monorepo 子模块源码为准，不依赖未读过的外部博客
- 先掌握 L0 总览与 module-frontend-workspace、module-gateway 模块导览

## 不在范围内
- lead agent middleware 链的完整推理细节（见 module-lead-agent）
- GitHub 事件驱动 agent 绑定（见 module-channels 与 agents `github:` 配置）
