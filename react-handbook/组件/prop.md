# prop

> prop = properties 属性，组件的属性

## constructor与prop

使用createClass语法的时候，我们直接使用this.props.[propName]即可接收到属性，但是在class语法中，需要在constructor中通过super继承props属性再去调用，否则将会出错(如下)。

```js
class TestComponent extends React.Component{
    constructor(props){
        super(props)
    }
    render(){
        return (
        	<div>{this.props.title}</div>
        )
    }
}
```



## this.props

prop属性很简单，即我们从父组件往子组件传的数据，只是数据的名称不同。比如:

```js
<TestComponent myData={this.state.data} />
```

传递一个数据`this.state.data`,名称为myData。这里我们将其看做对象的键值对就好啦。

在子组件中，我们通过`this.props.myData`，即`this.props.[propName]`的格式去接收就可以了。

## this.props.children

props中有一个特殊的属性，即children属性，children属性无需显式声明。如下:

```js
<TestComponent>
    <h1>Title</h1>
    <div>12312</div>
</TestComponent>
```

在TestComponent标签之间的元素即是children的内容。

那么我们在子组件中只需要通用this.props.children即可接收标签之间的全部内容。

子组件：

```js
render:function(){
    return <div>this.props.children</div>
}
```

## 默认属性

一般来说，我们需要给属性设置默认属性，防止因为用于不传递属性而产生的一些问题。

```js
getDefaultProps:{
    return {
        title:'',
        fruit:['apple','banana'],
        student:{},
        age:0,
        myFunc:funciton(){return}
    }
}
```

## 属性校验

调用组件的开发者可能会误传入属性的数据类型，所以，我们需要进行属性校验。使用属性校验时，如果传入错误的属性，控制台将会报错提醒开发者。

详细属性校验规则看官网。

参考:[propTypes属性校验](https://react.docschina.org/docs/typechecking-with-proptypes.html#proptypes)

## 其他

- props应该是只读的,不能进行this.props.propName=xx的操作