# javascript、es6、es7、typescript 等

## javascript

### js 优化

- 尽可能少的声明变量
- 尽量减少闭包的使用
- 尽量少使用 for..in(效率低)
- 尽量少使用 dom 操作
- 减少代码重用，尽量封装成函数和类
- 代码压缩，文件合并

### 引入脚本的`script`标签，加入 defer 和 async 的作用与区别

```
<script src="script.js"></script>
<script async src="script.js"></script>
<script defer src="script.js"></script>
```

- 不加 defer 或 async:解析 html 文档时，遇到 script 标签会停止 html 标签，下载并执行 script 引入的 js 脚本后，再加载 html
- 加 async: 解析 html 文档时，遇到 script 标签下载 script 引入的脚本。下载完成之后，停止 html 解析，执行 js 脚本，执行完毕后继续解析 html 文件。
- 加 defer:解析 html 文档时，遇到 script 标签下载 script 引入的脚本。不执行 js 脚本，直至 html 文档解析完毕。
  ![defer和async的区别](https://i.imgur.com/gHAdjeg.png)

### Javascript 中，有一个函数，执行时对象查找时，永远不会去查找原型，这个函数是？

hasOwnProperty

### new 操作符具体干了什么呢?

1. 创建一个空对象，并且 this 变量引用该对象，同时还继承了该函数的原型。
2. 属性和方法被加入到 this 引用的对象中。
3. 新创建的对象由 this 所引用，并且最后隐式的返回 this 。

### 如何判断一个对象是否属于某个类？

```
使用instanceof （待完善）

if(a instanceof Person){
    alert('yes');
}
```

### eval 是做什么的?

它的功能是把对应的字符串解析成 JS 代码并运行；
应该避免使用 eval，不安全，非常耗性能（2 次，一次解析成 js 语句，一次执行）。

### 数组类型转变

```
["1","2","3"].map(Number) // 字符串类型转为数字
[1,2,3].map(String) // 数字类型转字符串

```

#### 其他

["1", "2", "3"].map(parseInt) 答案是多少？
[1, NaN, NaN] 因为 parseInt 需要两个参数 (val, radix)，其中 radix 表示解析时用的基数。map 传了 3 个 (element, index, array)，对应的 radix 不合法导致解析失败。

### 如何创建一个对象? （画出此对象的内存图 ) => 如何创建一个类

**此处应该使用 es6 创建**

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
  this.sing = function() {
    alert(this.name);
  };
}
let person = new Person();
```

```js
let speak = class {
  constructor(name) {
    this.name = name;
  }
  sayName() {
    console.log(`Hello , My name is ${this.name}`);
  }
};
let me = new speak('vinr');
me.sayName();
```

### documen.write 和 innerHTML 的区别

document.write 只能重绘整个页面
innerHTML 可以重绘页面的一部分

### javascript 语句书写规范

1. 不要在同一行声明多个变量。
2. 请使用 ===/!==来比较 true/false 或者数值
3. 使用对象字面量替代 new Array 这种形式
4. 不要使用全局函数。
5. Switch 语句必须带有 default 分支
6. 函数不应该有时候有返回值，有时候没有返回值。
7. For 循环必须使用大括号
8. If 语句必须使用大括号
9. for-in 循环中的变量 应该使用 var 关键字明确限定作用域，从而避免作用域污染。

### JavaScript 原型，原型链 ? 有什么特点？

1.JS 中每个函数都存在有一个原型对象属性 prototype。并且所有函数的默认原型都是 Object 的实例。

2.每个继承父函数的子函数的对象都包含一个内部属性*proto*。该属性包含一个指针，指向父函数的 prototype。若父函数的原型对象的*proto*属性为再上一层函数。在此过程中就形成了原型链。

3.原型链实现了继承。原型链存在两个问题：a 包含引用类型值的原型属性会被所有实例共享。b 在创建子类型时，无法向超类型的构造函数中传递参数。

### 定时器,任务队列

定时器的任务队列排在最后

```
console.log(1);
setTimeout(function () {
    console.log(2);
}, 1000);
setTimeout(function () {
    console.log(3);
}, 0);
console.log(4);
1,4,3,2
```

```
var arr = [1, 2, 3];
for (var i = 0; i < arr.length; i++) {
setTimeout(function () {
    console.log(i);
}, 0);
}
3,3,3
```

### 获取一个元素到顶部的距离

```js
document.documentElement.scrollTop;
```

### getBoundingClientRect 获取的 top 和 offsetTop 获取的 top 区别

### 函数柯里化

#### 什么是函数柯里化?

#### 哪些地方用到了函数柯里化?

### 如何实现继承

- 构造函数
- 原型链
- extends

### 如何自定义事件

自定义事件的代码如下:

```
 var myEvent = new Event('clickTest');
    element.addEventListener('clickTest', function () {
        console.log('smyhvae');
    });

	//元素注册事件
    element.dispatchEvent(myEvent); //注意，参数是写事件对象 myEvent，不是写 事件名 clickTest
