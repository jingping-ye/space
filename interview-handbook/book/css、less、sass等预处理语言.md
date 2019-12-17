# css、less、sass 等预处理语言

## css

### 浏览器的兼容性写法

```sh
--webkit--
--moz--
--ms--
--o--
```

## 如何解决页面多次快速点击时出现蓝色背景的问题

只要禁止用户点击可以了，可以通过css和js两种方法解决

```css
//	css解决方法
element{
    user-select:none;
    -webkit-user-select:none;
    -moz-user-select:none;
    -ms-user-select:none;
}
```

```js
//	js解决方法
document.onselectstart = new Function("return false");
```



### 为什么要初始化 css 样式

不同的浏览器，标签的默认值是不一样的。如果没有对 css 初始化，将会出现浏览器之间页面的显示差异问题。

### 重置 css 和标准化 css 的区别是什么?你会选择哪种方式,为什么?

- 重置（Resetting）： 重置意味着除去所有的浏览器默认样式。对于页面所有的元素，像`margin`、`padding`、`font-size`这些样式全部置成一样。你将必须重新定义各种元素的样式。
- 标准化（Normalizing)： 标准化没有去掉所有的默认样式，而是保留了有用的一部分，同时还纠正了一些常见错误。

当需要实现非常个性化的网页设计时，我会选择重置的方式，因为我要写很多自定义的样式以满足设计需求，这时候就不再需要标准化的默认样式了。

### 盒模型:content-box 和 border-box，为什么看起来 content-box 更合理，但还是经常使用 border-box?

content-box 是 W3C 的标准盒模型 元素宽度+padding+border
border-box 是 ie 的怪异盒模型，他的元素宽度等于内容宽度 内容宽度包含了 padding 和 border
比如有时候在元素基础上添加内边距 padding 或 border 会将布局撑破 但是使用 border-box 就可以轻松完成

### 有什么不同的方式可以隐藏内容?

- visibility: hidden
- width: 0; height: 0
- position: absolute; left: -99999px
- text-indent: -9999px
- opacity:0

### css 优化

- 代码去重，相同属性使用 class
- 代码压缩:使用压缩工具
- 雪碧图
- 文件合并

### 实现两栏布局

- display:inline-block + float:right + width:50%;
- flex

```
* {
        margin: 0;
        padding: 0;
      }
      html,
      body {
        height: 100%;
      } //  这里是关键
      #container {
        display: flex;
        flex-flow: row;
        height: 100%;   // 这里是关键
      }
      #left {
        flex: 1;
        background: red;
      }
      #right {
        flex: 1;
        background: green;
      }
```

### 实现三栏布局

- flex 实现

```
* {
        margin: 0;
        padding: 0;
      }
      html,
      body {
        height: 100%;
      }
      #container {
        display: flex;
        flex-flow: row;
        height: 100%;
      }
      #left {
        flex: 1;
        background: red;
      }
      #middle {
        flex: 1;
        background: yellow;
      }
      #right {
        flex: 1;
        background: green;
      }
```

- width:33.33%+float 实现

```
* {
        padding: 0;
        margin: 0;
      }
      html,
      body {
        height: 100%;
      }
      #container {
        height: 100%;
      }
      #left,
      #middle,
      #right {
        display: inline-block;
        width: 33.333%;
        height: 100%;
      }
      #left {
        background-color: red;
        float: left;
      }
      #middle {
        background-color: blue;
      }
      #right {
        background-color: green;
        float: right;
      }
```

### rem 和 em 的区别？

em 相对于父元素，rem 相对于根元素

### 清除浮动

- 利用 clear 属性进行清理 clear:both
- 利用 css 伪元素,使用 clearfix 类
- overflow:auto 或者 overflow:hidden

```
.clearfix:after {
    content: ".";
    height: 0;
    visibility: hidden;
    display: block;
    clear: both;
}
```

### display:none 和 visibility:hidden 的区别？

- display:none 隐藏对应的元素，在文档布局中不再给它分配空间，它各边的元素会合拢，就当他从来不存在。
- visibility:hidden 隐藏对应的元素，但是在文档布局中仍保留原来的空间。

### flex 的属性值

- flex 属性是 flex-grow,flex-shrink 和 flex-basis 的简写
- flex-grow 属性定义项目的放大比例，默认为 0
- flex-shrink 属性定义了项目的缩小比例，默认为 1
- flex-basis 属性定义了项目的固定空间

### 实现一个 div 从页面左上角到右下角的移动，有哪些方法，怎么实现?

- 使用 div.style.top 设定，加上定时器；要点：初始 top 必须写在 style 中.
- css3 animation 方法

### 居中显示

