# NVM

## 下载地址

https://github.com/coreybutler/nvm-windows/releases

## 常用命令

- nvm arch 常见当前 node 是运行在 32 位还是 64 位系统
- nvm install <version>[arch] 用于下载指定的 node 版本;arch 是一个可选参数，表示下载的是 32 位还是 64 位，默认下载 64 位。如果把 arch 设为字符 all,则同时下载 32 位和 64 位版本。r
- nvm list[available]: 用于展示 node 的版本，加一个 available 可以查看所有可安装的版本
- nvm use [available][arch]: 用于切换到不同的 node 版本（version 是 node 版本号，arch 还是用于指定 32 位或 64 位）

- nvm uninstall <version>：用于卸载某个 node 版本

- nvm version：用于展示当前在 windows 系统运行的 node 版本
