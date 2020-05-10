# 第4章 HTML

> 尝试混合何种方法

1. 语义化而非div
2. 模块化而非页面化
3. 标签使用css选择器表明语义

## OOCSS方法 Object-Oriented CSS 面向对象的CSS

http://oocss.org/

原则： 

- 分离结构和外观 ==> 视觉特性定义为可复用的单元 simple--> 使用直角 complex--> 使用圆角还有阴影
- 分离容器和内容 =>  不再将元素位置作为样式的限定词

```html
<div class="toggle simple">
  <div class="toggle-control open">
    <h1 class="toggle-title">Title 1</h1>
  </div>
  <div class="toggle-detail open">
    <h1 class="toggle-title">Title 2</h1>
  </div>
</div>
```



## SMACSS方法 Scalable and Modular Architecture for CSS  模块化架构的可扩展CSS

比较oocss的不同:把样式系统分为5个具体类别

- 基础：如果不添加CSS类名，标记会以什么外观呈现。

- 布局：把页面分成一些区域。
- 模块：设计中的模块化，可复用的单元。 => toggle/toggle-simple/toggle-detail
- 状态：描述在特定的状态或情况下，模块或布局的显示方式。is-active
- 主题：一个可选的视觉外观层，可以让你切换不同的主题。

```html
<div class="toggle toggle-simple">
  <div class="toggle-control is-active">
    <h1 class="toggle-title">Title 1</h1>
  </div>
  <div class="toggle-detail is-active">
    <h1 class="toggle-title">Title 2</h1>
  </div>
</div>
```



## BEM方法 Block Element Modifier 块元素修饰符

> 单纯的命名规则

每个css类名的命名包含以下部分：

- 块名：所属组件的名称。 ==> toggle
- 元素：元素在块里面的名称。==> control
- 修饰符：任何与块或元素相关联的修饰符。 ==> active

```html
<div class="toggle toggle--simple">
  <div class="toggle__control toggle__control--active">
    <h1 class="toggle__title">Title 1</h1>
  </div>
 <div class="toggle__control toggle__control--active">
    <h1 class="toggle__title">Title 2</h1>
  </div>
</div>
```

