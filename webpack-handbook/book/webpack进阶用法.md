# 第三章 webpack 进阶用法

## 自动清理构建目录产品

- 通过npm script清理目录

  ```sh
   rm -rf ./dist&&webapck
   rimraf ./dist && webpack
  ```

- 插件 clean-webpack-plugin 默认删除output的指定输出目录

```js
const { CleanWebpackPlugin } = require('clean-webpack-plugin'); //	或者
// const CleanWebpackPlugin=require('clean-webpack-plugin'); 
module.exports = {
    entry:{
        app:'./src/app.js',
        search:'./src/search.js'
    },
    output:{
        filename:'[name][chunkhash:8].js',
        path:__dirname + '/dist'
    },
    plugins:[
        new CleanWebpackPlugin()
    ]
}
```

## postCSS插件autoprefixer自动补齐css3前缀

> css功能增强

css3的属性为什么需要前缀? 浏览器标准没有统一

- trident(-ms) ie
- geko(-moz) firefox
- webkit(-webkit) chrome
- presto(-o) opera

### 使用autoprefixer 后置处理器 代码打包完之后

> 根据can i use 自动补齐前缀

- 最新的 autoprefixer 版本里面建议把 browserslist 写在 package.json 或者 . browserslistrc 文件里面去了

```js
npm i postcss-loader autoprefixer -D
module.exports = {
    entry:{
        app:'./src/app.js',
        search:'./src/search.js'
    },
    output:{
        filename:'[name][chunkhash:8].js',
        path:__dirname + '/dist'
    },
    rules:[
        test:/\.less$/,
        use:['style-loader','css-loader','less-loader',{
        	loader:'postcss-loader',
        options:{
            plugins:()=>[
                require('autoprefixer')({
                    browsers:["last 2 version", ">1%", "IOS 7"] // 需要兼容浏览器的版本；版本使用人数所占人数;IOS7以上的
                })
               ]
            }
        }]
    ]
}
```

- 其他
  - 单独对webpack写配置 webpackchain
  - loader的顺序 less-loader --> postcss-loader --> css-loader --> style-loader/MiniCssExtractPlugin.loader(不将css文件插入到style中，直接抽离)

## 移动端css px自动转换rem

> 特性增强；rem:font-size of the root element

rem和px的对比:rem是相对单位;px是绝对单位

### 使用px2rem-loader

页面渲染时计算根元素的font-size的值

- 可以使用手淘的lib-flexible库
  - 解决手机端1px问题
  - vw/wh和rem:rem兼容性更好，支持android2.2以上的机型。但是vm只支持android4.4和ios8以上的。
- https://github.com/amfe/lib-flexible

```js
npm i px2rem-laoder -D
np i lib-flexible -S // 动态计算根元素rem的单位
<script type="text/javascript"> // 需要前置
	//	复制libflexible    
</script>

module.exports = {
    entry:{
        app:'./src/app.js',
        search:'./src/search.js'
    },
    output:{
        filename:'[name][chunkhash:8].js',
        path:__dirname + '/dist'
    },
    rules:[
        test:/\.less$/,
        use:['style-loader','css-loader','less-loader',{
        	loader:"px2rem-loader",
            options:{
                remUnit:75, // 1rem = 75px 转换单位 750的视觉稿
                remPrecision:8 // px转换成rem后面小数点的位数
            }
        }]
    ]
}
```



### 其他

- 如何不想转为rem可以使用`/*no*/`注释

- 设置exclude

- postcss有rem插件

- pv/uv? 访问量/独立访客

-   如果设置的 remUnit 是 75，那么对于 750 的设计稿如果字体是 24px，就写 24px（实际上在 iphone 6是12px的大小）

  如果设置的 remUnit 是 37.5，那么对于 375的设计稿如果字体是 12px，就写 12px（实际上在 iphone 6是12px的大小）
  

## 静态资源内联

> 什么是静态资源内联?

### 意义

代码层面:

- 页面框架的初始化脚本
- 上报相关打点 上报点,什么时候完成资源加载
- css内联避免页面闪动

请求层面:减少http网络请求数

 - 小图片或者字体内联(url-loader,limit，小于limit直接内联进去)

### loader

raw-loader 内联html/js 源码只有十几行，使用0.5版本