```

### 内存泄漏

内存泄漏指任何对象在您不再拥有或需要它之后仍然存在。

垃圾回收器定期扫描对象，并计算引用了每个对象的其他对象的数量。如果一个对象的引用数量为 0（没有其他对象引用过该对象），或对该对象的惟一引用是循环的，那么该对象的内存即可回收。
JavaScript 中最常用的垃圾收集方式是标记清除(mark-and-sweep)。当变量进入环境（例如，在函数中声明一个变量）时，就将这个变量标记为“进入环境”。从逻辑上讲，永远不能释放进入环境的变量所占的内存，因为只要执行流进入相应的环境，就可能用到它们。而当变量离开环境时，这将其 标记为“离开环境”。

常见内存泄漏的原因
虽然 js 会自动垃圾收集，但是如果代码写法不当，会让变量一直处于“进入环境”的环境，无法被回收。
以下情况后造成内存泄漏

1. 意外创建的全局变量，挂载在了 window 上
2. 被闭包所引用
3. dom 清空或删除，事件未清理
4. 未销毁定时器

setTimeout 的第一个参数使用字符串而非函数的话，会引发内存泄漏。
闭包、控制台日志、循环（在两个对象彼此引用且彼此保留时，就会产生一个循环）

### 垃圾回收机制

垃圾回收器会每隔一段时间找出那些不再使用的内存，然后为其释放内存
一般使用标记清除方法 当变量进入环境标记为进入环境，离开环境标记为离开环境
还有引用计数方法堆栈
stack 为自动分配的内存空间，它由系统自动释放；而 heap 则是动态分配的内存，大小不定也不会自动释放
基本数据类型存放在栈中
引用类型 存放在堆内存中，首先从栈中获得该对象的地址指针，然后再从堆内存中取得所需的数据

### 如何判断当前脚本运行在浏览器还是 node 环境中？

通过判断 Global 对象是否为 window，如果不为 window，当前脚本没有运行在浏览器中

### 异步加载 js 脚本的方式

- defer,只支持 ie,延迟
- async
- 创建 script,插入到 dom 中，加载完毕后 callback

### 事件冒泡

### 事件委托

利用冒泡原理，把时间加到父级上，触发执行效果
可以大量节省内存占用，减少事件注册
可以方便地动态添加和修改元素，不需要因为元素的改动而修改时间绑定

事件委托利用事件冒泡,只指定一个事件处理程序，就可以管理某一类型的所有事件。使用事件委托可以节省内存。

```
<ul>
  <li>1</li>
  <li>2</li>
  <li>3</li>
  <li>4</li>
</ul>

document.querySelector('ul').onclick=(event)=>{
  let target=event.target;
  if(target.nodeName==="Li"){
    console.log(target.innerHTML)
  }
}
```

### 事件循环

事件循环是一个单线程循环，用于监视调用堆栈并检查是否有工作即将在任务队列中完成。如果调用堆栈为空并且任务队列中有回调函数，则将回调函数出退出并推送到调用堆栈中执行。

### target 和 currentTarget 的区别

> 对多个元素做同一事件绑定

- event.target  
  返回触发事件的元素
- event.currentTarget
  返回绑定事件的元素

### prototype 和**proto**的关系

所有对象都有**proto**属性，它指向 Object.prototype。prototype 是原生 object 对象的属性。\_\_proto 是实例化后对象的属性.

```
let obj = {};
obj.__proto__ === Object.prototype
```

Object.prototype.**proto**指向 null

### 原型链

https://zhuanlan.zhihu.com/p/23090041

```
function foo(){};

