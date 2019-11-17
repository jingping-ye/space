# state

> - state是react用来刷新视图的工具，即state值变动，视图也会随之自动刷新。
> - state可以看做组件内部的数据，只不过会随时变更。
> - 优先使用变量，只在必要的时候才使用state

## 更新state

```js
this.setState({
    data:myData
})
```

## 异步与同步

setState是异步的，也就说，我们在setState之后基于state去进行操作，很有可能此时state的值还没有更新掉，这个时候，我们可以使用两种方法去使代码同步。方法一是使用setState的回调函数,方法二是使用setTimeout。

### 方法一:使用setState回调

```js
this.setState({
    data:myData
},function(){
    this.calculateData(this.state.data)
})
```

### 方法二:使用setTimeout

使用setTimeout可以让将要执行的事件与setState事件在同一任务队列中

```js
this.setState({
    data.myData
});
const _this = this;
setTimeout(function(){
   _this.calculateData(this.state.data); 
},0)
```

## 何时使用state

state对应的数据应该尽可能是由于用户交互和操作引起的`UI`变化这类数据，越少使用state越好。