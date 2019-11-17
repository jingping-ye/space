# ref

一般来说，我们无需通过直接操作DOM。直接操作DOM也与react的Virtual Dom理念相悖，但是某些时候，我们仍然需要用ref去获取真实的DOM节点。

## ref操作

一、操作值

```js
<input type="file" ref="uploadFile"/>
```

在以上例子中，我们清理文件上传元素中的文件时，只能通过以下方式。

```js
this.refs.uploadFile.value=""
```

二、操作事件

以下例子中我们通过点击按钮二调用了按钮一的事件

```js
<button onClick={this.handleBtn1} ref="btn1">按钮一</button>
<button onClick={this.handleBtn2}>按钮二</button>
handleBtn1:function(){
    console.log('我是button1');
}
handleBtn2:function(){
    console.log('我是button2');
    this.refs.btn1.click();
}
```

三、监听事件

```js
<button ref="myBtn">点击</button>
componentDidMount:function(){
    this.refs.myBtn.addEventListener("click",function(e){
        console.log('你点击了我')
    })
},
componentWillUnmount() {
    this.refs.myBtn.removeEventListener('click', function(e){
        console.log('清除数据')
    });
},
```

四、动态ref

如果一个组件在一个页面复用多次，而组件包含ref属性，那么我们必须给ref指定唯一的值，否则将会报错。给定ref唯一值有两种方式。

1. 使用React.createRef()

> 在16.3以上版本

```js
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.myRef = React.createRef();
  }
  render() {
    return <div ref={this.myRef} />;
  }
}
```

2.手动生成

## 父组件操作子组件

通过ref,父组件可以获取子组件的状态，执行子组件的方法。但是除非极端情况，不推荐直接通过ref去操作。

```js
<subCOmponent ref="myComponent"/>
this.refs.myComponent.state.[stateName]; //获取子组件中的状态
this.refs.myComponent.[Func](); //	执行子组件的Func()方法
```

## 转发

## 其他

- ref 在函数式组件上不可用，我们需要用其他方法去替代它

