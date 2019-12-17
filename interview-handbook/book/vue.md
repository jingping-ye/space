# vue

### vue 的生命周期

[API 文档](https://cn.vuejs.org/v2/api/#%E9%80%89%E9%A1%B9-%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E9%92%A9%E5%AD%90)
创建一个 Vue 实例，是一个漫长的过程，要经历初始化，数据合并，模板解析，数据渲染等等一系列过程。
所以，为了能实现在这个过程里面插入自己想要提前做的事情，就有了生命周期钩子函数。
beforecreated: el 和 data 并未初始化
created： 完成了 data 数据的初始化，el 没有
beforeMount：完成了 el 和 data 初始化
mounted：完成挂载，updated,destroyed

1. 创建前/后： 在 beforeCreate 阶段，vue 实例的挂载元素 el 和数据对象 data 都为 undefined，还未初始化，created 阶段，vue 实例的数据对象 data 有了，el 还没有；
2. 载入前/后：在 beforeMount 阶段，vue 实例的\$el 和 data 都初始化了，但还是挂载之前为虚拟的 dom 节点，data.message 还未替换。在 mounted 阶段，vue 实例挂载完成，data.message 成功渲染。
3. 更新前/后：当 data 变化时，会触发 beforeUpdate 和 updated 方法。
4. 销毁前/后：在执行 destroy 方法后，对 data 的改变不会再触发周期函数，说明此时 vue 实例已经解除了事件监听以及和 dom 的绑定，但是 dom 结构依然存在

### create 和 mounted 的区别

- create 只完成了 data 的初始化，没有完成 el 的初始化。而 mounted 的时候二者皆完成。

### 父子组件通信

vue：父组件是通过 props 属性给子组件通信，在子组件里面 emit，在父组件监听

### 兄弟组件通信

vuex 建立一个 vue 的实例，emit 触发时间 on 监听时间

### vue 的项目构建

- 按模块
- 模块下按照 vue 的架构分类，如图片、样式表、功能代码分类
- 功能代码按照功能组件化编写。

### vue 的特点

- 数据驱动、组件化、响应式
- 优点:数据和视图之间是同步的，无需认为干涉，所以开发者只需要关注业务逻辑，不需要手动操作 dom,不需要关注数据状态的同步问题。节省了很多精力。

### 双向绑定的实现原理

- 通过 mvvm
- Object.defineProperty( )
- 虚拟 DOM

### 什么是 mvvm

MVVM 最早由微软提出来，它借鉴了桌面应用程序的 MVC 思想，在前端页面中，把 Model 用纯 JavaScript 对象表示，View 负责显示，两者做到了最大限度的分离
把 Model 和 View 关联起来的就是 ViewModel。<br>
ViewModel 负责把 Model 的数据同步到 View 显示出来，还负责把 View 的修改同步回 Model<br>
View 和 Model 之间的同步工作完全是自动的，无需人为干涉（由 viewModel 完成，在这里指 VUE）<br>
因此开发者只需关注业务逻辑，不需要手动操作 DOM, 不需要关注数据状态的同步问题，复杂的数据状态维护完全由 MVVM 来统一管理<br>
mvc 的界面和逻辑关联紧密，数据直接从数据库读取，必须通过 controller 来承上启下，通信都是单向的
mvvm 的 view 和 viewModel 可以互相通信，界面数据从 viewmodel 中获取
Model 代表数据模型，数据和业务逻辑都在 Model 层中定义；
View 代表 UI 视图，负责数据的展示；
ViewModel 负责监听 Model 中数据的改变并且控制视图的更新，处理用户交互操作；
Model 和 View 并无直接关联，而是通过 ViewModel 来进行联系的，Model 和 ViewModel 之间有着双向数据绑定的联系。因此当 Model 中的数据改变时会触发 View 层的刷新，View 中由于用户交互操作而改变的数据也会在 Model 中同步。
这种模式实现了 Model 和 View 的数据自动同步，因此开发者只需要专注对数据的维护操作即可，而不需要自己操作 dom。

### vuex 作用 

[官方文档](https://cn.vuejs.org/v2/guide/components.html#%E9%80%9A%E8%BF%87-Prop-%E5%90%91%E5%AD%90%E7%BB%84%E4%BB%B6%E4%BC%A0%E9%80%92%E6%95%B0%E6%8D%AE)

### 单向数据流

view--> action--> state
| |
------------------ |

### active-class 是哪个组件的属性，嵌套路由怎么定义

vue-router 模块的 router-link 组件

### 怎么定义 vue-router 下的路由，怎么获取传过来的动态参数

在 router 目录下的 index.js 文件中，对 path 属性加上/:id,使用 router 对象的 params 属性

### vue-router 有哪几种导航钩子?

三种

- 全局导航钩子:router.beforeEach(to, from, next)。作用:跳转前进行拦截
- 组件内钩子
- 单独路由独享钩子

### v-model 是什么?怎么使用?vue 中标签怎么绑定事件？

v-model 数据绑定指令。绑定 vue 中 model 层的 data 属性。
绑定事件 @click v-onclik

### axios 是什么，怎么使用？描述使用它实现登录功能的流程?

请求后台资源的模块。npm install axios -S 装好，然后发送的是跨域，需在配置文件中 config/index.js 进行设置。后台如果是 Tp5 则定义一个资源路由。js 中使用 import 进来，然后.get 或.post。返回在.then 函数中如果成功，失败则是在.catch 函数中

### 什么是 restfulAPI?怎么使用?

一个 api 访问的格式和标准。无状态请求。
对象/行为 book/delete book/add book/
使用合适的访问方式：post/get/put/delete

### vuex 是什么？怎么使用？在哪种功能场景使用？

vue 框架中的集中状态管理。中心仓库，共享数据。
在 main.js 中引入 store,注入。新建一个目录 store, ...export。
场景有:单页应用中，组件之间的状态。音乐播放、登录状态、加入购物车。
缺点：页面刷新或者关闭浏览器再次打开时数据将会归零。
方法:localStorage 或者其他持久化存储(indexDB/proxy)
[proxy](https://www.cnblogs.com/cloud-/p/7103054.html)

### mvvm 框架是什么？与其他框架(jquery)有什么区别?

答:一个 model+view+viewModel 框架。数据模型 model,view 视图。viewModel 充当桥梁作用。传递数据。
区别:vue 是使用数据驱动的，通过数据来显示视图而不是 dom 操作。
场景:数据操作比较多的场景，更加便捷。

### 自定义指令的方法有哪些？它有哪些钩子函数和参数?

全局定义指令: 在 vue 对象的 directive 方法有两个参数,一个是指令名称，另外一个是函数。组件内定义指令:directives;
钩子函数:bind(绑定事件触发)、inserted(节点插入时触发)、update(组件内相关更新)
钩子函数参数:el、binding
创建局部指令

```js
var app = new Vue({
  el: '#app',
  data: {},
  // 创建指令(可以多个)
  directives: {
    // 指令名称
    dir1: {
      inserted(el) {
        // 指令中第一个参数是当前使用指令的DOM
        console.log(el);
        console.log(arguments);
        // 对DOM进行操作
        el.style.width = '200px';
        el.style.height = '200px';
        el.style.background = '#000';
      }
    }
  }
});
```

全局指令

```
Vue.directive('dir2', {
    inserted(el) {
        console.log(el);
    }
})
```

### 自定义过滤器

```js
<div id="app">
     <input type="text" v-model="msg" />
     {{msg| capitalize }}
</div>
var vm=new Vue({
    el:"#app",
    data:{
        msg:''
    },
    filters: {
      capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
    }
})

Vue.filter('capitalize', function (value) {
  if (!value) return ''
  value = value.toString()
  return value.charAt(0).toUpperCase() + value.slice(1)
})
```

### 让 css 只在当前组件起作用

在 style 标签中写入 scoped 即可

### $route和$router 的区别

$route是“路由信息对象”，包括path，params，hash，query，fullPath，matched，name等路由信息参数。而$router 是“路由实例”对象包括了路由的跳转方法，钩子函数等。

### vue 的两个核心

数据驱动、组件系统

### vue 常用的修饰符

.prevent: 提交事件不再重载页面；
.stop: 阻止单击事件冒泡；
.self: 当事件发生在该元素本身而不是子元素的时候会触发；.capture: 事件侦听，事件发生的时候会调用

### vue 的计算属性

在模板中放入太多的逻辑会让模板过重且难以维护，在需要对数据进行复杂处理，且可能多次使用的情况下，尽量采取计算属性的方式。好处：① 使得数据处理结构清晰；② 依赖于数据，数据更新，处理结果自动更新；③ 计算属性内部 this 指向 vm 实例；④ 在 template 调用时，直接写计算属性名即可；⑤ 常用的是 getter 方法，获取数据，也可以使用 set 方法改变数据；⑥ 相较于 methods，不管依赖的数据变不变，methods 都会重新计算，但是依赖数据不变的时候 computed 从缓存中获取，不会重新计算。

### hash 模式和 history 模式

hash 模式
hash 出现在 URL 中，但不会被包含在 http 请求中，对后端完全没有影响，因此改变 hash 不会重新加载页面。
特点：hash 虽然在 URL 中，但不被包括在 HTTP 请求中；用来指导浏览器动作，hash 不会重加载页面。
history 模式
history 利用了 html5 history interface 中新增的 pushState() 和 replaceState() 方法。这两个方法应用于浏览器记录栈，在当前已有的 back、forward、go 基础之上，它们提供了对历史记录修改的功能。只是当它们执行修改时，虽然改变了当前的 URL ，但浏览器不会立即向后端发送请求。

### vue 单页面应用优缺点

- 优点:Vue 的目标是通过尽可能简单的 API 实现响应的数据绑定和组合的视图组件，核心是一个响应的数据绑定系统。MVVM、数据驱动、组件化、轻量、简洁、高效、快速、模块友好。
- 缺点:不支持低版本的浏览器，最低只支持到 IE9；不利于 SEO 的优化（如果要支持 SEO，建议通过服务端来进行渲染组件）；第一次加载首页耗时相对长一些；不可以使用浏览器的导航按钮需要自行实现前进、后退。

### vue 中的\$nextTick

数据更新了，dom 没有变化

### for 中 key 的作用

当 Vue.js 用 v-for 正在更新已渲染过的元素列表时，它默认用“就地复用”策略。如果数据项的顺序被改变，Vue 将不会移动 DOM 元素来匹配数据项的顺序， 而是简单复用此处每个元素，并且确保它在特定索引下显示已被渲染过的每个元素。key 的作用主要是为了高效的更新虚拟 DOM。

### keep-alive

keep-alive 是 Vue 内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染。

### v-show 和 v-if 的区别

v-show 仅仅控制元素的显示方式，将 display 属性在 block 和 none 来回切换；而 v-if 会控制这个 DOM 节点的存在与否。当我们需要经常切换某个元素的显示/隐藏时，使用 v-show 会更加节省性能上的开销；当只需要一次显示或隐藏时，使用 v-if 更加合理。

### 说出 4 中 vue 的指令和它的用法?

v-if:v-show 显示隐藏
v-for:循环
v-bind:绑定属性
v-model:双向数据绑定

### vue-router 是什么?有哪些组件

vue 的路由插件。router-link、router-view

### 导航钩子有哪些？参数有哪些?

导航钩子有：a/全局钩子和组件内独享的钩子。b/beforeRouteEnter、afterEnter、beforeRouterUpdate、beforeRouteLeave

参数：有 to（去的那个路由）、from（离开的路由）、next（一定要用这个函数才能去到下一个路由，如果不用就拦截）最常用就这几种.

### vue 的双向数据绑定原理?(vue data 是怎么实现的?)

Object.defineProperty 通过 getter 和 setter 劫持了对象赋值的过程，在这个过程中可以进行更新 dom 操作等等。

在数据渲染时使用 prop 渲染数据，将 prop 绑定到子组件自身的数据上，修改数据时更新自身数据来替代 prop，watch 子组件自身数据的改变，触发事件通知父组件更改绑定到 prop 的数据。

vue.js 是采用数据劫持结合发布者-订阅者模式的方式，通过 Object.defineProperty()来劫持各个属性的 setter，getter，在数据变动时发布消息给订阅者，触发相应的监听回调。

第一步：需要 observe 的数据对象进行递归遍历，包括子属性对象的属性，都加上 setter 和 getter
这样的话，给这个对象的某个值赋值，就会触发 setter，那么就能监听到了数据变化

第二步：compile 解析模板指令，将模板中的变量替换成数据，然后初始化渲染页面视图，并将每个指令对应的节点绑定更新函数，添加监听数据的订阅者，一旦数据有变动，收到通知，更新视图

第三步：Watcher 订阅者是 Observer 和 Compile 之间通信的桥梁，主要做的事情是:
1、在自身实例化时往属性订阅器(dep)里面添加自己
2、自身必须有一个 update()方法
3、待属性变动 dep.notice()通知时，能调用自身的 update()方法，并触发 Compile 中绑定的回调，则功成身退。

第四步：MVVM 作为数据绑定的入口，整合 Observer、Compile 和 Watcher 三者，通过 Observer 来监听自己的 model 数据变化，通过 Compile 来解析编译模板指令，最终利用 Watcher 搭起 Observer 和 Compile 之间的通信桥梁，达到数据变化 -> 视图更新；视图交互变化(input) -> 数据 model 变更的双向绑定效果。

### 封装 vue 组件的过程

然后，使用 Vue.extend 方法创建一个组件，然后使用 Vue.component 方法注册组件。子组件需要数据，可以在 props 中接受定义。而子组件修改好数据后，想把数据传递给父组件。可以采 im 用 emit 方法。x
写好一个组件之后，在需要使用组件的地方 import,在 componet 属性注册，在 template 需要使用的地方调用。子组件通过 props 接受父组件数据，通过 emit 发送数据

### vue.js 中 template 编译的理解?【

先转化成 AST 树，再得到的 render 函数返回 VNode（Vue 的虚拟 DOM 节点）
首先，通过 compile 编译器把 template 编译成 AST 语法树（abstract syntax tree 即 源代码的抽象语法结构的树状表现形式），compile 是 createCompiler 的返回值，createCompiler 是用以创建编译器的。另外 compile 还负责合并 option。

然后，AST 会经过 generate（将 AST 语法树转化成 render funtion 字符串的过程）得到 render 函数，render 的返回值是 VNode，VNode 是 Vue 的虚拟 DOM 节点，里面有（标签名、子节点、文本等等）

### vue 响应式原理

当一个 Vue 实例创建时，vue 会遍历 data 选项的属性，用 Object.defineProperty 将它们转为 getter/setter 并且在内部追踪相关依赖，在属性被访问和修改时通知变化。
每个组件实例都有相应的 watcher 程序实例，它会在组件渲染的过程中把属性记录为依赖，之后当依赖项的 setter 被调用时，会通知 watcher 重新计算，从而致使它关联的组件得以更新。

vue 的响应式原理是使用 Object.defineProperty 追踪依赖，当属性被访问或改变时通知变化。
有两个不足之处：

不能检测到增加或删除的属性。
数组方面的变动，如根据索引改变元素，以及直接改变数组长度时的变化，不能被检测到。
原因差不多，无非就是没有被 getter/setter 。
第一个比较容易理解，为什么数组长度不能被 getter/setter ？
在知乎上找了一个答案：如果你知道数组的长度，理论上是可以预先给所有的索引设置 getter/setter 的。但是一来很多场景下你不知道数组的长度，二来，如果是很大的数组，预先加 getter/setter 性能负担较大。

现在有一个替代的方案 Proxy，但这东西兼容性不好，迟早要上的。

Proxy，在目标对象之前架设一层拦截。具体，可以参考 「 ECMAScript 6 入门 」
Object.defineProperty(obj,prop, descriptor),该方法接收 3 个参数
obj：
要在其上定义属性的对象。
prop：
要定义或修改的属性的名称。
descriptor：
给对象的属性添加特性描述，目前提供两种形式：数据描述和存取器描述。
返回值：

```js
<body>
    <div id="app">
    <input type="text" id="txt">
    <p id="show"></p>
</div>
</body>
<script type="text/javascript">
    var obj = {}
    Object.defineProperty(obj, 'txt', {
        get: function () {
            return obj
        },
        set: function (newValue) {
            document.getElementById('txt').value = newValue
            document.getElementById('show').innerHTML = newValue
        }
    })
    document.addEventListener('keyup', function (e) {
        obj.txt = e.target.value
    })
</script>
```

### vue 生命周期的作用是什么?

它的生命周期有多个事件钩子，让我们在控制整个 vue 实例的过程中更容易。

### 第一次页面加载会触发哪几个钩子?

beforeCreate、created、beforeMount,mounted

### DOM 渲染在哪个周期就已经完成?

DOM 渲染在 mounted 中已经完成了。

### 嵌套路由何时使用

菜单不止一级的时候

### vue 中如何监听某个属性值的变化?

比如现在需要监控 data 中，obj.a 的变化。Vue 中监控对象属性的变化你可以这样：

```js
// 方法一
watch: {
      obj: {
      handler (newValue, oldValue) {
        console.log('obj changed')
      },
      deep: true
    }
  }

// 方法二

watch: {
   'obj.a': {
      handler (newName, oldName) {
        console.log('obj.a changed')
      }
   }
  }

// 方法三
computed: {
    a1 () {
      return this.obj.a
    }
}
```

### delete 和 Vue.delete 删除数组的区别

delete 只是被删除的元素变成了 empty/undefined 其他的元素的键值还是不变。
Vue.delete 直接删除了数组 改变了数组的键值。

```js
var a = [1, 2, 3, 4];
var b = [1, 2, 3, 4];
delete a[1];
console.log(a);
this.$delete(b, 1);
console.log(b);
```

### 如何解决单页面(SPA)应用首屏加载速度慢的问题?

```js
将公用的JS库通过script标签外部引入，减小app.bundel的大小，让浏览器并行下载资源文件，提高下载速度；
在配置 路由时，页面和组件使用懒加载的方式引入，进一步缩小 app.bundel 的体积，在调用某个组件时再加载对应的js文件；
加一个首屏 loading 图，提升用户体验；
```

### 解决对象数据更新视图没有刷新的问题

\$set()方法相当于手动的去把 obj.b 处理成一个响应式的属性，此时视图也会跟着改变了

```js
addObjB () {
      // this.obj.b = 'obj.b'
      this.$set(this.obj, 'b', 'obj.b')
      console.log(this.obj)
    }
```

### vue 组件 data 为什么必须是函数?

封装作用域,避免变量互相污染
每个组件都是 Vue 的实例。
组件共享 data 属性，当 data 的值是同一个引用类型的值时，改变其中一个会影响其他。

### vue computed 实现

建立与其他属性（如：data、 Store）的联系；
属性改变后，通知计算属性重新计算。
初始化 data， 使用 Object.defineProperty 把这些属性全部转为 getter/setter。
初始化 computed, 遍历 computed 里的每个属性，每个 computed 属性都是一个 watch 实例。每个属性提供的函数作为属性的 getter，使用 Object.defineProperty 转化。
Object.defineProperty getter 依赖收集。用于依赖发生变化时，触发属性重新计算。
若出现当前 computed 计算属性嵌套其他 computed 计算属性时，先进行其他的依赖收集。
[vue computed 的实现](https://segmentfault.com/a/1190000010408657)

### diff 算法的实现

diff 的实现主要通过两个方法，patchVnode 与 updateChildren 。

patchVnode 有两个参数，分别是老节点 oldVnode, 新节点 vnode 。主要分五种情况：

if (oldVnode === vnode)，他们的引用一致，可以认为没有变化。
if(oldVnode.text !== null && vnode.text !== null && oldVnode.text !== vnode.text)，文本节点的比较，需要修改，则会调用 Node.textContent = vnode.text。
if( oldCh && ch && oldCh !== ch ), 两个节点都有子节点，而且它们不一样，这样我们会调用 updateChildren 函数比较子节点，这是 diff 的核心，后边会讲到。
if (ch)，只有新的节点有子节点，调用 createEle(vnode)，vnode.el 已经引用了老的 dom 节点，createEle 函数会在老 dom 节点上添加子节点。
if (oldCh)，新节点没有子节点，老节点有子节点，直接删除老节点。
updateChildren 是关键，这个过程可以概括如下：

jkchao.cn

oldCh 和 newCh 各有两个头尾的变量 StartIdx 和 EndIdx ，它们的 2 个变量相互比较，一共有 4 种比较方式。如果 4 种比较都没匹配，如果设置了 key，就会用 key 进行比较，在比较的过程中，变量会往中间靠，一旦 StartIdx > EndIdx 表明 oldCh 和 newCh 至少有一个已经遍历完了，就会结束比较。

### vue 的脚手架配置

### vue 如何在数据变动后引起视图层变动再通过 dom 获取变动后的数据

### vue 引用类型变量如何触发 view 层变动

### vue 父子组件的通信

### vue 中的数据监听变动是通过什么实现的?

### Vue complier 实现

模板解析这种事，本质是将数据转化为一段 html ，最开始出现在后端，经过各种处理吐给前端。随着各种 mv\* 的兴起，模板解析交由前端处理。
总的来说，Vue complier 是将 template 转化成一个 render 字符串。
可以简单理解成以下步骤：

parse 过程，将 template 利用正则转化成 AST 抽象语法树。
optimize 过程，标记静态节点，后 diff 过程跳过静态节点，提升性能。
generate 过程，生成 render 字符串。

### vue-router 实现原理?

### vue 与其他框架对比的优势和劣势?

### vue 如何实现父子组件通信以及非父子组件通信?

1. 父组件传给子组件:通过 props 的方式接收数据
2. 子组件传给父组件:\$emit 方式传递参数
   非父子组件间的数据传递，兄弟组件传值
   eventBus，就是创建一个事件中心，相当于中转站，可以用它来传递事件和接收事件。项目比较小时，用这个比较合适。（虽然也有不少人推荐直接用 VUEX，具体来说看需求咯。技术只是手段，目的达到才是王道。）

### vuex 是做什么?

只用来读取的状态集中放在 store 中； 改变状态的方式是提交 mutations，这是个同步的事物； 异步逻辑应该封装在 action 中。
在 main.js 引入 store，注入。新建了一个目录 store，….. export 。
场景有：单页应用中，组件之间的状态、音乐播放、登录状态、加入购物车
state
Vuex 使用单一状态树,即每个应用将仅仅包含一个 store 实例，但单一状态树和模块化并不冲突。存放的数据状态，不可以直接修改里面的数据。
mutations
mutations 定义的方法动态修改 Vuex 的 store 中的状态或数据。
getters
类似 vue 的计算属性，主要用来过滤一些数据。
action
actions 可以理解为通过将 mutations 里面处里数据的方法变成可异步的处理数据的方法，简单的说就是异步操作数据。view 层通过 store.dispath 来分发 action。

```js
const store = new Vuex.Store({
  //store实例
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  },
  actions: {
    increment(context) {
      context.commit('increment');
    }
  }
});
```

modules
项目特别复杂的时候，可以让每一个模块拥有自己的 state、mutation、action、getters,使得结构非常清晰，方便管理。

```js
const moduleA = {
  state: { ... },
  mutations: { ... },
  actions: { ... },
  getters: { ... }
 }
const moduleB = {
  state: { ... },
  mutations: { ... },
  actions: { ... }
 }

const store = new Vuex.Store({
  modules: {
    a: moduleA,
    b: moduleB
})
```

### vue 的源码结构?

### 怎么认识 vuex

vuex 是一种开发模式或框架，可以通过状态(数据源)集中管理驱动组件的变化。

应用级的状态放在 store 中；改变状态的方式 mutations,这个是同步的事物。异步逻辑应该写在 action 中。

### vue-loader 是什么？它的用途是设呢么?

vue 文件的一个加载器，跟 template/js/style 转换为 js 模块
用途:js 可以写成 es6,style 样式可以跟 scss 或 less、template 可以加 jade

### vue.cli 项目中 src 目录中的每个文件夹和文件的用法

- asserts 放静态资源
- componets 组件
- router 定义理由
- view 视图
- app.vue 应用主组件
- main.js 入口文件

### vue 与 react 和 angular.js 的区别

版本在不断更新，以下的区别有可能不是很正确。我工作中只用到 vue，对 angular 和 react 不怎么熟） 1.与 AngularJS 的区别
相同点：
都支持指令：内置指令和自定义指令；都支持过滤器：内置过滤器和自定义过滤器；都支持双向数据绑定；都不支持低端浏览器。

不同点：
AngularJS 的学习成本高，比如增加了 Dependency Injection 特性，而 Vue.js 本身提供的 API 都比较简单、直观；在性能上，AngularJS 依赖对数据做脏检查，所以 Watcher 越多越慢；Vue.js 使用基于依赖追踪的观察并且使用异步队列更新，所有的数据都是独立触发的。

2.与 React 的区别
相同点：
React 采用特殊的 JSX 语法，Vue.js 在组件开发中也推崇编写.vue 特殊文件格式，对文件内容都有一些约定，两者都需要编译后使用；中心思想相同：一切都是组件，组件实例之间可以嵌套；都提供合理的钩子函数，可以让开发者定制化地去处理需求；都不内置列数 AJAX，Route 等功能到核心包，而是以插件的方式加载；在组件开发中都支持 mixins 的特性。
不同点：
React 采用的 Virtual DOM 会对渲染出来的结果做脏检查；Vue.js 在模板中提供了指令，过滤器等，可以非常方便，快捷地操作 Virtual DOM。