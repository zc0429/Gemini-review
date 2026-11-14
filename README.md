# Gemini 独立审查副本

审查仓库：[zc0429/Gemini-review](https://github.com/zc0429/Gemini-review)。

来源：[zc0429/graduation-project](https://github.com/zc0429/graduation-project)，分支 `codex/thesis-final-quality-20261113`，固定提交 [`34f6ac93fc3c45e43619eda9d4b36866658c29c4`](https://github.com/zc0429/graduation-project/commit/34f6ac93fc3c45e43619eda9d4b36866658c29c4)。该分支已继续推进，本副本不包含后续提交；新仓库从单个根提交开始，不继承旧 Git 历史。

本次仅整理审查材料，没有修改或审查论文、业务代码、学校原件和验证证据，也没有修改、合并原仓库分支或 PR。

| 目录 | 内容 |
| --- | --- |
| `server/`、`web/` | 完整前后端源码、接口、SQL 数据库设计、配置示例及全部已有测试 |
| `docs/thesis/毕业论文.md` | 指定提交的最新论文 Markdown；其全部 28 处图像引用及对应源文件保留 |
| `output/thesis/thesis-windows-fonts-43541893783-1/` | 指定提交的最新正式论文 DOCX / PDF（Windows 原字体交付版） |
| `output/docx/`、`output/pdf/` | 无“视觉校正版”后缀的正式任务书、开题报告；另保留导师业务流程讲解 PDF |
| `docs/materials/` | 原有 20 份学校通知、模板、参考论文与导师材料完整保留；另补充两份需求分析 PDF |
| `docs/materials/需求分析参考资料/` | Google Drive「毕业设计」目录的 DFD 辅助指导材料，不作为学校规范或实测证据 |
| `docs/experiments/`、`docs/validation/` | 原始实验、人工评价、必要测试证据、数据库及接口核对、交付与字体验证报告 |
| `docs/design/`、`docs/references/`、`docs/notes/`、`scripts/` | 界面设计、当前参考文献、相关指导说明和原有辅助脚本 |
| `review-copy/` | 本次新增的来源、逐文件哈希、排除清单、安全检查与完整性核验记录 |

审查可覆盖代码与数据库、接口、需求与实现对应、论文与正式导出件、学校规范及已有验证证据。历史报告中的测试结果属于其原始轮次；本次未运行系统、真实模型或论文质量验证，也不新增论文结论。

排除了旧论文 DOCX/PDF、视觉校正版开题旧稿、备份、未被现稿使用的旧图、逐页及大型拼版校样、安装和运行日志、重复构建日志、旧仓库管理记录、个人联系及交接资料、Actions 自动化流程、缓存和依赖目录。必要测试原始日志作为验证证据例外保留，字节不变。旧说明可能链接到这些已排除文件，请查 `review-copy/excluded-files.json`，或回到来源提交查看；本副本不是全部历史成果的备份。学校材料、现稿引用图和原始实验没有按重复内容去重。

Gemini 网页版请用“添加文件 → 更多上传 → 导入代码”输入本仓库地址。Google 官方限制为每个对话一个仓库、最多 5,000 文件及 100 MB；本副本按更严格的 80,000,000 字节预算核验。不要将仓库 ZIP 当成普通附件上传。PDF、DOCX、图片的存档完整性已检查，但 GitHub 导入对二进制内容的解析及实际账号可用性仍需在 Gemini 中确认；需要时单独上传相应 PDF。依据：[Google 导入说明](https://support.google.com/gemini/answer/16176929?hl=en)。

运行 `python review-copy/verify_copy.py` 可独立复核清单、哈希、必要目录、图像依赖和体积；该脚本只读文件，不运行应用或文档生成器。两份云盘 PDF 均已取得，第二份仅将文件名中的空格移除，内容未变。详见 `review-copy/drive-materials.json`。

按本次对话中继续制作公开副本的授权，正式原件中的作者姓名、学号、班级及导师署名原样保留；私人联系记录已排除，代码中的显式演示/隔离测试夹具和占位配置保留。本仓库由用户创建，审查副本上传到 `main` 分支。
