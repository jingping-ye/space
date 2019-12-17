# 实验 02:直接使用 webpack 命令打包

1. 使用`npm ini -y`生成一个`package.json`文件

2. 安装webpack和webpack-cli

   ```sh
   cnpm i webpack webpack-cli -D
   ```

3. 在script中写入以下命令

   ```sh
   "pack": "webpack index.js -o bundle.js"
   ```

   这里其实运行的是`node_modules/.bin/webpack`,但是当创建webpack包的时候，自动化在`.bin`目录下创建了一个软链接，当执行`npm run pack`会自动在`.bin`目录下寻找相关脚本
   
4. 执行`npm run pack`

   附:[实验 02:直接使用 webpack 命令打包]( [https://github.com/jingping-ye/training-room/tree/master/%E7%8E%A9%E8%BD%ACwebpack/%E7%AC%AC%E4%B8%80%E7%AB%A0/train03](https://github.com/jingping-ye/training-room/tree/master/玩转webpack/第一章/train02) )

