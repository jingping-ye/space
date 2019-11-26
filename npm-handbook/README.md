# npm

## 什么是包

包就一堆封装起来的代码，目的是抽象或总结解决问题的方法，避免重复解决问题。包可以是一个文件，也可以是多个文件。

## npm的作用

1. 引入包

   把所有的包汇集在一个库中，使用同一的命令管理

2. 管理包之间的关系

   通过cdn引入代码库的形式，容易造成代码包之间版本兼容等问题。npm可以管理包和包之间的关系和包的版本。

## npm操作

1. 生成一个管理文件package.json

   ```js
   npm init -yes // -yes表示采用默认配置，也可以简写为-y
   ```

2. 安装包

   ```js
   npm install jquery@3.0.0 // 指定版本
   npm install jquery@lastst -g //安装最新版本
   npm install jquery // 默认安装最新版本
   npm install jqury -D // 默认安装jquery的最新版本至开发环境, -D表达--save-dev
   ```

   ps: 包会默认安装到根目录下的`node_modules`目录

3. 删除包

   ```js
   npm uninstall jquery
   ```

4. 更新包

   ```js
   npm update jquery // 更新jquery
   ```

5. 查询包

   ```js
   npm ls
   npm ls --depth 0 // 不输出包的依赖
   ```

6. 运行包

   我们可以在scripts中定义快捷命令，并且用`npm run <命令>`操作

   ```js
   npm run *<scripts>
   ```

   