# class 和 style

## 写法

### style 的写法

```js
function Welcome(props) {
  const style = {
    width: '100%',
    height: '500px',
    backgroundColor: 'blue',
    fontSize: '18px'
  };
  return <h1 style={style}>Hello,word</h1>;
}
```

- 驼峰命名:除了浏览器前缀，全部采用小驼峰法，浏览器前缀除了 ms 浏览器外，均采用大驼峰法

- 对象写法，无需引号。

- 单独写 style 可以不用加 px 单位

#### class 的写法

在 jsx 中，不能使用`class`属性，而是用`className`替代

### 动态添加 style 和 class

```js
//  动态添加style
<div style=\{\{display:(index===this.state.show?'block':'none',color:'red')\}\}>显示div</div>
//  动态添加class
//  单个class
<div className={this.state.show?showBlock:''}>显示div</div>
//  单个class
<div className={this.state.show&&'showBlock'}>
//  多个class
<div className={["other-class ", this.state.show?showBlock:''].join(' ')}>显示div</div>
```

## 外部传入 style 和 class

### 外部传入 style

```js
static defaultProps = {
    divStyle: {
    width: '650px',
    height: '200px'
   }
};
render(){
    return(
    <div style={this.props.divStyle}></div
    )
}
```
