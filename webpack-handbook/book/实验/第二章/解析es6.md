# 实验 01：解析 es6

1. 使用`npm init -y`命令生成一个`package.json`文件

2. 安装依赖

   ```sh
   cnpm i @babel/core @babel/preset-env babel-loader webpack webpack-cli -D
   ```

3. 配置`webpack`

   （1）在`package.json`文件写入以下脚本

   ```sh
   "build":"webpack"
   ```

   （2）新建一个`webpack.config.js`,写入以下代码(使用babel-loader)

   ```js
   const path = require('path');
   module.exports = {
     entry: './index.js',
     output: {
       filename: 'bundle.js',
       path: path.join(__dirname, 'dist')
     },
     module: {
       rules: [
         {
           test: /\.js$/,
           use: 'babel-loader'
         }
       ]
     },
     mode: 'development'
   };
   ```

4. 配置`babel`--新建`.babelrc`配置文件

   ```sh
   {
     "presets": ["@babel/preset-env"]
   }
   ```

5. 运行`npm run build`命令