#### 水平居中显示

1. 使用 text-align

```javascript
<p>水平居中1</p>
p {
    text-align: center;
  }
```

2. 使用 margin:0 auto;

```html
<div id="align2">水平居中2</div>
#align2 { width: 200px; background-color: green; margin: 0 auto; }
```

3. 使用 flex

```
<div id="align5">水平居中5</div>
#align5 {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: blanchedalmond;
  }
```

#### 垂直居中显示

1. 不定宽高:使用 transform

```
<div id="align3">水平居中3</div>
#align3 {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: antiquewhite;
}
```

2. 定宽高:使用 top/left/bottom/right:0px;

```html
<div id="align4">水平居中4</div>
#align4 { position: absolute; top: 0; left: 0; right: 0; bottom: 0; margin: auto; background-color: aquamarine; width:
200px; height: 200px; }
```

3.文字使用line-height

```js
<div id="align">文字</div>
#align{
    height:100px;
	line-height:100px;
}
```



### @import 和 link 的区别

- link 属于 XHTML 标签，除了加载 CSS 外，还能用于定义 RSS, 定义 rel 连接属性等作用；而@import 是 CSS 提供的，只能用于加载 CSS;
- 页面被加载的时，link 会同时被加载，而@import 引用的 CSS 会等到页面被加载完再加载;
- import 是 CSS2.1 提出的，只在 IE5 以上才能被识别，而 link 是 XHTML 标签，无兼容问题;
- link 方式的优先级高于@import 的优先级

### 如果需要手动写动画，你认为最小时间间隔是多久？为什么?

多数显示器默认频率是 60Hz，即 1 秒刷新 60 次，所以理论上最小间隔为 1/60＊1000ms ＝ 16.7ms

### transition 和 margin 的百分比根据什么计算？

transition 是相对于自身；margin 相对于参照物

### css 盒模型

css 盒子模型分为两种 ie 盒子模型、标准 w3c 盒子模型;ie 的 content 部分包含了 border 和 padding。盒模型由内容(content)、填充(padding)、边界(margin)、边框(border)。

### display 的属性值

- none
- block
- inline
- inline-block
- table
- table-row
- table-cell
- list-item 象块类型元素一样显示，并添加样式列表标记。

### `inline`和`inline-block`有什么区别？

我把`block`也加入其中，为了获得更好的比较。

|                                 | `block`                                                     | `inline-block`                             | `inline`                                                     |
| ------------------------------- | ----------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------ |
| 大小                            | 填充其父容器的宽度。                                        | 取决于内容。                               | 取决于内容。                                                 |
| 定位                            | 从新的一行开始，并且不允许旁边有 HTML 元素（除非是`float`） | 与其他内容一起流动，并允许旁边有其他元素。 | 与其他内容一起流动，并允许旁边有其他元素。                   |
| 能否设置`width`和`height`       | 能                                                          | 能                                         | 不能。 设置会被忽略。                                        |
| 可以使用`vertical-align`对齐    | 不可以                                                      | 可以                                       | 可以                                                         |
| 边距（margin）和填充（padding） | 各个方向都存在                                              | 各个方向都存在                             | 只有水平方向存在。垂直方向会被忽略。 尽管`border`和`padding`在`content`周围，但垂直方向上的空间取决于'line-height' |
| 浮动（float）                   | -                                                           | -                                          | 就像一个`block`元素，可以设置垂直边距和填充。                |

### position 的属性值

经过定位的元素，其`position`属性值必然是`relative`、`absolute`、`fixed`或`sticky`。

- `static`：默认定位属性值。该关键字指定元素使用正常的布局行为，即元素在文档常规流中当前的布局位置。此时 top, right, bottom, left 和 z-index 属性无效。生成相对定位的元素，相对于其正常位置进行定位。
- `relative`：该关键字下，元素先放置在未添加定位时的位置，再在不改变页面布局的前提下调整元素位置（因此会在此元素未添加定位时所在位置留下空白）。
- `absolute`：不为元素预留空间，通过指定元素相对于最近的非 static 定位祖先元素的偏移，来确定元素位置。绝对定位的元素可以设置外边距（margins），且不会与其他边距合并。生成绝对定位的元素，相对于 static 定位以外的第一个父元素进行定位。
- `fixed`：不为元素预留空间，而是通过指定元素相对于屏幕视口（viewport）的位置来指定元素位置。元素的位置在屏幕滚动时不会改变。打印时，元素会出现在的每页的固定位置。fixed 属性会创建新的层叠上下文。当元素祖先的 transform 属性非 none 时，容器由视口改为该祖先。生成绝对定位的元素，相对于浏览器窗口进行定位。
- `sticky`：盒位置根据正常流计算(这称为正常流动中的位置)，然后相对于该元素在流中的 flow root（BFC）和 containing block（最近的块级祖先元素）定位。在所有情况下（即便被定位元素为 `table` 时），该元素定位均不对后续元素造成影响。当元素 B 被粘性定位时，后续元素的位置仍按照 B 未定位时的位置来确定。`position: sticky` 对 `table` 元素的效果与 `position: relative` 相同。

