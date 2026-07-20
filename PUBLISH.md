# 发布到GitHub

建议新建独立公开空仓库：`kumizeod/ml-foundations-study`。
创建入口：https://github.com/new?name=ml-foundations-study
不要勾选自动添加README、gitignore或LICENSE。

解压时保留`.git`，在解压目录打开PowerShell。第一次查看本地历史：

```powershell
git log --reverse --format="%h %aI %s"
```

只发布到7月底、8月底或9月28日：

```powershell
powershell -ExecutionPolicy Bypass -File .\publish.ps1 -Through 2026-07
powershell -ExecutionPolicy Bypass -File .\publish.ps1 -Through 2026-08
powershell -ExecutionPolicy Bypass -File .\publish.ps1 -Through 2026-09
```

直接发布全部也只需最后一条。日期前缀通过普通推送更新main，不使用force。
推送较早前缀不能撤销较晚前缀，Git会拒绝非快进更新。

如遇认证问题，在同一个Windows PowerShell环境使用：

```powershell
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
```

如果未安装GitHub CLI，可使用Git for Windows的浏览器认证，或先安装CLI。
不要将账号密码当作HTTPS Git凭据。无需把Token交给任何人。

脚本不创建GitHub仓库、不安装软件、不改其他仓库和全局Git配置。
若你想用不同仓库名，可传`-Repository owner/name`。远端若已有无关历史，
先人工检查，不要为了通过推送而强制覆盖。

## 贡献图条件

仓库应为独立仓库，提交可达默认分支，作者邮箱关联账号。归属邮箱为
`145240248+kumizeod@users.noreply.github.com`。GitHub最终决定统计结果，
可能需要等待刷新。创建时间与提交者日期不会因作者日期变化而消失。
