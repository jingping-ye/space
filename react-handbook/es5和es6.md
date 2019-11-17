# es5与es6

>  在学习es5与es6之前，必须了解以下几个概念:
>
> - Javascript由DOM、BOM和ECMAScript组成。es5和es6中的es即是ECMAScript的缩写
> - es5指的的2012年到2015年发布的ECMAScript版本，es6指的是2015年发布的ECMAScript版本。目前,es的版本号已经发布到7。

## es5

> 主要说明api

### 对象

| 对象     | 构造器                     | 说明                                                         |
| -------- | -------------------------- | ------------------------------------------------------------ |
| `Object` | `getPrototypeOf`           | 返回对象的原型                                               |
| `Object` | `getOwnPropertyDescriptor` | 返回对象自有属性的属性描述符                                 |
| `Object` | `getOwnPropertyNames`      | 返回一个数组，包括对象所有自有属性名称集合（包括不可枚举的属性） |
| `Object` | `create`                   | 创建一个拥有置顶原型和若干个指定属性的对象                   |
| `Object` | `defineProperty`           | 给对象定义一个新属性，或者修改已有的属性，并返回             |
| `Object` | `defineProperties`         | 在一个对象上添加或修改一个或者多个自有属性，并返回该对象     |
| `Object` | `seal`                     | 锁定对象。阻止修改现有属性的特性，并阻止添加新属性。但是可以修改已有属性的值。 |
| `Object` | `freeze`                   | 冻结对象，阻止对对象的一切操作。冻结对象将永远不可变。       |
| `Object` | `preventExtensions`        | 让一个对象变的不可扩展，也就是永远不能再添加新的属性。       |
| `Object` | `isSealed`                 | 判断对象是否被锁定                                           |
| `Object` | `isFrozen`                 | 判断对象是否被冻结                                           |
| `Object` | `isExtensible`             | 判断对象是否可以被扩展                                       |
| `Object` | `keys`                     | 返回一个由给定对象的所有可枚举自身属性的属性名组成的数组，常用! |

### 数组

| 对象              | 构造器        | 说明                                                         |
| ----------------- | ------------- | ------------------------------------------------------------ |
| `Array.prototype` | `indexOf`     | 返回根据给定元素找到的第一个索引值，否则返回-1               |
| `Array.prototype` | `lastIndexOf` | 方法返回指定元素在数组中的最后一个的索引，如果不存在则返回 -1 |
| `Array.prototype` | `every`       | 测试数组的所有元素是否都通过了指定函数的测试                 |
| `Array.prototype` | `some`        | 测试数组中的某些元素是否通过了指定函数的测试                 |
| `Array.prototype` | `forEach`     | 让数组的每一项都执行一次给定的函数                           |
| `Array.prototype` | `map`         | 返回一个由原数组中的每个元素调用一个指定方法后的返回值组成的新数组 |
| `Array.prototype` | `filter`      | 利用所有通过指定函数测试的元素创建一个新的数组，并返回       |
| `Array.prototype` | `reduce`      | 接收一个函数作为累加器，数组中的每个值（从左到右）开始缩减，最终为一个值 |
| `Array.prototype` | `reduceRight` | 接受一个函数作为累加器，让每个值（从右到左，亦即从尾到头）缩减为一个值 |

## es6

### es6新特性

| 新增特性                   | 关键词                              | 用法                           | 描述                                                 |
| -------------------------- | ----------------------------------- | ------------------------------ | ---------------------------------------------------- |
| 箭头操作符                 | Arrows                              | `v => console.log(v)`          | 类似于部分强类型语言中的lambda表达式                 |
| 类的支持                   | Classes                             | -                              | 原生支持类，让javascript的OOP编码更加地道            |
| 增强的对象字面量           | enhanced object literals            | -                              | 增强对象字面量                                       |
| 字符串模板                 | template strings                    | `${num}`                       | 原生支持字符串模板，不再需要第三方库的支持           |
| 解构赋值                   | destructuring                       | `[x, y] = ['hello', 'world']`  | 使用过python的话，你应该很熟悉这个语法               |
| 函数参数扩展               | default, rest, spread               | -                              | 函数参数可以使用默认值、不定参数以及拓展参数了       |
| let、const                 | let、const                          | -                              | javascript中可以使用块级作用域和声明常量了           |
| for…of遍历                 | for…of                              | `for (v of someArray) { ... }` | 又多了一种折腾数组、Map等数据结构的方法了            |
| 迭代器和生成器             | iterators, generator, iterables     | -                              | ES6较为难以理解的新东西，后面会有相关文章            |
| Unicode                    | unicode                             | -                              | 原生的unicode更加完美的支持                          |
| 模块和模块加载             | modules, modules loader             | -                              | ES6中开始支持原生模块化啦                            |
| map, set, weakmap, weakset | -                                   | -                              | 新的数据结构                                         |
| 监控代理                   | proxies                             | -                              | 我们可以监听对象发生了哪些事，并可以自定义对应的操作 |
| Symbols                    | -                                   | -                              | 我们可以使用symbol来创建一个不同寻常的key            |
| Promises                   | -                                   | -                              | 这家伙经常在讨论异步处理流程时被提到                 |
| 新的API                    | math, number, string, array, object | -                              | 原生的功能性API就是方便些                            |
| 内置对象可以被继承         | subclassable built-ins              | -                              | 可以基于内置对象，比如Array，来生成一个类            |
| 二进制、八进制字面量       | -                                   | -                              | 可以直接在es6中使用二进制或者八进制字面量了          |
| Reflect API                | -                                   | -                              | 反射API？                                            |
| 尾调用                     | tail calls                          | -                              | ES6中会自动帮你做一些尾递归方面的优化                |

## 参考

- [ECMAScript官网](http://www.ecma-international.org/ecma-262/5.1/)

- [阮一峰的es6入门](http://es6.ruanyifeng.com/) 

- [es中文版翻译集合](http://yanhaijing.com/es5/#null)