### css 选择器

#### 类别

1. id 选择器（ # myid）
2. 类选择器（.myclassname）
3. 标签选择器（div, h1, p）
4. 相邻选择器（h1 + p）
5. 子选择器（ul > li）
6. 后代选择器（li a）
7. 通配符选择器（ \* ）
8. 属性选择器（a[rel = "external"]）
9. 伪类选择器（a: hover, li: nth - child）

#### 优先级

important > 内联 > ID > 类 > 标签 | 伪类 | 属性选择 > 伪对象 > 继承 > 通配符

- 选择器越具体，优先级越高，比如#xxx 大于.yyy
- 同样的优先级，写在后面的覆盖前面的。
- color:red !important; 优先级最高

#### 新增选择器

- p:first-of-type 选择属于其父元素的首个<p>元素的每个<p>元素。
- p:last-of-type 选择属于其父元素的最后<p>元素的每个<p>元素。
- p:only-of-type 选择属于其父元素唯一的<p>元素的每个<p>元素。
- p:only-child 选择属于其父元素的唯一子元素的每个<p>元素。
- p:nth-child(2) 选择属于其父元素的第二个子元素的每个<p>元素。
- :enabled :disabled 控制表单控件的禁用状态。
- :checked 单选框或复选框被选中。

### bfc 及其工作原理

块格式上下文（BFC）是 Web 页面的可视化 CSS 渲染的部分，是块级盒布局发生的区域，也是浮动元素与其他元素交互的区域。

一个 HTML 盒（Box）满足以下任意一条，会创建块格式化上下文：

- `float`的值不是`none`.
- `position`的值不是`static`或`relative`.
- `display`的值是`table-cell`、`table-caption`、`inline-block`、`flex`、或`inline-flex`。
- `overflow`的值不是`visible`。

在 BFC 中，每个盒的左外边缘都与其包含的块的左边缘相接。

### css 样式继承

- 可继承样式:font-size、font-family、color、ul、li、dl、dd、dt
- 不可继承样式:border、padding、margin、width、height

### 雪碧图

雪碧图是把多张图片整合到一张上的图片。它被运用在众多使用了很多小图标的网站上（Gmail 在使用）。实现方法：

1. 使用生成器将多张图片打包成一张雪碧图，并为其生成合适的 CSS。
2. 每张图片都有相应的 CSS 类，该类定义了`background-image`、`background-position`和`background-size`属性。
3. 使用图片时，将相应的类添加到你的元素中。

好处：

- 减少加载多张图片的 HTTP 请求数（一张雪碧图只需要一个请求）。但是对于 HTTP2 而言，加载多张图片不再是问题。
- 提前加载资源，防止在需要时才在开始下载引发的问题，比如只出现在`:hover`伪类中的图片，不会出现闪烁。

### css 实现瀑布流

```
 column-count: 2; /*分几s列*/
  width: 100%;
  column-gap: 10px; /*列间距*/
```

### 实现超出字数省略号

- 单行

```
overflow: hidden;
text-overflow:ellipsis;
white-space: nowrap;
```

- 多行

```
display: -webkit-box;
-webkit-box-orient: vertical;
-webkit-line-clamp: 3; // 最多显示几行
overflow: hidden;
```

### 实现三角

```
.info-tab {
    position: relative;
}
.info-tab::after {
    content: '';
    border: 4px solid transparent;
    border-top-color: #2c8ac2;
    position: absolute;
    top: 0;
}

```



## 预处理语言

### 使用 css 预处理语言的优缺点

- 优点

  - 提高 CSS 可维护性。
  - 易于编写嵌套选择器。
  - 引入变量，增添主题功能。可以在不同的项目中共享主题文件。
  - 通过混合（Mixins）生成重复的 CSS。
  - 将代码分割成多个文件。不进行预处理的 CSS，虽然也可以分割成多个文件，但需要建立多个 HTTP 请求加载这些文件。
  - Less 用 JavaScript 实现，与 NodeJS 高度结合。

- 缺点：

  - 需要预处理工具。
  - 重新编译的时间可能会很慢。
  - 使用`@`作为前缀，容易与 css 关键字混淆，如 `@media`、`@import`、`@font-face`

### less

### sass