foo.prototype.z = 3;

var obj = new foo();
obj.x = 1;
obj.y = 2;

obj.x //1
obj.y //2
obj.z //3
```

### 原型继承

所有的 JS 对象都有一个 prototype 属性，指向它的原型对象。当试图访问一个对象的属性时，如果没有在该对象上找到，它还会搜寻该对象的原型，以及该对象的原型的原型，依次层层向上搜索，直到找到一个名字匹配的属性或到达原型链的末尾。

### 继承

```
function SuperType(name) {
    this.name = name
    this.colors = ['red']
}

SuperType.prototype.sayName = function() {
    console.log(this.name)
}
// 继承实例属性
function SubType(name, age) {
    SuperType.call(this, name)
    this.age = age
}

function inheritPrototype(subType, superType) {
    let prototype = Object.create(superType.prototype)
    prototype.constructor = subType
    subType.prototype = prototype
}
// 继承原型方法
inheritPrototype(SubType, SuperType)

// 定义自己的原型方法
SubType.prototype.sayAge = function() {
    console.log(this.age)
}
```

### 闭包

变量可以分为全局变量或者局部变量。闭包就是一个函数引用另一个函数的变量，因为变量被引用所以不会被回收，因此可以用来封装一个私有变量。
闭包就是子函数可以使用父函数的局部变量和参数，还有父函数的参数。
闭包就是在提供了一个在外部访问另一个函数内部局部变量的方式。

```
执行say667()后,say667()闭包内部变量会存在,而闭包内部函数的内部变量不会存在.使得Javascript的垃圾回收机制GC不会收回say667()所占用的资源，因为say667()的内部函数的执行需要依赖say667()中的变量。这是对闭包作用的非常直白的描述.

function say667() {
// Local variable that ends up within closure
var num = 666;
var sayAlert = function() { alert(num); }
num++;
return sayAlert;
}

var sayAlert = say667();
sayAlert()//执行结果应该弹出的667
```

作用域问题:js 函数的子函数可以直接读取父函数的变量，但是父函数不可以。闭包定义在一个函数的内部，这个函数可以读取父函数的变量。

- 用途:
  - 读取函数内部的变量
  - 让变量保存在内存中:将子函数设置为全局函数，那么父函数运行之后的结果，会被保存在内存中，不会被垃圾回收机制回收。
- 注意点:
  - 由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包，否则会造成网页的性能问题，在 IE 中可能导致内存泄露。解决方法是，在退出函数之前，将不使用的局部变量全部删除。
  - 闭包会在父函数外部，改变父函数内部变量的值。所以，如果你把父函数当作对象（object）使用，把闭包当作它的公用方法（Public Method），把内部变量当作它的私有属性（private value），这时一定要小心，不要随便改变父函数内部变量的值。

### 深拷贝

对象自己有相应的内存地址，而不是与原来的对象共享内存地址。

```
let o1 = {a:{
    b:1
  }
}
let o2 = JSON.parse(JSON.stringify(o1))
```

缺点：JSON 不支持函数、引用、undefined、RegExp、Date……

另一种方法

```
function deepCopy(s) {
    const d = {}
    for (let k in s) {
        if (typeof s[k] == 'object') {
            d[k] = deepCopy(s[k])
        } else {
            d[k] = s[k]
        }
    }

    return d
}
```

3. 尾递归拷贝

```
 function clone(object){
	     var object2
	     if(! (object instanceof Object) ){
	         return object
	     }else if(object instanceof Array){
	         object2 = []
	     }else if(object instanceof Function){
	         object2 = eval(object.toString())
	     }else if(object instanceof Object){
	         object2 = {}
	     }
	     你也可以把 Array Function Object 都当做 Object 来看待，参考 https://juejin.im/post/587dab348d6d810058d87a0a
	     for(let key in object){
	         object2[key] = clone(object[key])
	     }
	     return object2
	 }
```

### 数组去重

1. 一维数组去重

```
function unique (arr) {
   return [...new Set(arr)]
}
```

```
 var a = [4,2,5,6,3,4,5]
 var hashTab = {}
 for(let i=0; i<a.length;i++){
     if(a[i] in hashTab){
         // 什么也不做
     }else{
         hashTab[ a[i] ] = true
     }
 }
 //hashTab: {4: true, 2: true, 5: true, 6:true, 3: true}
 console.log(Object.keys(hashTab)) // ['4','2','5','6','3']
