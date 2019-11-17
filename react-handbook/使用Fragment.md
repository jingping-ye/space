# Fragment

在render渲染元素时，按照语法，所有元素必须包裹在一个元素下，否则将会报错(如下)。

```js
render:function(){
    <div>
        <h1>姓名</h1>
    	<p>isME</p>
    </div>
}
```

这样会造成无关语义和样式的多一个div标签。为了去掉这个div标签，我们可以用`Fragment`替代。此时，浏览器将不再显示div,而是直接从`h1`开始显示

```js
render:function{
  return (
    <React.Fragment>
        <h1>姓名</h1>
    	<p>isME</p>
    </React.Fragment>
  )
}
```

## 其他

- react的某些版本不支持fragment语法
- `fragement`也可以使用key