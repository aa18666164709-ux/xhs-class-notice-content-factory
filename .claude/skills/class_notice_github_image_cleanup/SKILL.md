---
name: class_notice_github_image_cleanup
description: Use when the user says 清理GitHub临时图片, 删除已复核主图预览, 清理ChatGPT临时图片, or 清理线上仓库图片. Cleans temporary ChatGPT image previews from the GitHub-tracked knowledge base while preserving written main-image review conclusions.
---

# Class Notice GitHub Image Cleanup

## 触发语

- 清理GitHub临时图片
- 删除已复核主图预览
- 清理ChatGPT临时图片
- 清理线上仓库图片

## 功能

清理 GitHub 仓库中已经被 ChatGPT 复核过的临时图片，只保留文字复核结论。

## 执行流程

1. 检查目录：`90-临时给ChatGPT看的图片/`
2. 查找图片文件：
   - `.png`
   - `.jpg`
   - `.jpeg`
   - `.webp`
3. 如果存在图片文件，先确认是否已经有对应文字结论文件：`16-复盘进化库/主图复核结论/`
4. 如果没有文字结论，先创建：`16-复盘进化库/主图复核结论/YYYYMMDD_主图复核结论.md`
5. 如果用户明确说“已经复核完”，则删除临时图片文件。
6. 删除后执行：

```powershell
git status
git add .
git commit -m "cleanup temporary ChatGPT image previews"
git push
```

## 文字结论模板

```markdown
# YYYYMMDD 主图复核结论

## 本轮主图拼图文件名

## ChatGPT 是否已复核
待确认 / 已复核

## 通过主图

## 需重做主图

## 优化建议

## 后续动作
```

## 执行边界

- 只删除 `90-临时给ChatGPT看的图片/` 目录下的图片。
- 不删除知识库规则文件。
- 不删除发布包索引。
- 不删除复盘结论。
- 不删除 E 盘本地成品图片。
- 不删除任何发布助手需要读取的本地图片。

## 完成后输出

完成清理后输出：

- 删除了哪些临时图片
- 保留或创建了哪个文字复核结论
- 是否已提交并推送
- commit hash
