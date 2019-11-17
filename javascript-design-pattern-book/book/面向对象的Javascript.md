# 第 1 章：面向对象的 Javascript

## 编程语言分类（按数据类型）

### 静态类型语言

1. 定义

   静态类型语言是指在编译时已经确定变量类型的语言。

2. 优缺点

   - 优点

     （1）安全性：在编译时就能发现类型不匹配的错误，编辑器可以提前避免程序在运行期间有可能发生的一些错误。

     （2）便于优化：如果程序明确的规定了数据类型，编译器可以针对这些信息对程序进行一些优化，提高程序执行速度

   - 缺点

     （1）迫使程序员依照契约来编写程序

     （2）增加代码，将程序员的精力从思考业务逻辑上分散开来

### 动态类型语言

1. 定义

   动态类型语言是指变量类型要到程序运行时，待变量被赋予某个值之后，才会具有确定类型的语言。

2. 优缺点

   - 优点

     （1）代码数量更少，更简洁，程序员可以把更多的精力放在业务逻辑上

     （2）专注逻辑表达，代码更便于阅读。

   - 缺点

     （1）无法保证变量类型，要等程序运行才能知道与类型相关的错误。

3. 基础：鸭子类型(duck typing)

   - 不要问我是什么，看我做了什么
   - 不关注对象本身，只关心对象的行为，也就是关注 HAS-A,而不是 IS-A

## 面向对象特点在 js 中的实现

### 多态

1. 特点

   （1）分离变化：将不变的事物与可能改变的事物分离开来；将做什么与谁去做以及怎么去做分离开来。

   （2）向上转型：忽略具体类型，而寻求超类

2. 作用

   通过把过程化的条件分支语句转换为对象的多态性，从而消除这些条件分支语句‘

3. js 天生多态性

   - 不区分数据类型，无需考虑向上转型
   - 函数作为一等公民，可以分装行为并且作为参数传递。

4. 实例

```js
/**
 * 调用不同的接口渲染地图
 * Note: 分离变化：将做什么与谁去做以及怎么去做分离开来。
 *       向上转型：忽略具体类型，而寻求超类；
 */

var renderMap = function(map) {
  if (map.show instanceof Function) {
    map.show();
  }
};
var googleMap = {
  show: function() {
    console.log('开始渲染谷歌地图');
  }
};

var baiduMap = {
  show: function() {
    console.log('开始渲染百度地图');
  }
};

var sosoMap = {
  show: function() {
    console.log('开始渲染搜搜地图');
  }
};

renderMap(baiduMap);
```

### 封装

> 封装的目的是将信息隐藏

1. 特点

   - 封装数据：数据具有访问权限。
   - 封装实现：隐藏实现细节、设计细节以及隐藏对象的类型。
   - 封装类型：隐藏对象的类型。
   - 封装变化：将稳定不变的部分与容易变化的部分隔离开来

2. js 实现封装

   - 封装数据

     - 使用 let 和作用域
     - 使用（闭包）函数创建作用域
     - 通过 Symbol 创建私有属性

     ```js
     var myObject = (function() {
       var _name = 'sven'; // 私有变量
       return {
         getName: function() {
           // 公有方法
           return _name;
         }
       };
     })();
     console.log(myObject.getName());
     console.log(myObject.__name);
     ```

### 继承

### 组合

## 设计模式

> 设计模式是对具体解决方法的抽象总结，这种具体解决方法并不仅限于编程。

## 原型模式

1. 特点

- 对象是通过克隆另一个对象得到的。对象一定有一个根对象存在。（吸血鬼必然有一个吸血鬼祖先）；A 从 B 克隆而来，B 是 A 的原型。
- 所有数据都是对象。
- 要得到一个对象，不是通过实例化类，而是找到一个对象原型并克隆它。
- 对象会记住它的原型。
- 如果对象无法响应某个请求，它会把请求委托给自己的原型。

2. 关键

   原型对象的关键是是否提供了 clone 方法。

3. js 实现原型模式

   - es5 提供了`Object.create`方法，实现克隆对象
   - js 本身是一门基于原型的面向对象方法
   - 原型特点在 js 中的体现
     - 所有数据都是对象：除了 undefined,一切都是对象。number、string、boolean 等基本类型数据可以通过包装类的方式来变成对象类型数据处理。
     - 对象是通过克隆另一个对象得到的。对象一定有一个根对象存在：js 的根对象是`Object.prototype`对象,`Object.prototype`是一个空对象。js 对象都是从`Object.prototype`对象克隆的。
     - 要得到一个对象，不是通过实例化类，而是找到一个对象原型并克隆它:js 中克隆的过程由引擎内部实现，我们只需要显示调用`var obj1 = new Object()`或者`var obj1 ={}`,引擎内部会从`Object.prototype`上克隆一个对象。
     - 对象会记住它的原型：js 提供`__proto__`隐藏属性，默认只想构造器的原型对象，即`{constructor}.prototype`。`__proto__`是对象与对象构造器的原型联系起来的纽带。
     - 如果对象无法响应某个请求，它会把请求委托给自己的原型：原型链。js 的对象最初都是`Object.prototype`对象克隆而来，但是对象构造器的原型不仅限于`Object.prototype`上，而是可以动态的指向其他对象。
   - 实例

   ```js
   /**
    * 使用Object.create克隆对象
    */
   var Plane = function() {
     this.blood = 100;
     this.attachLevel = 1;
     this.defenseLevel = 1;
   };

   var plane = new Plane();
   plane.blood = 500;
   plane.attachLevel = 10;
   plane.defenseLevel = 8;

   var clonePlane = Object.create(plane);
   console.log(clonePlane.blood); // 500

   /**
    * 函数构造器:用new来调用函数时，此时的函数就是一个构造器
    * @param {string} name 名称
    */
   function Person(name) {
     this.name = name;
   }

   Person.prototype.getName = function() {
     return this.name;
   };

   var a = new Person('me');

   console.log(a.name); //me
   console.log(a.getName()); // me

   /**
    * 1. 遍历a属性，没有找到name属性
    * 2. 委托对象构造器原型，__proto__指向obj
    * 3. 在obj找到name属性，并返回值
    */
   var obj = { name: 'sven' };
   var A = function() {};
   A.prototype = obj;
   var a = new A();
   console.log(a.name);
   ```
