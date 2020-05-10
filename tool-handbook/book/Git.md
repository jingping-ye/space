# Git

## 常用命令

## 常见问题及解决方法

### 1. 强制使用一分支代码覆盖另一分支

> 以下假设要将develop分支强制覆盖至master分支，以下都是origin下的直接分支

1. 切换到develop分支下，并保证本地已经同步了远端develop的最新代码。

   ```
   git checkout develop
   git pull
   ```
2. 把本地的develop分支强制(-f)推送到远端master。

   `git push origin develop:master -f`

3. 切换到旧分支master。

   `git checkout master`

4. 下载远程仓库最新内容，不做合并。

   `git fetch --all`

5. 把HEAD指向master最新版本。

   `git reset --hard origin/master`