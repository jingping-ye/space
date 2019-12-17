# html

## html5的离线缓存怎么使用及其工作原理

1. 离线存储
   在用户没有与因特网连接时，可以正常访问站点或应用，在用户与因特网连接时，更新用户机器上的缓存文件。
2. 离线存储的原理
   HTML5 的离线存储是基于一个新建的.appcache 文件的缓存机制(不是存储技术)，通过这个文件上的解析清单离线存储资源，这些资源就会像 cookie 一样被存储了下来。之后当网络在处于离线状态下时，浏览器会通过被离线存储的数据进行页面展示。
3. 如何使用

```js
// 检测是否支持离线存储,ie9以上支持
 if(window.applicationCache){
    alert("支持离线缓存");
}
else{
    alert("不支持离线缓存");
}
// 引入manifest文件
<!DOCTYPE html>
<html lang="en" manifest="test.manifest">
...
</html>
// 在mainfest文件中编写离线存储的资源
// 在离线状态下，操作window.applicationCache进行需求实现。
```

[Html5 离线缓存详细讲解 - ZQ 是水鱼 - 博客园](https://www.cnblogs.com/wuzhiquan/p/4844258.html)

### 语义化

#### 什么是语义化

使用带有清晰含义、符合内容的标签去展示内容。像 html5 的新的标签 header,footer,section 等就是语义化

#### 如何实现语义化

页头页脚分别用 header、footer，导航区用 nav 标签，段落用 p，边栏用 aside,主要内容要 main 标签

#### 语义化的好处

- 易于用户阅读，即使样式丢失，也能较好的展示页面
- 便于屏幕阅读器等辅助工具，帮助阅读障碍人群阅读
- 程序较为请求，有利于后期网站的维护
- 便于 seo 和搜索引擎根据标签确定关键字的权重

### html5 有哪些新特性、移除了那些元素？如何处理 HTML5 新标签的浏览器兼容问题？如何区分 HTML 和 HTML5?

#### 新特性

- 新的 DOCTYPE 声明<!DOCTYPE html>,不再是 sgml 的子集
- 完全支持 css3
- video 和 audio
- 本地(离线)存储，添加了 localstorage 长期存储数据，浏览器关闭后数据不丢失；添加了 sessionStorage 在浏览器关闭后自动删除
- 语义化标签，入 header、footer、nav、section、article
- canvas,添加了 video 和 audio 元素
- 新事件如 ondrag onresize
- 添加了一些表单控件，如 calendar、date、time、email、url、search
- 添加了新的技术,webworker, websocket, Geolocation

#### 移除的元素

- 纯表现的元素：basefont，big，center，font, s，strike，tt，u；
- 对可用性产生负面影响的元素：frame，frameset，noframes；

#### 处理兼容性问题

- IE8/IE7/IE6 支持通过 document.createElement 方法产生的标签，
  可以利用这一特性让这些浏览器支持 HTML5 新标签，
- 浏览器支持新标签后，还需要添加标签默认的样式：
- 当然最好的方式是直接使用成熟的框架、使用最多的是 html5shim 框架

```
<!--[if lt IE 9]>
<script> src="http://html5shim.googlecode.com/svn/trunk/html5.js"</script>
<![endif]-->
```

#### 如何区分 html5 与其他 html

doctype 声明、新增的标签，如 header 和 date 控件

### doctype

#### doctype 有多少种文档类型

- 该标签可声明三种 DTD 类型，分别表示严格版本、过渡版本以及基于框架的 HTML 文档
- HTML4.01 规定了三种文档类型：Strict, Transitional 以及 Frameset
- XHTML 1.0 规定了三种 XML 文档类型：Strict, Transitional 以及 Franmeset
- Standards（标准）模式（也就是严格呈现模式）用于呈现遵循最新标签的网页，而 Quirks（包容）模式（也就是松散呈现模式或者兼容模式）用于呈现为传统浏览器而设计的网页

#### doctype 的作用

- 声明文档:声明 html 页面是用哪个版本的 html 进行编写的
- 告知解析器采用什么 DTD(文档类型定义)来解析 html 文档

#### 为什么 html5 只用写<!doctype html>?

HTML5 不基于 SGML，因此不需要对 DTD 进行引用，但是需要 doctype 来规范浏览器的行为（让浏览器按照它们应该的方式来运行。

### 行内元素与块级元素

#### 行内元素

a b span img input select strong（强调的语气）

### 块级元素

div ul ol li dl dt dd h1 h2 h3 h4…p

#### 行内元素与块级元素的区别

- 行内元素：和其他元素都在一行上，高度、行高及外边距和内边距都不可改变，文字图片的宽度不可改变，只能容纳文本或者其他行内元素；其中 img 是行元素
- 块级元素：总是在新行上开始，高度、行高及外边距和内边距都可控制，可以容纳内敛元素和其他元素；行元素转换为块级元素方式：display：block；

### iframe 的缺点

- iframe 会阻塞主页面的 Onload 事件；
- iframe 和主页面共享连接池，而浏览器对相同域的连接有限制，所以会影响页面的并行加载。
  使用 iframe 之前需要考虑这两个缺点。如果需要使用 iframe，最好是通过 javascript
  动态给 iframe 添加 src 属性值，这样可以可以绕开以上两个问题。

### html5 的 form 如何关闭自动完成功能

给不想要提示的 form 或下某个 input 设置为 autocomplete=off

### img 中 title 和 alt 的区别

- title:鼠标移上去显示的文字，也可用于其他标签
- alt 图片丢失时显示的文字

### src 和 href 的区别

- src 用于引进图片、外部 js 脚本等资源。浏览器解析时，遇到 src 标签将会暂停其他资源的下载和处理，一直到资源加载、编译、执行完毕。
- href 用于外部链接、外部 css 样式文件等资源。浏览器对外部 css 文件解析时，会并行下载其他资源。

### reflow 和 repaint

#### reflow 和 repanit 是什么

- reflow
  当 DOM 节点的布局属性(位置和大小)发生变化时，浏览器会重新描绘该属性，这就叫做重排(reflow)。
- repaint
  当 DOM 节点的可见性属性发生改变时，浏览器会重新绘制该节点，这就叫做重绘(repaint)。
  PS:重排必然会引起重绘。

#### 什么操作会引起 reflow 和 repaint？

- 调整浏览器窗口的大小
- 进行删减、添加元素的 DOM 操作
- 字体大小和样式的改变
- 元素内容发生改变，尤其是输入控件
- hover 等动作产生的用户交互行为
- width、clientWidth、scrollTop 等计算行为

#### 如何降低 reflow 和 repaint 对性能的影响

- 使用 class 统一改变样式，避免逐条改变样式。
- 避免 clientWidth 和 scrollTop 的频繁操作。
- 对需要的元素使用绝对定位脱离文档流，避免父元素和后续元素的大量回流。
- 避免频繁的 DOM 操作。

### viewport 属性

```
<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">

```

- width 设置 layout viewport 的宽度，为一个正整数，或字符串"width-device"
- initial-scale 设置页面的初始缩放值，为一个数字，可以带小数
- minimum-scale 允许用户的最小缩放值，为一个数字，可以带小数
- maximum-scale 允许用户的最大缩放值，为一个数字，可以带小数
- height 设置 layout viewport 的高度，这个属性对我们并不重要，很少使用
- user-scalable 是否允许用户进行缩放，值为"no"或"yes", no 代表不允许，yes 代表允许这些属性可以同时使用，也可以单独使用或混合使用，多个属性同时使用时用逗号隔

### link 和 script 在浏览器中的位置

link 放在文档开头的 head 标签中，script 防止在 body 标签结束时。原因，css 文件是对页面样式的描述，先加载 css，可以给用户呈现一个体验感更高的网页。script 文件大多数时候是一些用户和网站之间的交互函数，script 加载时，会阻塞浏览器加载其他的网页资源，这样，可能会产生一个空白的页面给用户。script 中如果要进行 dom 操作，也要依赖于 body 中的 html 代码。所以，先加载 css 资源，最后再加载 script 资源。