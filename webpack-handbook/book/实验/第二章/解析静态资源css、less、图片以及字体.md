# 实验 03：解析静态资源 css、less、图片以及字体

1. 使用`npm init -y`生成`package.json`文件

2. 新建`.gitignore`文件，写入以下

   ```sh
   /node_modules
   ```

3. 安装相关依赖

   ```sh
   cnpm i webpack webpack-cli babel-loader @babel/core @babel/preset-env @babel/preset-react react react-dom -D
   ```

4. 配置`webpack.config.js`文件，在`package.json`文件编写脚本运行命令

   ```js
   // webpack.config.js
   const path = require('path');
   module.exports = {
     entry: './index.js',
     output: {
       filename: 'bundle.js',
       path: path.join(__dirname, '/dist')
     },
     module: {},
     mode: 'development'
   };
   
   ```

   ```sh
   "build":"webpack"
   ```

5. 在`webpack.config.js`中配置babel和编写babel配置文件`.babelrc`

   ```js
   //	webpack.config.js 
   module: {
       rules: [
         {
           test: /\.js$/,
           use: ['babel-loader']
         }
       ]
     },
   ```

   ```sh
   //	.babelrc
   {
     "presets": ["@babel/preset-env"]
   }
   ```

6. 编写react组件

   ```sh
   import React from 'react';
   import ReactDOM from 'react-dom';
   
   class Index extends React.Component {
     render() {
       return <div>Hello React</div>;
     }
   }
   
   ReactDOM.render(<Index />, document.getElementById('root'));
   
   ```

7. 配置`@babel/preset-react`解析jsx

   ```sh
   {
     "presets": ["@babel/preset-env", "@babel/preset-react"]
   }
   ```

8. 运行`npm run build`

## 解析css

1. 安装css-loader和style-loader

   ```sh
   cnpm i css-loader style-loader -D
   ```

2. 在`webpack.config.js`中配置css-loader和style-loader
	  ```sh
    {
           test: /\.css$/,
           use: ['style-loader', 'css-loader']
         }
   ```
   
   PS: 注意这些要先写style-loader，再写class-loader。因为loader是链式调用的，从右到左调用。执行顺序为css--> commonJs对象 --> style。
   
3. 新建`index.css`文件

     ```css
     .theme-red-color {
       color: rgb(201, 67, 67);
     }
     
     ```
4. 修改`index.js`文件，引入css文件

   ```js
   import React from 'react';
   import ReactDOM from 'react-dom';
   import './styles/index.css';
   
   class Index extends React.Component {
     render() {
       return <div className='theme-red-color'>Hello React</div>;
     }
   }
   
   ReactDOM.render(<Index />, document.getElementById('root'));
   
   ```

   

--------------------

## 解析less

1. 安装less-loader

   ```sh
   cnpm i less less-loader - D
   ```

   

2. 修改webpack.config.js文件

   ```sh
 {
           test: /\.less$/,
           use: ['style-loader', 'css-loader', 'less-loader']
      }
   ```
3. 编写`index.less`文件
	
	```css
	.theme-bg-color {
      color: yellow;
    }

	```
4. 修改`index.js`文件 
   
   ```js
    import React from 'react';
    import ReactDOM from 'react-dom';
    import './styles/index.css';
    import './styles/index.less';

    class Index extends React.Component {
      render() {
        return <div className='theme-red-color theme-bg-color'>Hello React</div>;
      }
    }

    ReactDOM.render(<Index />,  document.getElementById('root'));

   ```
   
   
   

----------------

## 解析图片和字体

1. 安装file-loader或者url-loader。

   > file-loader和url-loader都可用于处于文件和字体，不同的是，url-loader可以将较小资源（图片和字体)转为base64

   ```sh
   cnpm i file-loader -D
   ```

2. 配置webpack.config.js

   ```js
    {
         test:/\.(png|svg|jpg|gif|jpeg)$/,
         use:['file-loader']
     },
     {
         test:/\.(woff|woff2|eot|ttf|otf)$/,
         use:['file-loader']
     }
   ```

3. 修改`index.js`文件

   ```js
   import React from 'react';
   import ReactDOM from 'react-dom';
   import logo from './assets/image/logo.jpg';
   import './styles/index.css';
   import './styles/index.less';
   
   class Index extends React.Component {
     render() {
       return (
         <div className='theme-red-color theme-bg-color'>
           <img src={logo} />
           Hello React
         </div>
       );
     }
   }
   
   ReactDOM.render(<Index />, document.getElementById('root'));
   ```

4. 打包`npm run build`

----------

也可以使用url-loader,url-loader和file-loader用法一致。与file-loader不同的是,url-loader可以设置一个大小限制，将图片和字体转为base 64

```js
 modules{
      rules:[
          {
              test:/\.(png|svg|jpg|gif|jpeg)$/,
              use:[{
                  loader:'url-loader',
                  options:{
                      limit:10240
                  }
              }]
          }
      ]
  }
```

