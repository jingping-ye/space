# 第一章 webpack 与构建发展简史

## 一、为什么要使用构建工具

1. web应用多元化:随着手机、平板、web、可穿戴设备的发展，一份代码往往要运行在多个端，而不同端对代码的要求各不相同。比如pc端应用，需要针对支持单页页面的打包构建;H5页面通常对性能和可访问性有着极高的要求，因此需要通过构建来支持服务端渲染和PWA离线缓存。
2. 组件化:nodejs的社区十分繁荣,npm组件不能直接引用，但是可以通过webpack构建。
3. 框架DSL解析：jsx,vue指令在浏览器无法直接解析，需要通过webpack转换
4. 转换es6语法
5. 代码压缩混淆
6. css前缀补全/预处理器
7. 图片压缩

## 二、构建工具发展史

ant+YUI Tool --> grunt --> fis3 /gulp --> rollup/webpack/parcel

- YUI Tool:远古前端开发方式：切图片--> 编写css-->编写html-->编写js。通过YUI进行本地css代码和js代码压缩
- grunt:模块化概念催生。grunt将整个打包过程分为一个个任务，打包之后会放在本地磁盘上，速度比较慢。
- gulp: 使用文件流的概念，将打包之后的文件放在内存中，下个打包过程可以使用上个打包的内存。
- fis3: 百度出品，fis3官方团队不再进行维护

## 三、为什么选择webpack

1. 社区生态丰富
2. 配置灵活和插件化扩展
3. 官方更新迭代速度快

|              | webpack        | grunt       | gulp        |
| ------------ | -------------- | ----------- | ----------- |
| 定义         | Module bundler | Task runner | Task runner |
| 语言         | JS             | node.js     | node.js     |
| 发布时间     | 2012.3         | 2012.6      | 2013.7      |
| GitHub stars | 40766          | 11796       | 29427       |
| 周下载量     | 3,385,392      | 478,876     | 816,228     |

## 四、简单的webpack使用

### 安装及简单配置

- 默认配置文件:webpack.config.js
- webpack --config webpack.dev.config.js 制定配置文件
- 常用配置:出口、入口、环境、模块、插件

```js
module.exports = {
    entry:'./index.js', //打包的入口文件（默认）
    output: {
        filename: 'main.js',
        path: __dirname
      }, // 打包的输出文件（默认）
    mode:'production', // 环境
    module:{
    	rules:[
    		{test:/\.txt$/,use:'raw-loader'} //loader配置
    	]
	},
    plugins:[	//	插件配置
        new HtmlwebpackPlugin({
            template:'./src/index.html'
        })
    ]
}
```

```sh
//	安装
mkdir my-project
npm install webpack webpack-cli -D // 使用cnpm更快
```

### 实验

- [01 使用.bin下的webpack打包](./实验/第一章/使用.bin下的webpack打包.md)
- [02 直接使用webpack命    令打包](./实验/第一章/直接使用webpack命令打包.md)
- [03 使用webpack.config.js](./实验/第一章/使用webpack.config.js.md)
- [04 多入口打包](./实验/第一章/多入口打包.md)

## 其他:参考名词

 **客户端渲染**：用户访问 url，请求 html 文件，前端根据路由动态渲染页面内容。关键链路较长，有一定的白屏时间。

SSR: 服务端渲染。简单理解是将组件或页面通过服务器生成html字符串，再发送到浏览器，最后将静态标记"混合"为客户端上完全交互的应用程序 ；用户访问 url，服务端根据访问路径请求所需数据，拼接成 html 字符串，返回给前端。前端接收到 html 时已有部分内容； 

Prerender:预渲染（预加载）。 构建阶段生成匹配预渲染路径的 html 文件（注意：每个需要预渲染的路由都有一个对应的 html）。构建出来的 html 文件已有部分内容  构建阶段生成匹配预渲染路径的 html 文件（注意：每个需要预渲染的路由都有一个对应的 html）。构建出来的 html 文件已有部分内容 。

tree shaking：摇树优化；删除没用到的代码 。

PWA: PWA（Progressive Web App）是一种理念，使用多种技术来增强web app的功能，可以让网站的体验变得更好，能够模拟一些[原生](https://baike.baidu.com/item/原生/1203260)功能，比如通知[推送](https://baike.baidu.com/item/推送/9908161)。在移动端利用标准化框架，让网页应用呈现和原生应用相似的体验 

文件指纹: 当你从网络上下载了软件后，想确保此软件没有被人修改过（如添加了木马/病毒/非官方插件），或在下载中被破坏，可以用文件指纹验证（MD5）技术进行确认。 

热更新: 热更新是一种各大手游等众多[App](https://baike.baidu.com/item/App)常用的更新方式。简单来说，就是在用户通下载安装APP之后，打开App时遇到的即时更新。 

