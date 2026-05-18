# GitHub Sync README

## 仓库定位

这个公开仓库用于保存“班级通知小红书内容增长系统”的公开项目状态。

它方便 ChatGPT / Codex / Claude Code 读取：

- 系统最高目标
- 当前产品资料
- 内容生产规则
- 本地 Skill 说明
- 笔记方案
- 发布包索引
- 数据复盘摘要
- 运行状态摘要

## 公开边界

本仓库是公开仓库，所有进入仓库的内容都必须默认可公开。

允许同步：

- 系统协议与总规则
- 产品公开说明
- 内容生产模板
- 本地 Skill 说明文档
- 笔记方案草稿
- 做图交接单
- 发布包索引
- 数据复盘摘要
- 运行日志摘要

禁止同步：

- Cookie
- Token
- API Key
- 账号密码
- 客户隐私
- 完整订单明细
- 激活卡号完整列表
- 带登录态的 network-response 文件
- HAR 文件
- 浏览器缓存
- 原始接口响应
- E 盘图片原图

## 同步原则

每次 push 前必须先执行敏感信息检查。

如果发现疑似敏感文件，必须停止 push，先人工确认。

GitHub 仓库只作为公开项目状态仓库，不作为私密数据仓库。

## GitHub raw 换行校验标准

GitHub raw 默认使用 LF 换行，即 `\n`，不一定是 Windows 的 CRLF `\r\n`。

校验线上 raw 文件行数时，必须使用：

```powershell
$content = (Invoke-WebRequest -Uri "raw地址" -UseBasicParsing).Content
($content -split "`n").Count
```

不要使用：

```powershell
$content -split "`r`n"
```

如果用 `\r\n` 判断，可能会误判为 1 行。

以后判断 GitHub 线上文件是否有真实换行，以以下结果为准：

- LF_COUNT 大于 20：通过
- `content -split "\n"` 行数正常：通过
- GitHub 页面能正常显示 Markdown：通过

不要再仅凭某些网页抽取工具显示“一行”就判断失败。

当前已验证：

- `.gitignore`：GitHub raw 按 `\n` 分割为 38 行
- `PROJECT_STATUS.md`：GitHub raw 按 `\n` 分割为 103 行
- 发布包索引：GitHub raw 按 `\n` 分割为 50 行

本次结论：

GitHub 同步换行问题已通过，不再重复修复。
