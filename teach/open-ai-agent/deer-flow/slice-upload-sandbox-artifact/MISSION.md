# 使命：上传文件到 sandbox 再产出 artifact

## 为什么
用户在聊天框附加文件后，需要 agent 能在沙箱里读到内容，工作区侧栏也要能预览同一份文件。排查「上传成功但 agent 读不到」「附件链接 404」「Docker sandbox 权限错误」时，必须知道字节从前端 FormData 一路落到 host uploads 目录、再进入 sandbox 虚拟路径，最后经 artifacts API 回到 UI 的完整链路。

## 成功的样子
- 能按层说出：InputBox → `uploadFiles` → Gateway `upload_files` → `deerflow/uploads/manager` →（可选）`sandbox.update_file` → `artifact_url` → `get_artifact`
- 能解释 `virtual_path`（`/mnt/user-data/uploads/...`）与 `artifact_url` 的对应关系
- 能区分 bind-mount 模式与 `sync_to_sandbox` 模式，并说出至少一条异常路径（413 超限、路径遍历 400、HTML artifact 强制下载）

## 约束条件
- 以 workspace 聊天附件为主路径，不展开 IM channel 收文件或 `present_files` 产出 outputs 的分支
- 单节课 15 分钟内完成，接口表与 chmod 细节查 reference 速查页

## 不在范围内
- `UploadsMiddleware` 如何把文件列表注入 agent 提示（见 lead-agent 模块）
- Office/PDF 自动转 Markdown 的 markitdown 实现细节
- agent 用 `write_file` 生成 outputs 类 artifact 的预览逻辑
