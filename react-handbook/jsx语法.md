# JSX

> JSX = javascript xml 或者 JSX=javascript extension

## 写法

~~~
//  dom类型标签
const element = <h1>123</h1>
//  react组件类型标签
const element = <HelloWorld />
//  混用dom和react
const element = (
    <div>
        <HelloWorld />
    </div>
)
//  使用表达式计算
const element = <div>{1+2}</div>
//  表达式中使用列表渲染
const element = (
    <ul>
        {
            todos.map((item,index),function(){
                return <li key="index">item<li>
            })
        }
    </ul>
)
~~~

注意:

*   使用表达式的方法时，不能使用js多行语句。
    

## 展开属性

> ​	展开属性是es6语法，请在支持es6的环境中使用展开属性

请看以下代码，假定a的属性都是接收过来的props值,我们可以写成

~~~
const attr = {
    href:"www.baidu.com",
    target:"_blank"
}
return <a {...attr}>Hello</a>
~~~

`...`展开运算符会把属性一一展开

## 注意

*   使用jsx渲染元素时，只能使用js表达式，不能使用js多行语句。遇到需要使用多行语句时，可以使用三目运算符或者逻辑与替代
    

~~~
//  写法一
let complete;
const element = (
    <div>
        {
            complete?<CompletedList />:null
        }
    </div>
)
​
//  写法二
let complete;
const element = (
    <div>
        {
            complete&&<CompletedList />
        }
    </div>
)
~~~

## 注释

在jsx中注释的格式为`{/* 注释 */}`，比如

~~~
consr element =(
    <div>
        {/* 这里是一个注释 */}
        <span>React</span>
    </div>
)
~~~