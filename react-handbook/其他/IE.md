# IE

> 输入框输入内容时，在onFocus和onBlur之间切换时，光标会跳到输入内容前
> 解决方法:手动定位光标位置

```js
this.refs.xx.setSelectionRange(length,length)
```

------

> 排序方法，sort函数传入方法在IE中失效 
> 解决方法：使用1和-1替代直接返回true和false

```js
func.sort(function (a, b) {
    // return a<b;
    if (a < b) {
       return 1;
    } else {
      return -1;
    }
});
```

------

> IE下的input框末尾显示x，但是点击时触发不了onchange事件
> 解决方法:将x在界面上隐藏

```js
input::-ms-clear, input::-ms-reveal{
     display: none;  
}
```

