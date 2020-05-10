# NVM

> 多版本node管理工具

## 下载地址

https://github.com/coreybutler/nvm-windows/releases

## 常用命令

- nvm arch 常见当前 node 是运行在 32 位还是 64 位系统
- nvm install <version>[arch] 用于下载指定的 node 版本;arch 是一个可选参数，表示下载的是 32 位还是 64 位，默认下载 64 位。如果把 arch 设为字符 all,则同时下载 32 位和 64 位版本。r
- nvm list[available]: 用于展示 node 的版本，加一个 available 可以查看所有可安装的版本
- nvm use [available][arch]: 用于切换到不同的 node 版本（version 是 node 版本号，arch 还是用于指定 32 位或 64 位）
- nvm uninstall <version>：用于卸载某个 node 版本
- nvm version：用于展示当前在 windows 系统运行的 node 版本
- nvm root:nvm 安装目录
- nvm install latest // 安装最新

## 安装过程

[使用 nvm 管理不同版本的 node 与 npm | 菜鸟教程](https://www.runoob.com/w3cnote/nvm-manager-node-versions.html)

注意：为了防止国外镜像下载卡顿，可切换到淘宝源进行安装。

1. 使用nvm root 找到nvm的安装目录。

2. 编辑settings.txt文件，在末尾增加两行，即可。

   ```
   node_mirror: https://npm.taobao.org/mirrors/node/
   
   npm_mirror: https://npm.taobao.org/mirrors/npm/

   
   ```
   
   