```

2. 二维数组去重

```
返回一维数组:
[...new Set(student.map(({ sex }) => sex))];
返回二维数组:
getUniqueArray(array, item){
    let uniqueArray = [];
    for (let i = 0; i < array.length; i++) {
      let flag = true;
      for (let j = 0; j < uniqueArray.length; j++) {
        if ((uniqueArray[j][item] === array[i][item])) {
          flag = false;
        }
      }
      if (flag) {
        uniqueArray.push(array[i]);
      }
    }
    return uniqueArray;
  }
```

### 数据类型

- 基本数据类型：string number bool undefined null
- 引用数据类型：object
  另外，object 包括：数组、函数、正则、日期等对象。NaN 属于 number 类型。
  注意，数据类型里，没有数组。因为数组属于 object（一旦说数组、函数、正则、日期、NaN 是数据类型，直接 0 分）。

### 内置函数(原生函数)

- String
- Number
- Boolean
- Object
- Function
- Array
- Date
- RegExp
- Error
- Symbol

原始值 "I am a string" 并不是一个对象，它只是一个字面量，并且是一个不可变的值。 如果要在这个字面量上执行一些操作，比如获取长度、访问其中某个字符等，那需要将其 转换为 String 对象。 幸好，在必要时语言会自动把字符串字面量转换成一个 String 对象，也就是说你并不需要 显式创建一个对象。

### 图片懒加载

当页面滚动的时间被触发->执行加载图片操作->判断图片是否在可视区域内->在，则动态将 data-src 的值赋予该图片

### 实现 add 函数,让 add(a)(b)和 add(a,b)两种调用结果相同

> 参照函数柯里化

```js
//	方法一:判断参数的个数，使用高阶函数
function add(a, b) {
  if (arguments.length === 2) {
    return a + b;
  } else {
    return function(b) {
      return a + b;
    };
  }
}
console.log(add(2, 3));
console.log(add(2)(3));

