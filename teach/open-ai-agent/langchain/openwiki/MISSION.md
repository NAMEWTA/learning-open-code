# 使命：OpenWiki 使用指南

## 为什么
用户已安装 OpenWiki，想了解如何用这个 CLI 工具为其代码仓库自动生成并维护文档，以及使用个人知识库功能来管理个人学习笔记和知识源。

## 成功的样子
- 能熟练执行 `openwiki --init` 初始化代码仓库文档
- 知道代码模式与个人模式的区别并能按需切换
- 能配置 AI 提供商（API Key）和模型
- 能通过 `openwiki --update` 更新文档
- 能使用个人模式连接外部数据源（Git 仓库、Gmail、Notion 等）
- 能配置 CI/CD 自动更新文档

## 约束条件
- 用户已通过 `npm install -g openwiki` 完成安装
- 教学重点在"安装后如何使用"，而非安装过程

## 不在范围内
- OpenWiki 源码架构细节
- LangGraph/LangChain 的其他组件
