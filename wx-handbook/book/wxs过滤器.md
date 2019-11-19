# wxs 过滤器

> wxs 主要作用是对显示的数据进行简单的处理。在微信小程序中，不可以通过\{\{formatData(varName)\}\}去实时格式化数据，但是 wxs 弥补了这种不足。wxs 可以简化代码，减少代码数量，使代码更有通用性。

## wxs 的写法

推荐使用第二种，有助于代码分离和维护。

写法一:直接写在 wxml 中，直接调用就好

```
//	wxml文件
<wxs module="mytest">
    function toUpper(str){
    	return str.toUpperCase();
	}

	function printMyName(){
        console.log("my name is vine")
    }

	var initData = "0.00";

	module.exports = {
        toUpper: toUpper,
        printMyName: printMyName,
        initData: initData
    }
</wxs>
<view>{{mytest.toUpper("a")}}</view>
<view bindtap="{{mytest.printMyName}}">点击我</view>
<view>{{mytest.initData}}</view>
```

第二种：写成单独的 wxs 文件并在 wxml 中引入

```
//	wxs文件 test.wxs
function toUpper(str){
    	return str.toUpperCase();
	}

function printMyName(){
    console.log("my name is vine")
}

var initData = "0.00";

module.exports = {
    toUpper: toUpper,
    printMyName: printMyName,
    initData: initData
}
//	wxml文件
//	引用
<wxs src="test.wxs" module="mytest" />
<view>{{mytest.toUpper("a")}}</view>
<view bindtap="{{mytest.printMyName}}">点击我</view>
<view>{{mytest.initData}}</view>
```

## wxs 的注意点

- 只支持 es5 语法，不支持 es6 语法

- 数据类型只有 number、string、boolean、object、function、array、data、regexp 类型，没有 null 和 undefined

- 在 wxs 文件中可以引用其他的 wxs 文件，但是只能使用 require 引入

- wxs 文件中不能像 js 一样使用正则，如果要使用正则，要使用小程序独有的`getRegExp`
