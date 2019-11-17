# 操作DOM

> ​	实际开发中，我们不可避免的会遇到需要操作真实DOM的操作。下面介绍几种操作DOM的方法。

## 1.使用refs

```js
 <button ref='myBtn' onClick={this.handleBtnClick}>
  我是要div去触发的
</button>
<div onClick={this.handleClick}>我是div呀</div>
---------------------------------------------------
handleBtnClick: function() {
	alert('我是btn啊');
},
handleClick: function() {
	this.refs.myBtn.click();
},
```

## 2.使用`ReactDOM.findDOMNode`

```js
const ReactDOM = require('react-dom');
-------------------------------------------------
<button id='myBtn' onClick={this.handleBtnClick}>
我是要div去触发的
</button>
<div onClick={this.handleClick}>我是div呀</div>
--------------------------------------------------
handleBtnClick: function() {
    alert('我是btn啊');
  },
handleClick: function(e) {
    const myBtn = document.querySelector('#myBtn');
    ReactDOM.findDOMNode(myBtn).click();
}
```

## 3.使用纯`js`

```js
<button id='myBtn' onClick={this.handleBtnClick}>
我是要div去触发的
</button>
<div onClick={this.handleClick}>我是div呀</div>
--------------------------------------------------
handleBtnClick: function() {
    alert('我是btn啊');
},
handleClick: function(e) {
    const myBtn = document.querySelector('#myBtn');
    myBtn.click();
},
```

## 4.回调引用(callback ref)

> es6中使用更加便捷

```js
const _this = this;
-------------------------------------------
<button
  ref={function(e) {
    return (_this.myBtn = e);
  }}
  onClick={this.handleBtnClick}>
  我是要div去触发的
</button>
----------------------------------------------
<div onClick={this.handleClick}>我是div呀</div>
----------------------------------------------
handleBtnClick: function() {
	alert('我是btn啊');
},
handleClick: function() {
	this.myBtn.click();
},
```

## 5.使用事件代理e

```js
<div onClick={this.handleClick}>我是div呀</div>
handleClick: function(e) {
    const myDiv = e.target;
    myDiv.style.backgroundColor = 'red';
}
```

