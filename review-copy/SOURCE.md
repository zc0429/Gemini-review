# 副本制作记录

- 来源仓库：`zc0429/graduation-project`。
- 用户指定分支：`codex/thesis-final-quality-20261113`。
- 固定来源提交：`34f6ac93fc3c45e43619eda9d4b36866658c29c4`。
- 2026-11-14 读取时，分支头为 `d74c52b555fb16341eba6e5e4af15d1bd9571f63`，比来源提交领先 5 项提交；比较 API 确认来源提交为其祖先。本副本只取固定来源提交。
- GitHub 完整递归树未截断，共 1,385 个 blob，227,076,914 字节。
- 保留 736 个原文件（44,668,636 字节），排除 649 个文件。全部原件先与 GitHub tree 的 blob SHA-1 核验，再对副本逐一核对 SHA-256。完整保留后端 159 文件、前端 96 文件、原有材料 20 文件和实验 11 文件。
- GitHub tarball 按 `.gitattributes` 将 `server/mvnw.cmd` 导出成 CRLF；制作时直接读取原提交 blob 恢复 Git 中的原始 LF 字节，核对 blob SHA-1 后复制。没有编辑脚本内容。
- 正式论文取 `output/thesis/thesis-windows-fonts-43541893783-1/`，而不是更早的 Linux 字体受限预览。开题报告及任务书取无“视觉校正版”后缀的正式 DOCX/PDF。
- 当前论文 Markdown 的 28 处图像引用全部保留；相关目录名中的旧日期是来源标识，不能据此删除现稿仍依赖的图表。同名可编辑源、矢量导出、来源及结构元数据也已保留。
- 补充两份云盘原始 PDF，共 1,576,223 字节；来源文件夹、文件 ID、原名、目标名及 SHA-256 见 `drive-materials.json`。第二份只规范目标文件名中的空格。两份均成功获取，没有缺失项。
- 原始校样图、旧导出及环境日志仅在本副本省略，原仓库和历史成果没有删除。保留的报告仍可能引用已省略的历史文件；请结合 `excluded-files.json` 或来源提交读取。原报告中的字数、页码、测试与审查结论均属于历史记录，本次没有重新评审。
- 未克隆、推送、修改或合并来源仓库任何分支或 PR；没有运行原仓库 Actions、模型或应用测试。
- 新增内容仅为根 README、补充的两份 PDF 和本 `review-copy/` 目录。原有文件内容均保持其固定提交中的原字节。

`source-files.json` 记录每个保留原件，`excluded-files.json` 记录每个未复制文件及理由，`generated-files.json` 记录新增说明与验证脚本。`verification-report.json` 和 `generated-files.json` 本身不列入其自身哈希，避免自引用；其余所有文件均被清单覆盖。核验脚本另检查报告中的总量。

Gemini 兼容性按 Google 官方文档的 GitHub 导入限制核验：单仓库至多 5,000 文件和 100 MB，本副本采用 80 MB 十进制上限；无子模块、LFS 指针、软链接、依赖目录和缓存。PDF 通过解析器、非加密及无 JavaScript 检查；Office 文件通过 ZIP CRC 检查。这是结构与可读性核验，未登录用户 Gemini 账号执行实际导入，不保证 GitHub 连接器会读取每个二进制附件。请从“导入代码”使用仓库 URL；需要单独阅读正式版或学校原件时，可另上传原 PDF/DOCX。

目标公开仓库：[https://github.com/zc0429/Gemini-review](https://github.com/zc0429/Gemini-review)，由用户创建。上传前已通过 GitHub API 确认 `private=false`、仓库为空且当前连接有推送权限。本副本只有一个无父提交的根提交，提交身份采用 GitHub noreply 邮箱；仅向新仓库的 `main` 分支上传。
