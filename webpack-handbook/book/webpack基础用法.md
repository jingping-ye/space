# 第二章 webpack 基础用法

## entry

> 入口:指定打包的入口;源代码

webpack是一个模块打包器，webpack把图片、字体、文本、css代码、js代码都看作模块，模块存在依赖文件。从入口文件开始寻找依赖，形成依赖树，编译完了之后才会开始生成打包资源。

单入口:单页应用

```js
module.exports = {
    entry:"./index.js"
}
```

多入口:多页应用

```js
module.exports = {
    entry:{
        "index":"./index.js",
        "signup":"./signup.js"
    }
}
```

## output

> 打包的输出；结果代码；

多入口:通过占位符确保文件名称的唯一 ` [name]`

```js
module.exports = {
    entry:{
        "index":"./index.js",
        "signup":"./signup.js"
    },
    output:{
        filename:"[name].bundle.js",
        path:__dirname
    }
}
```

## loaders

>loader将webpack原生不支持解析的文件类型通过loader去支持。

webpack开箱只支持js和json两种文件，通过loaders去支持其他文件类型并转换为有效的模块，并且可以添加依赖图去。

loader本身是一个函数，接受源文件作为参数，返回转换结果。

### 常见的loaders

| 名称          | 描述                                                     |
| ------------- | -------------------------------------------------------- |
| babel-loader  | 转换es6,es7语法                                          |
| css-loader    | 支持.css文件的加载和解析，如果采用import的语法           |
| less-loader   | 将less文件转换为css                                      |
| ts-loader     | 将ts转换为js                                             |
| file-loader   | 进行图片、字体等的打包                                   |
| raw-loader    | 将文件以字符串的形式导入,首屏                            |
| thread-loader | 多进程打包js和css(正常情况下，webpack只会有一个进程打包) |

### loader的用法

```js
modules:{
    rules:[
        {
            test:/\.txt$/, use:'raw-loader'
        }
    ]
}
```

- test 指定匹配规则，正则
- use 指定所使用的loader名称

## plugins

> 增强webpack的功能，用于打包输出的js文件优化，资源的管理和环境环境注入。任何loader无法进行的事情，可以通过plugins完成。plugins作用于整个构建过程。

### 常见plugins

| 名称                                              | 描述                                                       |
| ------------------------------------------------- | ---------------------------------------------------------- |
| CommonsChunkPlugin  =>splitchunksplugin           | 将chunks相同的模块提取成公共js，比如两个js文件有相同的函数 |
| CleanWebpackPlugin                                | 清理构建目录                                               |
| ExtractTextWebpackPlugin=>mini-css-extract-plugin | 将css从bundle文件里提取成一个独立的css文件                 |
| CopyWebPackPlugin                                 | 将文件或者文件夹拷贝到构建的输出目录                       |
| HtmlWebpackPlugin                                 | 创建html文件去承载输出的bundle                             |
| UglifyjsWebpackPlugin                             | 压缩js                                                     |
| ZipWebpackPlugin                                  | 将打包出的资源生成一个zip包                                |

### 用法

> 挡在plugins数组里就可以了

```js
plugins:[
    new HtmlWebpackPlugin({
        template:'index.html'
    })
]
```

## mode

> 指定webpack的当前打包环境:development|production|none ，默认为production。

webpack会根据设置的mode自动设置一些webpac

k的一些功能

### mode的内置函数功能

| 选项         | 描述                                                         |
| ------------ | ------------------------------------------------------------ |
| development  | 设置`process.env.NODE_ENV`的值为`development`，开启`NamedChunkPlugin`和`NamedModulesPlugin` （打印哪些模块发生了热更新，打印路径） |
| `production` | 设置`process.env.NODE_ENV`的值为`production`，开启`FlagDependencyUsagePlugin`,`FlagIncludeChunkPlugin`,`ModuleConcatenationPlugin`,`NoEmitOnErrorsPlugin`,`OccurrenceOrderPlugin`,`SideEffectsFlagPlugin`<br/>代码压缩和去除无效代码 |
| `none`       | 不开启任何优化选项                                           |

- process.env会返回用户的环境变量,NODE_ENV环境变量中用于设置构建脚本是开发阶段还是生产阶段的

## 解析es6和react jsx

### 解析es6 

> webpack支持解析js，但是不支持es6，借助babel-loader来解析

### 基础用法

````js
//	webpack.config.js
modules:{
    rules:[
        {
            test:/\.js$/,
            use:'babel-loader'
        }
    ]
}
````

```sh
//	 .babelrc
{
	"presets":[
		"@babel/preset-env"
	],
	"plugins":[
		"@babel/proposal-class-properties"
	]
}
```

#### babel-loader

- babel的配置文件时`.babelrc`

- presets:一系列babel plugins的集合
  - preset-env 解析es6
  - preset-react 解析react
- plugins:一个plugins对应一个功能

## 解析css、less和sass

### 解析css

- css-loader 用于加载.css文件，并且转换成commonjs对象
- style-loader 将样式通过`<style>`标签插入到head中

#### 基础用法

```js
modules{
    rules:[
        {
            test:/\.css$/,
            use:['style-loader','css-loader']
        }
    ]
}
```

- PS:loader是链式调用的，从右到左调用。这里必须先写css-loader,再写style-loader，否则会报错。执行顺序为css--> commonJs对象 --> style。 因为 loader 采用的是 compose 的实现，不是 unix 的 pipe 实现。 

### 解析less和sass

```js
modules{
    rules:[
        {
            test:/\.css$/,
            use:['style-loader','css-loader','less-loader']
        }
    ]
}
```

