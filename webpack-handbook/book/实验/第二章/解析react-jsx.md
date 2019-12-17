# 实验 02: 解析 react-jsx

1. 使用`npm init -y`命令生成一个`package.json`文件

2. 安装依赖

   ```sh
   cnpm i @babel/core @babel/preset-env babel-loader webpack webpack-cli react reac-dom -D
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
     "presets": ["@babel/preset-env" ,"@babel/preset-react"]
   }
   ```

5. 新建`index.js`文件，写入以下代码

   ```js
   import React from 'react';
   import ReactDom from 'react-dom';
   
   class Index extends React.Component {
     render() {
       return <div>这里是首页</div>;
     }
     componentDidMount() {
       const a = [1, 2, 3];
       const b = [4, 5, 6];
       console.log(JSON.stringify([...a, ...b]));
     }
   }
   
   ReactDom.render(<Index />, document.getElementById('root'));
   
   ```

6. 新建`index.html`文件，写入以下代码

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <meta http-equiv="X-UA-Compatible" content="ie=edge" />
       <title>解析JSX</title>
     </head>
     <body>
       <div id="root"></div>
       <script src="./dist/bundle.js"></script>
     </body>
   </html>
   ```

7. 运行`npm run build`命令

8. 打开index.html文件测试