```

### 事件绑定的方式

- 嵌入 dom

```
<button onclick="func()">click</button>
```

- 直接绑定

```
let btn = document.getElementsByTagName('button')[0];
btn.onclick=()=>{};
```

- 事件监听

```
let btn = document.getElementsByTagName('button')[0];
btn.addEventListener('click',()=>{})
```

### 判断数组的方法

```js
Array.isArray();
// 是否为数组
function isArray(obj) {
  return Object.prototype.toString.call(obj) === '[object Array]';
}
```

### 函数防抖和函数节流

函数防抖是指频繁触发的情况下，只有足够的空闲时间，才执行代码一次
函数防抖的要点，也是要一个 setTImeout 来辅助实现。延迟执行需要跑的代码
如果方法多次触发，则要把上次记录的延迟执行代码用 clearTimeout 清掉，重新开始
如果计时完毕，没有方法进来访问触发，则执行代码

```
var time = false;
document.getElementById(‘debounce’,onScrll = function(){
    clearTimeout(timer);
    timer = setTimeout(function(){
        console.log('111')
    }, 300);
}
```

### js 中万物皆对象你认为对吗?

我认为是对的 在 JS 中有原生函数、基本数据类型，它们的原型最终还是对象。

### 多个页面之间如何进行通信

- cookie
- web worker
- localeStorage 和 sessionStorage

### css 动画和 js 动画的差异

1. 代码复杂度，js 动画代码相对复杂一些
2. 动画运行时，对动画的控制程度上，js 能够让动画，暂停，取消，终止，css 动画不能添加事件
3. 动画性能看，js 动画多了一个 js 解析的过程，性能不如 css 动画好

### 使用 js 取出字符串空格

去除所有空格

```js
str.replace(/\s/g, '');
```

去除两边空格

1. js 方式

```
str.trim()
```

2. 正则方式

```
 function trim(string) {
        return string.replace(/^\s+|\s+$/g, '')
    }
```

3. es6 方法

```js
function trimStr(str) {
  let strArr = str.split(' ');
  return strArr.filter(a => a !== '').join('');
}
console.log(trimStr(' Hel  lo   world! '));
```

### new 一个对象经历了什么

```
function Test(){}
const test = new Test()
```

1. 创建一个新对象：

```
const obj = {}
```

2. 设置新对象的 constructor 属性为构造函数的名称，设置新对象的**proto**属性指向构造函数的 prototype 对象

```
obj.constructor = Test
obj.__proto__ = Test.prototype
```

3. 使用新对象调用函数，函数中的 this 被指向新实例对象

```
Test.call(obj)
```

4. 将初始化完毕的新对象地址，保存到等号左边的变量中。

### 如何实现文件断点续传

断点续传最核心的内容就是把文件“切片”然后再一片一片的传给服务器，但是这看似简单的上传过程却有着无数的坑。

首先是文件的识别，一个文件被分成了若干份之后如何告诉服务器你切了多少块，以及最终服务器应该如何把你上传上去的文件进行合并，这都是要考虑的。

因此在文件开始上传之前，我们和服务器要有一个“握手”的过程，告诉服务器文件信息，然后和服务器约定切片的大小，当和服务器达成共识之后就可以开始后续的文件传输了。

前台要把每一块的文件传给后台，成功之后前端和后端都要标识一下，以便后续的断点。

当文件传输中断之后用户再次选择文件就可以通过标识来判断文件是否已经上传了一部分，如果是的话，那么我们可以接着上次的进度继续传文件，以达到续传的功能。 有了 HTML5 的 File api 之后切割文件比想想的要简单的多的多。

只要用 slice 方法就可以了

```
var packet = file.slice(start, end);
```

参数 start 是开始切片的位置，end 是切片结束的位置 单位都是字节。通过控制 start 和 end 就可以是实现文件的分块

如

```
file.slice(0,1000);
file.slice(1000,2000);
file.slice(2000,3000);
// ......
```

在把文件切成片之后，接下来要做的事情就是把这些碎片传到服务器上。 如果中间掉线了，下次再传的时候就得先从服务器获取上一次上传文件的位置，然后以这个位置开始上传接下来的文件内容。

### bind、call、apply 的区别

call 和 apply 其实是一样的，区别就在于传参时参数是一个一个传或者是以一个数组的方式来传。
call 和 apply 都是在调用时生效，改变调用者的 this 指向。

```
let name = 'Jack'
const obj = {name: 'Tom'}
function sayHi() {console.log('Hi! ' + this.name)}

sayHi() // Hi! Jack
sayHi.call(obj) // Hi! Tom

```

bind 也是改变 this 指向，不过不是在调用时生效，而是返回一个新函数。

```
const newFunc = sayHi.bind(obj)
newFunc() // Hi! Tom
```

### 事件是？IE 与火狐的事件机制有什么区别？ 如何阻止冒泡？

我们在网页中的某个操作（有的操作对应多个事件）。例如：当我们点击一个按钮就会产生一个事件。是可以被 JavaScript 侦测到的行为。

事件处理机制：IE 是事件冒泡、火狐是 事件捕获；

event.stopPropagation()

### 请简述 JavaScript 中的 this

this 是 js 的一个关键字，随着函数使用场合不同，this 的值会发生变化。

但是有一个总原则，那就是 this 指的是调用函数的那个对象。

this 一般情况下：是全局对象 Global。 作为方法调用，那么 this 就是指这个对象

1.  fn() 里面的 this 就是 window

2.  fn() 是 strict mode，this 就是 undefined

3.  a.b.c.fn() 里面的 this 就是 a.b.c

4.  new F() 里面的 this 就是新生成的实例

5.  () => console.log(this) ，这个 this 指的是外面的 this。

JS 中的 this 是一个相对复杂的概念，不是简单几句能解释清楚的。粗略地讲，函数的调用方式决定了 this 的值。我阅读了网上很多关于 this 的文章，Arnav Aggrawal 写的比较清楚。this 取值符合以下规则：

1. 在调用函数时使用 new 关键字，函数内的 this 是一个全新的对象。
2. 如果 apply、call 或 bind 方法用于调用、创建一个函数，函数内的 this 就是作为参数传入这些方法的对象。
3. 当函数作为对象里的方法被调用时，函数内的 this 是调用该函数的对象。比如当 obj.method()被调用时，函数内的 this 将绑定到 obj 对象。
4. 如果调用函数不符合上述规则，那么 this 的值指向全局对象（global object）。浏览器环境下 this 的值指向 window 对象，但是在严格模式下('use strict')，this 的值为 undefined。
5. 如果符合上述多个规则，则较高的规则（1 号最高，4 号最低）将决定 this 的值。
6. 如果该函数是 ES2015 中的箭头函数，将忽略上面的所有规则，this 被设置为它被创建时的上下文。

### 题目:考察变量定义提升、this 指针指向、运算符优先级、原型、全局变量、变量污染、对象属性、原型属性优先

```js
function Foo() {
    getName = function () { alert (1); };
    return this;
}
Foo.getName = function () { alert (2);};    //Foo函数上存储的静态属性
Foo.prototype.getName = function () { alert (3);};
var getName = function () { alert (4);};
function getName() { alert (5);}

//请写出以下输出结果：
Foo.getName(); 2 未实例化对象，所以调用的是静态方法
getName(); 4
Foo().getName(); 1
getName(); 1 上层的 Foo().getName 把 var getName 重写了。
new Foo.getName(); 2 getName属性，没有重新new对象
new Foo().getName(); 3 new 了一个 foo 对象，定义了一个 getName 方法。优先采用原型链方法
new new Foo().getName(); 3 new 了一个 foo 对象，定义了一个 getName 方法。优先采用原型链方法
```

- Foo.getName
  访问 Foo 函数上存储的静态属性，结果是 2。
  参考

```
function User(name) {
	var name = name; //私有属性
	this.name = name; //公有属性
	function getName() { //私有方法
		return name;
	}
}
User.prototype.getName = function() { //公有方法
	return this.name;
}
User.name = 'Wscats'; //静态属性
User.getName = function() { //静态方法
	return this.name;
}
var Wscat = new User('Wscats'); //实例化
```

注意:

- 调用公有方法，公有属性，我们必需先实例化对象，也就是用 new 操作符实化对象，就可构造函数实例化对象的方法和属性，并且公有方法是不能调用私有方法和静态方法的
- 静态方法和静态属性就是我们无需实例化就可以调用
- 而对象的私有方法和属性,外部是不可以访问的

* getName();
  结果是 5，优先访问 function getName()
* 变量提升，函数声明会被提升到作用域最前面
* 函数表达式创建的函数是在运行时赋值，最后等到表达式赋值完成后才能调用.

* Foo().getName();
  结果是 1,访问 Foo()函数的 getName()方法.注意此处的 Foo()函数的 getName 没有用 var 或者 Let 声明,所以,getName 变为了全局变量。这个时候,getName 将全局的 getName 变量重写。
  Foo 执行后把全局的 getName 函数重写了一遍.
  注意,Foo()函数中的 this 指向的是 window 对象，也就是说 Foo 函数，返回的是 windows 对象，相当于执行 window.getName();this 的指向由函数的调用方式决定。

* getName
  结果是 1,上层的 Foo().getName 把 var getName 重写了。
* new Foo.getName();
  结果是 2
  new Foo;
  Foo.getName();

* new Foo().getName();
  (new Foo()).getName();
  结果是 3
  new 了一个 foo 对象，定义了一个 getName 方法。优先采用原型链方法

* new new Foo().getName();
  结果是 3
  new ((new Foo()).getName)();

## es6/es7

### 实现 promise.finally

finally 方法用于指定不管 Promise 对象最后状态如何，都会执行的操作，使用方法如下：

```js
Promise
    .then(result => { ··· })
    .catch(error => { ··· })
    .finally(() => { ··· })
```

finally 的特点：不接受任何的参数
finally 本质上是 then 方法的特性

```js
Promise.prototype.finally = function(callback) {
  let P = this.constructor;
  return this.then(
    value => P.resolve(callback()).then(() => value),
    reason =>
      P.resolve(callback()).then(() => {
        throw reason;
      })
  );
};
```

### const 常量是否能修改

- 如果是值类型，值不可变
- 如果是引用类型，比如对象、数组等，地址不可变，属性值可以修改
- const 的原理是引用地址不变

### 介绍 promise

promise 是一个异步编程模型。有三种状态：pending(进行中)，resolved(已完成)和 rejected(失败)

有了 promise 对象，就可以将异步操作以同步操作的流程表示出来，避免了层层嵌套的回调函数

### let 和 const 的区别

- let 声明的变量可以改变，值和类型都可以改变，没有限制
- const 声明的变量不得改变值

### class

https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Classes

### ES6 的新特性有哪些?

- 块级作用域：使用 let 和 const 代替 var,防止变量提升
- 函数扩展(扩展运算符、默认参数、箭头函数)
- 对象扩展
- 解构
- set 和 map
- 迭代器和生成器
- 类
- 异步 promise
- 模块化

### 箭头函数与匿名函数的区别

箭头函数的匿名函数的区别是，箭头函数内部的 this 是词法作用域，由上下文确定。  
普通 this 是动态作用域；箭头函数的 this 指向词法作用域

```
var obj1 = {
    birth: 1990,
    getAge: function (year) {
        let fn=function(y){
            return y - this.birth; // this指向window或undefined
        };
        return fn(year);
    }
};

var obj2 = {
    birth: 1990,
    getAge: function (year) {
        var fn = (y) => y - this.birth; // this.birth为1990
        return fn(year);
    }
};
```

## 介绍下 Set、Map 的区别？

应用场景 Set 用于数据重组，Map 用于数据储存

Set：

（1）成员不能重复
　　（2）只有键值没有键名，类似数组
　　（3）可以遍历，方法有 add, delete,has

Map:

（1）本质上是健值对的集合，类似集合
　　（2）可以遍历，可以跟各种数据格式转换

## setTimeout、Promise、Async/Await 的区别

事件循环中分为宏任务队列和微任务队列

其中 setTimeout 的回调函数放到宏任务队列里，等到执行栈清空以后执行

promise.then 里的回调函数会放到相应宏任务的微任务队列里，等宏任务里面的同步代码执行完再执行

async 函数表示函数里面可能会有异步方法，await 后面跟一个表达式

async 方法执行时，遇到 await 会立即执行表达式，然后把表达式后面的代码放到微任务队列里，让出执行栈让同步代码先执行

## 下面 Set 结构，打印出的 size 值是多少

```js
let s = new Set();
s.add([1]);
s.add([1]);
console.log(s.size);
```

两个数组[1]并不是同一个值，它们分别定义的数组，在内存中分别对应着不同的存储地址，因此并不是相同的值

都能存储到 Set 结构中，所以 size 为 2

## 设计一个对象，键名的类型至少包含一个 symbol 类型，并且实现遍历所有 key

```js
let name = Symbol('name');
let product = {
  [name]: '洗衣机',
  price: 799
};
Reflect.ownKeys(product);
```

### promise

#### promise 的使用

then：

```
	$.ajax(...).then(成功函数, 失败函数)
```

链式 then：

```
 	$.ajax(...).then(成功函数, 失败函数).then(成功函数2, 失败函数2)
```

如何自己生成 Promise 对象：

```
let promise = new Promise(function(resolved,reject){
    resolved();
});
//  已完成状态
promise.then(function(){
    console.log("Resolved");
});
//  拒绝状态:捕捉错误
promise.catch(function(err){
    console.log(error)
})
	function xxx(){
      return new Promise(function(resolve, reject){
          setTimeout(()=>{
              resolve() 或者 reject()
          },3000)
      })
  }
  xxx().then(...)
```

#### promise 的状态

#### Promise 中 reject 和 catch 处理上有什么区别

reject 是用来抛出异常，catch 是用来处理异常

reject 是 Promise 的方法，而 catch 是 Promise 实例的方法

reject 后的东西，一定会进入 then 中的第二个回调，如果 then 中没有写第二个回调，则进入 catch

网络异常（比如断网），会直接进入 catch 而不会进入 then 的第二个回调

#### setTimeout(0)和一个 promise 哪个先执行

任务队列可以有多个，promise 的任务队列，优先级更高

### asynv/await

目的：把异步代码写成同步代码的形式。

```
let promise = new Promise((resolve, reject) => {
        //进来之后，状态为pending
        console.log('111');  //这一行代码是同步的
        //开始执行异步操作（这里开始，写异步的代码，比如ajax请求 or 开启定时器）
        if (异步的ajax请求成功) {
            console.log('333');
            resolve();//如果请求成功了，请写resolve()，此时，promise的状态会被自动修改为fullfilled
        } else {
            reject();//如果请求失败了，请写reject()，此时，promise的状态会被自动修改为rejected
        }
    })
    console.log('222');

    //调用promise的then()
    promise.then(() => {
            //如果promise的状态为fullfilled，则执行这里的代码
            console.log('成功了');
        }
        , () => {
            //如果promise的状态为rejected，则执行这里的代码
            console.log('失败了');

        }
    )
```

有了 await 之后，可以直接替换掉 then。如下：

```
 function returnPromise(){
     return new Promise( function(resolve, reject){
         setTimeout(()=>{
             resolve('success')
         },3000)
     })
 }

 returnPromise().then((result)=>{
     result === 'success'
 })

 var result = await returnPromise()
 result === 'success'
```

### 理解 async/await 以及对 Generator 的优势

async await 是用来解决异步的，async 函数是 Generator 函数的语法糖

使用关键字 async 来表示，在函数内部使用 await 来表示异步

async 函数返回一个 Promise 对象，可以使用 then 方法添加回调函数

当函数执行的时候，一旦遇到 await 就会先返回，等到异步操作完成，再接着执行函数体内后面的语句

async 较 Generator 的优势：

（1）内置执行器。Generator 函数的执行必须依靠执行器，而 Aysnc 函数自带执行器，调用方式跟普通函数的调用一样

（2）更好的语义。async 和 await 相较于 \* 和 yield 更加语义化

（3）更广的适用性。yield 命令后面只能是 Thunk 函数或 Promise 对象，async 函数的 await 后面可以是 Promise 也可以是原始类型的值

（4）返回值是 Promise。async 函数返回的是 Promise 对象，比 Generator 函数返回的 Iterator 对象方便，可以直接使用 then() 方法进行调用

### forEach、for in、for of 三者区别

forEach 更多的用来遍历数组

for in 一般常用来遍历对象或 json

for of 数组对象都可以遍历，遍历对象需要通过和 Object.keys()

for in 循环出的是 key，for of 循环出的是 value

### async 和 await

正常情况下，await 命令后面是一个 Promise 对象，返回该对象的结果。如果不是 Promise 对象，就直接返回对应的值（相当于直接 Promise.resolve）。

```js
//  例子1
async function async1() {
  console.log('async1 start');
  await async2();
  console.log('async1 end');
}
async function async2() {
  console.log('async2');
}
console.log('script start');
setTimeout(function() {
  console.log('setTimeout');
}, 0);
async1();
new Promise(function(resolve) {
  console.log('promise1');
  resolve();
}).then(function() {
  console.log('promise2');
});
console.log('script end');
```

```js
//例子2
async function async1() {
  console.log('async1 start');
  await async2();
  console.log('async1 end');
}
function async2() {
  // 去掉了 async 关键字
  console.log('async2');
}
console.log('script start');
setTimeout(function() {
  console.log('setTimeout');
}, 0);
async1();
new Promise(function(resolve) {
  console.log('promise1');
  resolve();
}).then(function() {
  console.log('promise2');
});
console.log('script end');
```

### 如何解决地狱回调问题?

```javascript
//获得商品列表 实例化promise 并传入resolve 和 reject两个参数
  var getGoodsList = new Promise(function(resolve,reject){
      axios.get('/ggserver/api/products/list',{params})
        .then(function(res){
            if(res.data.code == '200'){
                resolve(res.data.result)      //成功
            }else{
                reject(res.data.errMsg)       //失败
            }
        })
  })
//我们在请求一个分类列表
var getGoodsType = new Promise(function(resolve,reject){
      axios.get('/ggserver/api/goodsType')
      .then(function(res){
           if(res.data.code == '200'){
                resolve(res.data.result)      //成功
            }else{
                reject(res.data.errMsg)       //失败
            }
      })
})
然后。在将获得的数据进行业务处理
getGoodsList.then(function(goodslistdata){
    //处理业务
}).catch(function(errMsg){
    //失败业务
    console.log('哎，goodslist运气不佳...')
})

getGoodsType.then(function(goodsTypedata){
    //处理业务
}).catch(function(errMsg){
    //失败业务
    console.log('哎，goodstyoe运气不佳...')
})

最后 我们通过promise.all()方法来 等列表 和 类型加载完 进行其他业务处理
Promise.all([getGoodsList, getGoodsType]).then(function([data1,data2]){
    console.log(data1,data2,'已经加载完成啦')
})

使用`Promise.all([request1,request2])`
```



## typescript