- less-loader:less-loader对less解析

```sh
cnpm i less less-loader -D
```

- less-loader依赖less

## 解析图片和字体

- file-loader 处理文件(非代码文件:图片、字体)

```js
  modules{
      rules:[
          {
              test:/\.(png|svg|jpg|gif|jpeg)$/,
              use:['file-loader']
          },
          {
              test:/\.(woff|woff2|eot|ttf|otf)$/,
              use:['file-loader']
          }
      ]
  }
```

- url-loader:处理图片和字体，可以设置较小资源base64(将小图片和小字体可以转为base64)

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

- limit 10240byte (10kb)拷贝如果图片资源小于10kb的话，url-loader会自动将图片转为base64

## 文件监听

> 文件监听是在发现源码发生变化是，自动重新构建出新的输出文件。缺点：需要手动刷新浏览器。

webpack开启监听模式，有两种方式

- 启动webpack命令时，带上--watch参数
- 在配置webpack.config.js中设置watch:true

```js
//	package.json
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack",
    "build:watch":"webpack --watch"
  },
```

运行`npm run build:watch`就好了。

唯一缺陷：每次需要手动刷新浏览器。

```js
// webpack.config.js
module.exports = {
    //	默认false,也就是不开启
    watch:true,
    watchOptions:{
        //	默认为空，不监听的文件或者文件夹，支持正则匹配
        ignored:/node_modules/,
        //	监听到变化发生会等300ms再去执行，默认300ms
        aggregateTimeout:300,
        //	判断文件是否发生变化是通过不停询问系统指定文件有没有变化实现的，默认每秒问1000次
        poll:1000
    }
}
```

### 文件监听的原理分析

轮询判断文件的最后编辑时间是否发生变化。一开始会有文件修改时间，这个修改时间会存储起来。比较两个时间，从而判断是否发生变化。某个文件发生了变化，并不会立刻告诉监听者，而是先缓存起来，等到aggregateTimeout(缓存等待时间)。

## 热更新

### 方法一:使用webpack-dev-server与HotModuleReplacementPlugin插件共同使用

- WDS 不刷新浏览器
- WDS 不输出文件，而是放在内存中。--watch的方式是放在本地磁盘，所以wds的速度更快。
- 要和HotModuleReplacementPlugin插件一起使用，这个插件是webpack内置的。

```js
//	package.json
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack",
    "build:watch": "webpack --watch",
    "dev":"webpack-dev-server --open"
  },
```

- open 构建完成之后自动开启浏览器



指定配置文件

```js
//	package.json
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack --config webpack.prod.js",
    "build:watch": "webpack --watch",
    "dev":"webpack-dev-server --config webpack.dev.js --open"
  },
```



### 方法二:使用webpack-dev-middleware

> 自建node服务器

- WDM将webpack输出的文件传输给服务器
- 适用于灵活的定制场景

### 热更新原理

- weback Compile（编译器z）:将js编译成Bundle
- HMR Server:将热更新的文件输出给HMR Runtime
- Bundle server: 提供文件在浏览器的访问(localhost:8080)
- HMR Runtime:打包阶段会被注入到浏览器端的bundle.js，更新文件的变化,会与服务器进行一个连接，通常是websoket
- bundle.js：构建输出的文件

#### 热更新的过程

- 启动阶段:文件系统打包1-->2--A-->B
- 文件变化: 1--> 2-->3-->4

## 文件指纹:chunkhash/contenthash/hash

### 文件指纹是什么

打包输出文件名的后缀。好处：文件指纹做版本的管理。项目发布时，有些文件修改了，只需要发布修改的文件名称，对于没有修改的文件，则使用浏览器缓存，提高页面的性能。

### 文件指纹如何生成

- Hash：和整个项目的构建相关，只要项目文件有修改，整个项目构建的hash值就会更改。compile对象,complation???对象变化

- Chunkhash:和webpack打包的chunk有关，不同的entry会生成不同的chunkhash值。【chunk指的是模块】。对于js文件采用chunkhash。对于模块之间的关系进行联系。

- Contenthash:根据文件内容来定义hash，文件内容不变，则contenthash不会变。既有css资源和js资源。css根据内容生成hash。根据文件名联系文件内容

PS: js使用chunkhash时为了便于寻找资源,js的资源关联度更高；而css采用content hash是因为css一般根据不同的页面书写，css的资源关联度不高，不必在乎其他资源修改；chunkhash不能与热更新HMR一起使用；js没有contenthash

### 文件指纹设置

```js
module.exports = {
    entry:{
        app:'./src/app.js',
        search:'./src/search.js'
    },
    output:{
        filename:'[name][chunkhash:8.js]',
        path:__dirname+'/dist'
    },
    plugins:[
        new MiniCssExtractPlugin({
            filename:`[name][contenthash:8].css`
        })
    ]
}
```

PS:hash有32位 [chunkhash:8]默认取前8位

### 图片的文件指纹设置

> 设置file-loader的name,使用[hash]

| 占位符名称    | 含义                         |
| ------------- | ---------------------------- |
| [ext]         | 资源后缀名                   |
| [name]        | 文件名称                     |
| [path]        | 文件的相对路径               |
| [folder]      | 文件所在文件夹               |
| [contenthash] | 文件内容hash，默认md5生成    |
| [hash]        | 文件内容hash，默认md5生成    |
| [emoj]        | 一个睡觉的代指文件内容的emoj |



## html、css、js代码压缩

## 实验

[实验01 解析es6]()

[实验02 解析React JSX]()

[实验03 解析静态资源css、less、图片以及字体](解析静态资源css、leass、图片以及字体.md)





