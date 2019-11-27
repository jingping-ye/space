# GitBook

## 常用命令

- gitbook ls  // 列出所有gitbook版本
- gitbook uninstall <version>  // 卸载某个版本
- gitbook build // 编译成静态网页
  - gitbook build --gitbook=2.6.7  // 以某个版本编译，如果没有该版本，会自动下载
- gitbook init // 初始化目录文件
- gitbook help // 列出帮助命令
- gitbook serve // 生成网页并运行服务器
- gitbook --help // 列出gitbook-cli的帮助命令
- gitbook ls-remote 列出远程可用的gitbook版本
- gitbook fetch <version> 安装对应版本的gitbook

## 常见问题

### gitbook生成的html链接不能跳转?

降级gitbook版本至2.6.7,同时降级node版本至6.4.0