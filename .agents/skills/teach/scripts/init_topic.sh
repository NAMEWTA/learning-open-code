#!/bin/bash
# ============================================================
# teach skill — 初始化教学主题目录
#
# 用法:
#   scripts/init_topic.sh <teach-project-path> <topic-slug> [--skip-index]
#
# 示例:
#   scripts/init_topic.sh teach/open-java/RuoYiVuePlus permission-model
#   scripts/init_topic.sh teach/open-ai-agent/claude-code plugin-system --skip-index
#
# 功能:
#   1. 创建 teach/<path>/<topic-teach>/ 目录结构
#   2. 生成占位文件 (MISSION.md, RESOURCES.md, NOTES.md, SNAPSHOT.md)
#   3. 创建子目录 (lessons/, reference/, learning-records/, assets/)
#   4. 更新 teach/<path>/index.md（除非指定 --skip-index）
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# --- 参数解析 ---
if [ $# -lt 2 ]; then
    echo "用法: $0 <teach-project-path> <topic-slug> [--skip-index]"
    echo ""
    echo "示例:"
    echo "  $0 teach/open-java/RuoYiVuePlus permission-model"
    echo "  $0 teach/open-ai-agent/claude-code plugin-system"
    exit 1
fi

PROJECT_PATH="$1"
TOPIC_SLUG="$2"
SKIP_INDEX=false
if [ "${3:-}" = "--skip-index" ]; then
    SKIP_INDEX=true
fi

TOPIC_DIR="$WORKSPACE_ROOT/$PROJECT_PATH/$TOPIC_SLUG"

# --- 检查是否已存在 ---
if [ -d "$TOPIC_DIR" ]; then
    echo "❌ 教学主题已存在: $PROJECT_PATH/$TOPIC_SLUG"
    echo "   路径: $TOPIC_DIR"
    exit 1
fi

# --- 创建目录结构 ---
echo "📁 创建教学主题目录..."
mkdir -p "$TOPIC_DIR"/{lessons,reference,learning-records,assets}

# --- 生成 MISSION.md ---
cat > "$TOPIC_DIR/MISSION.md" << 'MISSION_EOF'
# 使命：{主题}

## 为什么
{1-3 句话。用户正在追求的具体的现实世界目标。}

## 成功的样子
- {用户将能够做到的一个具体的、可观察的事情}
- {……}

## 约束条件
- {时间、预算、已有承诺、学习偏好}

## 不在范围内
- {用户明确表示现在不想追求的相邻主题}
MISSION_EOF

# --- 生成 RESOURCES.md ---
cat > "$TOPIC_DIR/RESOURCES.md" << 'RESOURCES_EOF'
# {主题} 资源

## 知识

<!-- 添加高可信度知识来源：书籍、文章、官方文档 -->
<!-- 格式：- [标题](URL) — 一句话说明适用场景 -->

## 智慧（社区）

<!-- 添加用户可以检验技能的高声誉社区 -->
<!-- 格式：- [社区名](URL) — 一句话说明适用于什么 -->

## 空白

<!-- 记录缺失的资源领域，推动未来搜索 -->
RESOURCES_EOF

# --- 生成 NOTES.md ---
cat > "$TOPIC_DIR/NOTES.md" << 'NOTES_EOF'
# 教学笔记：{主题}

<!-- 记录用户偏好、教学注意事项、待办事项等 -->
NOTES_EOF

# --- 生成 SNAPSHOT.md 占位 ---
cat > "$TOPIC_DIR/SNAPSHOT.md" << 'SNAPSHOT_EOF'
# 课程快照：{主题}

> ⚠️ 运行 `scripts/generate_snapshot.py` 填充实际内容。

## 源项目信息
<!-- generate_snapshot.py 将自动填充 -->

## 课程引用的源文件
<!-- generate_snapshot.py 将自动填充 -->

## 已生成课程
<!-- generate_snapshot.py 将自动填充 -->

## 快照摘要
<!-- generate_snapshot.py 将自动填充 -->
SNAPSHOT_EOF

echo "✅ 目录结构已创建: $PROJECT_PATH/$TOPIC_SLUG"
echo "   ├── MISSION.md"
echo "   ├── RESOURCES.md"
echo "   ├── NOTES.md"
echo "   ├── SNAPSHOT.md"
echo "   ├── lessons/"
echo "   ├── reference/"
echo "   ├── learning-records/"
echo "   └── assets/"

# --- 更新 index.md ---
if [ "$SKIP_INDEX" = false ]; then
    INDEX_FILE="$WORKSPACE_ROOT/$PROJECT_PATH/index.md"
    if [ -f "$INDEX_FILE" ]; then
        # 检查是否已有该主题条目
        if grep -q "./$TOPIC_SLUG/" "$INDEX_FILE" 2>/dev/null; then
            echo "⚠️  index.md 中已存在该主题条目，跳过更新"
        else
            # 在「教学主题」表格末尾添加新行
            # 查找最后一个表格行的位置
            NEW_ENTRY="| {主题名称} | \`./$TOPIC_SLUG/\` | {简短描述 ≤ 50 字} |"
            echo "" >> "$INDEX_FILE"
            echo "$NEW_ENTRY" >> "$INDEX_FILE"
            echo "📝 已更新 index.md（请手动填写主题名称和描述）"
        fi
    else
        echo "⚠️  index.md 不存在，跳过索引更新"
    fi
fi

echo ""
echo "🔜 下一步:"
echo "   1. 编辑 $TOPIC_SLUG/MISSION.md — 填写用户的学习目标"
echo "   2. 运行 generate_snapshot.py 填充 SNAPSHOT.md"
echo "   3. 开始设计第一节课"