```js
npm i raw-loader@0.5.1 -D 
//	将str引入到对应的位置
${require('raw-loader!babel-loader!./meta.html') // 已经有script就不需要再用script
<script>${require('raw-loader!babel-loader!../../node_modules/lib-flexible')}}</script>
```

### css内联

- 借助style-loader
- html-inline-css-webpack-plugin

```js
module.exports = {
    entry:{
        app:'./src/app.js',
        search:'./src/search.js'
    },
    output:{
        filename:'[name][chunkhash:8].js',
        path:__dirname + '/dist'
    },
    rules:[
        test:/\.less$/,
        use:[{loader:'style-loader',options:{
        	insertAt:"top", // 样式插入到<head>
        	singleton:true // 将所有style标签合并成一个}},
        'css-loader','less-loader']
    ]
}
```

### 其他

- style-loader是代码运行时动态的创建style标签，然后将css style插入到style标签里面。
- css-loader 的作用是将 css 转换成 commonjs 对象，也就是样式代码会被放到 js 里面去了。
- css内联:现将css提取打包成一个独立的css文件（使用MiniCssExtractPlugin.loader），然后读取提取出的 css 内容注入到页面的 style 里面去。这个过程在构建阶段完成。

## 多页面应用打包通用方案

### 多页面应用(MPA)概念

每一个页面跳转的时候，后台服务器都会返回一个新的html文档，这种类型的网站也就是多页网站，也叫做多页应用。

优势：

- 页面解耦
- 对seo更加友好

### 多页面打包基本思路

每个页面对应一个entry,一个html-webpack-plugin

缺点:每次新增或删除都需要修改

- 动态获取entry和设置html-webpack-plugin数量。

  每个入口文件都约定为index.js

  ```js
  module.exports = {
      entry:{
          index:'./src/index/index.js',
          search:'./src/search/index.js'
      }
  }
  ```

- 利用glob.sync

  ```js
  entry:glob.sync(path.join(__dirname, './src/*/index.js'))
  ```

  利用linux的文件通配匹配

```js
const setMAP  = ()=>{
    const entry = {};
    const htmlWebpackPlugins = [];
    
    const entryFiles = golb.sync(path.join(__dirname,'index.js'));
    Object.keys(entryFiles)
        .map((index)=>{
        const entryFile = entryFiles[index];
        const match = entryFile.match(/src\(.*)/index\.js/);
        const pageName = match&&match[1];
        
        entry[pageName] = entryFile;
        htmlWebpackPlugins.push({
            
        })
    })
    return {
        entry,
        htmlWebpackPlugins
    }
}
setMAP();
```



### 其他

  更新文件缓存是生成的文件指纹去控制的，文件变化后，那么文件指纹会发生相应变化，就不会出现缓存还在的问题了。顺便说下通常的文件缓存策略：

html: header 头的 cache-control 会设置成 no-cache。也就是 html 文件不会走缓存

css/js/img 等静态资源：header头的 cache-control 设置成强缓存，缓存时间通常是1年的样子。通过文件指纹控制缓存是否失效，文件指纹一变，请求就不会走旧文件了。  

1、map确实比foreach快，自己用console.time花2分钟做实验就知道了；
2、foreach会改变原数组，在这里我们不想对原数组进行任何修改，只是想拿数据来用；
3、map会返回一个新的数组，如果像有额外操作，可以继续在后面链式的使用filter、reduce等等，很方便。有返回值不是说一定要把这个返回值拿来用，不要读死书；
4、entryfile可以直接用map，这里遍历keys是考虑到如果entryfile如果是一个对象的情况，其实按照本章案例，用map、foreach、for遍历都行，看你编码习惯，作者在用的时候顺便说明一下就好了，导致评论里有很多人不理解。

## 使用sourcemap

作用：通过source map定位到源代码 阮一峰

开发环境开启，线上环境关闭

- 线上排查问题的时候可以将sourcemap上错到错误监控系统

### source map 关键字

- evel:使用eval包裹模块代码
- source map:产生.map文件
- cheap :包含列的信息
- inline: 将.map作为DataURI嵌入，不单独生成.map文件
- module:包含loader的sourcemap

### sourcemap的类型

### 其他

基本上开发环境直接用source-map。
production环境就把source-map添加到Error Reporting Tool（e.g. Sentry）上。这样既不直接暴露源代码，也能方便解决production环境遇到的bug。

