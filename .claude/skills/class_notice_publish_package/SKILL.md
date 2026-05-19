---
name: class_notice_publish_package
description: "整理班级通知小红书发布包。Use when the user says 整理班级通知发布包, 生成发布助手读取目录, 归档本次成品图片, 重命名主图副图, 整理小红书发布包, or asks to create info.json for the Xiaohongshu publish plugin. Copies final images from .codex/generated_images to the E drive standard publish directory, renames them to 主图.png and 副图1.png through 副图5.png, creates 发布文案.md and info.json, and validates real paragraph breaks before publishing handoff."
---

# class_notice_publish_package

## 功能

把 `.codex/generated_images` 里的班级通知最终图片复制到 E 盘标准发布目录，并按发布助手固定规则重命名，同时生成 `发布文案.md` 和 `info.json`。

默认检查完整发布包，不再检查半成品主图包。

只有当用户明确执行“主图质检流程”时，才允许发布包暂时只有主图。

固定目标根目录：

`E:\优逸店资料截图\班级通知\笔记素材\生成成品图片`

发布插件优先读取 `info.json`，不要依赖浏览器里的 Markdown 预览文本。

## 触发语

- 整理班级通知发布包
- 生成发布助手读取目录
- 归档本次成品图片
- 重命名主图副图
- 整理小红书发布包

## 输入

用户通常会提供：

- 源图片目录：例如 `C:\Users\Administrator\.codex\generated_images\某个批次ID`
- 目标发布包目录名：例如 `20260518_临时叫学生不用跑教室_全新生成`
- 每张图片对应页面：主图、P2、P3、P4、P5、P6
- 发布文案内容：标题、正文、标签、首评、验收重点

如果用户没有提供每张图的对应关系，必须先读取源目录图片并根据画面内容判断。

如果无法准确判断图片顺序，停止执行，输出所有图片文件名和缩略说明，不要乱命名。

## 输出

目标发布包目录中必须包含：

- `主图.png`
- `副图1.png`
- `副图2.png`
- `副图3.png`
- `副图4.png`
- `副图5.png`
- `发布文案.md`
- `info.json`
- `做图交接单.md`
- `状态.md`

## info.json 必需结构

必须生成：

```json
{
  "title": "笔记标题",
  "content": "第一段正文。\n\n第二段正文。\n\n第三段正文。",
  "tags": ["班主任", "老师日常", "教师工具"],
  "comment": "这里是首评",
  "product": {
    "id": "",
    "name": "班级通知"
  },
  "scheduleAt": ""
}
```

字段要求：

- `title` 放小红书标题，不能为空。
- `content` 放纯文本正文，不能为空。
- `content` 段落之间必须使用 `\n\n`。
- `tags` 必须是数组，不允许写成一个字符串。
- `tags` 里的标签不要带 `#`。
- `comment` 保存首评，不能为空。
- `product.name` 默认写 `班级通知`。
- `product.id` 暂时留空，除非用户提供商品 ID。
- `scheduleAt` 暂时留空，除非用户明确指定发布时间。

如果 `content` 不包含 `\n\n`，必须报错并停止，不允许通过。

## 发布文案.md 要求

`发布文案.md` 给人工检查使用，必须保留真实 Markdown 源码换行。

正文段落之间必须空一行，也就是源码里真实存在两个换行。

不要把正文写成一整行。  
不要只依赖浏览器自动换行。  
不要用 HTML 预览效果作为排版判断。  

`发布文案.md` 中的人眼可读内容必须和 `info.json` 对应：

- `## 正文标题` 对应 `info.json.title`
- `## 正文内容` 对应 `info.json.content`
- `## 标签` 对应 `info.json.tags`
- `## 首评` 对应 `info.json.comment`

## 执行流程

1. 确认源图片目录是否存在。
2. 读取源目录下的图片文件。
3. 判断图片对应关系：
   - 主图：P1 封面图
   - 副图1：P2
   - 副图2：P3
   - 副图3：P4
   - 副图4：P5
   - 副图5：P6
4. 如果无法准确判断图片顺序，停止执行，输出所有图片文件名和缩略说明。
5. 创建目标发布包目录；如果已存在，不删除原内容。
6. 复制最终确认版本到目标目录。
7. 统一重命名为发布助手固定文件名。
8. 创建或更新 `发布文案.md`，保留真实段落空行。
9. 创建或更新 `info.json`，正文段落使用 `\n\n`。
10. 校验图片、`发布文案.md`、`info.json` 是否全部存在。
11. 校验 `info.json` 字段格式和正文换行。
12. 如果完整发布包齐全，将 `状态.md` 改为“当前阶段：待发布”。
13. 输出发布包校验结果。

## 命名规则

必须使用：

- `主图.png`
- `副图1.png`
- `副图2.png`
- `副图3.png`
- `副图4.png`
- `副图5.png`
- `发布文案.md`
- `info.json`
- `做图交接单.md`
- `状态.md`

禁止使用：

- `ig_` 开头的随机文件名
- 长标题文件名
- 带空格的文件名
- 带括号的文件名
- `主图1.png`
- `封面.png`
- `p1.png`
- `p2.png`

## 校验逻辑

生成发布包后必须校验：

- `info.json` 是否存在。
- `title` 是否非空。
- `content` 是否非空。
- `content` 是否包含 `\n\n`。
- `tags` 是否为数组。
- `comment` 是否存在且非空。
- 图片文件是否齐全。
- `发布文案.md` 是否存在。
- `做图交接单.md` 是否存在。
- `状态.md` 是否存在。

如果 `content` 不包含 `\n\n`，必须报错并停止，不允许通过。

可使用本 Skill 自带脚本校验：

```powershell
python .\scripts\validate_publish_package.py "E:\优逸店资料截图\班级通知\笔记素材\生成成品图片\20260518_临时叫学生不用跑教室_全新生成"
```

## 执行边界

- 只复制和重命名，不删除源文件。
- 不修改图片内容。
- 不自动发布。
- 不让发布助手直接读取 `.codex/generated_images`。
- 无法判断图片顺序时必须停止询问。
- 不覆盖知识库核心规则，除非用户明确要求。

## 校验输出格式

完成后必须输出：

```text
【发布包校验】
目标目录：
主图.png：存在 / 缺失
副图1.png：存在 / 缺失
副图2.png：存在 / 缺失
副图3.png：存在 / 缺失
副图4.png：存在 / 缺失
副图5.png：存在 / 缺失
发布文案.md：存在 / 缺失
info.json：存在 / 缺失
做图交接单.md：存在 / 缺失
状态.md：存在 / 缺失

【info.json 校验】
title：通过 / 失败
content：通过 / 失败
content 是否包含真实段落换行 \n\n：通过 / 失败
tags 是否为数组：通过 / 失败
comment 是否存在：通过 / 失败

【最终结论】
发布包可交给小红书发布插件读取。
```

如果不通过，输出具体缺失项，不要说可以发布。
