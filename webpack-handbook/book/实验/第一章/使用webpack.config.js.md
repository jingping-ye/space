# 实验 03：使用 webpack.config.js

1. 使用`npm init -y`生成一个`package.json`文件

2. 在`package.json`文件中写入以下命令

   ```sh
   "pack": "webpack"
   ```

   当没有指定文件时，webpack会自动寻找`webpack.config.js`中的配置

3. 创建`webpack.config.js`文件，写入以下命令

   ```js
   module.exports = {
     entry: './index.js', //打包的入口文件（默认）
     output: {
       filename: 'bundle.js',
       path: __dirname
     }, // 打包的输出文件（默认）
     mode: 'production', // 环境
     module: {
       rules: [
         { test: /\.txt$/, use: 'raw-loader' } //loader配置
       ]
     },
     plugins: []
   };
   
   ```

   - 注意此处的entry入口文件要用相对路径，否则将找不到文件
   - __dirname:指向被执行 js 文件的绝对路径 ,node.js

4. 运行`npm run pack`，可以在当前目录下找到打包生成的`bundle.js`文件

附:[实验 03：使用 webpack.config.js]( [https://github.com/jingping-ye/training-room/tree/master/%E7%8E%A9%E8%BD%ACwebpack/%E7%AC%AC%E4%B8%80%E7%AB%A0/train02](https://github.com/jingping-ye/training-room/tree/master/玩转webpack/第一章/train03) )