## 提取页面公共资源

> 提取什么页面公共资源?

基础库分离:

思路:将react、react-dom基础包通过cdn引入,不引入bundle中

- 方法1:使用html-webpack-externals-plugin

- 使用splitchunksplugin进行公共脚本分离。webpack4内置，替代commonschunkplugin插件
  - chunks参数说明
    - async: 异步引入的库进行分离(默认)
    - initial 同步引入的库进行分离
    - all 所有引入的库进行分离（推荐）
  - test匹配规则
  - minChunks 设置最小引入次数为2次
    minusSize 分离包的体积的大小

chunks 决定了插入到 html 里面的 js 脚本的引用顺序。建议顺序是：react/react-dom 基础包 -> 业务项目的 公共 common.js 包 的顺序放

## tree shaking（摇树优化）的使用和原理分析

概念:1个模块可能有多个方法，只要其中的某个方法使用到了，则整个文件都会被打倒bundle里面去,tree shaking就是只把用到的方法打入bundle,没用到的会在uglify阶段被擦掉

使用：webpack默认支持,在.babelrc里设置modules:false即可.production mode的情况下默认开启

要求: 必须是es6语法，cjs的方式不支持

### 原理

DCE(dead code Elimination)

- 代码不会被执行，不可打倒
- 代码执行的结果不会被用到
- 代码只会影响死变量（只写不读）

## scope hoisting使用和原理分析

> scope hoisting 将所有的模块的代码按照引用顺序放在一个函数作用域内，然后适当重命名一些变量以防止变量名冲突。

对比:通过scope hoisting可以减少函数声明代码和内存开销。

## 代码分割和动态import

> 对于大的web应用来讲，将所有的代码都放在一个文件中显然是不够有效额，特别是你的某些代码块是在某些特殊的时候才会被使用到。webpack有一个功能就是讲你的代码库分割成chunks（语块)，当代码运行到需要它们的时候再进行加载。

适用的场景：

- 抽离相同代码到一个代码块
- 脚本懒加载，使得初始下载的代码更小

## 在webpack中使用eslint

## webpack打包组件和基础库

## webpack实现SSR打包(上)

## webpack实现SSR打包(下)

## 优化构建时命令行的显示日志

> 展示需要的信息

统计信息stats

> 输出webpack中统计的信息

| preset        | alternative | description                    |
| ------------- | ----------- | ------------------------------ |
| `errors-only` | none        | 只在发生错误时输出             |
| `minimal`     | none        | 只在发生错误或有新的编译时输出 |
| `none`        | false       | 没有输出                       |
| `normal`      | `true`      | 标准输出                       |
| `verbose`     | none        | 全部输出                       |

```js
stats:'errors-only' // 在生产环境直接添加
devServer:{
    contentBase:'./dist',
    hot:true,
    stats:'errors-only' // 在开发环境必须加在devServer中
}
```

### 使用插件friendly-errors-webpack-plugin

> 直接显示结果

- success : 构建成功的日志提示
- warning:构建警告的日志提示
- error:构建报错的日志提示

stats设置成errors-only

插件开头大写

```js
module.exports = {
    entry:{
        app:'./app.js',
        search:'./search.js'
    },
    output:{
        filename:'[name][chunkhash:8].js',
        path:__dirname + '/dist'
    },
    plugins:[
        new FriendlyErrorsWebpackPlugin()
    ],
    stats:'errors-only'
}
```



## 构建异常和中断处理

### 如何判断构建是否成功?

在CI/CD的pipline或者发布系统需要知道当前构建状态

每次构建完成之后输入`echo $?`获取错误码

```sh
npm run build
echo $? // webpack4会自动抛出错误码，但是webapck3不会
```

node.js中的`process.exit`规范

- 0表示成功完成，回调函数，err为null
- 非0表示执行失败，回调函数中，err不为null,err.code就是传给exit的数字

### 如何主动捕获并处理构建错误

compiler在每次构建结束后会触发done这个hook.

process.exit主动处理构建报错

````js
plugins:[
    function(){
        this.hooks.donw.tap('done',(stats)=>{
            if(stats.compilation.errors&&stats.compilation.errors.length && process.argv.indexOf('--watch') == -1){
                console.log('build error');
                process.exit(1);
            }
        })
    }
]
````



