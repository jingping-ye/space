## 安装使用

```sh
npm install echarts --save

import * as echarts from 'echarts';
```

## 基础配置

echarts的图形化呈现主要通过配置方法(setOption)实现，然后对图形标签进行初始化

```sh
|-- series:[array:object]系列:一组数值(注意是数值！) 、图标类型、以及他们映射成的图的参数--> 图及数据，一组图和数据就是一个对象
	|-- type: [string] pie|bar|line|bar|pie|scatter|graph|tree 图表类型
	|-- data: [array:object] 成组数据，对应y轴数据
	|-- name: [string] 数据名称，变量名，与legend-data配套使用
	|-- center
	|-- radius
	|-- encode
		|-- x 与source中的数据对应，下标
		|-- y 与source中的数据对应，下标
		|-- itemName 与source中的数据对应，下标，适用于饼状图
		|-- value 与source中的数据对应，下标
|-- title:[object]标题
	|-- text:[string]图表的标题文字，位于图表左上方
|-- legend：[object] 图例
	|-- data: [array] 图例名称
|-- xAxis:[array?:object] X轴
	|-- data[array] x轴分类或者刻度数据
	|-- name[string] x轴坐标轴标题
|-- yAxis:[array:object] Y轴
	|-- data[array] y轴分类或刻度数据
	|-- name[string] y轴坐标轴标题
|-- polar:
|-- radiusAxis
|-- angleAxis
|-- radar
|-- dataZoom
|-- tooltip [object] 鼠标悬停的提示内容
|-- toolbox [object] 图表工具栏（比如刷新，下载等）
	|-- feature
    	|-- dataView
    	|-- saveAsImage
    		|-- pixelRatio
    	|-- restore
|-- brush
|-- geo
|-- parallel
|-- parallelAxis
|-- singleAxis
|-- timeline
|-- color
|-- background
|-- textStyle
|-- grid 坐标轴背景
```

1. 在使用echarts.js的时候一定要配置xAxis,yAxis,series这三个参数，如果是不想设置的话也要初始化可以将其设置为空JSON就可以了，要不然会出项报错，同时要保证在echarts.init之前的对象是有宽高的

### 其他数据

```js
|-- dataZoom 数据区缩放
|-- visualMap 视觉映射
```



## 交互api

- echarts 获取或设置全局属性API
- echartsInstance 获取或设置图标echart.init对象相关的API属性
- actions events事件和数据可视化行为例如高亮、tooltip位置设置等
- events 图表的触发事件

## echart编写流程

- 画布 设定宽高
- 配置

## 二维数据的组织方式

### x轴和y轴都是数据

> 全部写入series

```js
option = {
    title: {
        text: '秋季服饰销售一览'
    },
    tooltip: {},
    toolbox: {
        feature: {
            dataView: {},
            saveAsImage: {
                pixelRatio: 2
            },
            restore: {}
        }
    },
    xAxis: {},
    yAxis: {},
    series: [{
        type: 'line',
        smooth: true,
        data: [[1, 40], [12, 20], [36, 36], [48, 10], [60, 10], [72, 20]]
    }]
};
```

### x轴和y轴有一个是文字

> 分别组织，文字写入xAxis，数据写入series

```js
option = {
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    xAxis: {
        data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    },
    yAxis: {},
    series: [{
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};
```

### 各类图形的组织形式

#### 柱状图

```js
option = {
    series : [
        {
            name: '访问来源',
            type: 'bar',
            data:[
                {value:235,itemStyle:{color:'#dedede'}},
                {value:274, name:'联盟广告'},
                {value:310, name:'邮件营销'},
                {value:335, name:'直接访问'},
                {value:400, name:'搜索引擎'}
            ]
        }
    ],
    xAxis:{
        data:['视频广告','联盟广告','邮件营销','直接访问','搜索引擎']
    },
    yAxis:{}
    
};
```

#### 饼状图

```js
{
    type: "pie",
    center: ["65%", 60], // 圆的位置，可以使百分比，也可以使数据[左，上]的构成结构
    radius: 35, // 圆的半径，可以使百分比，也可以使数据
    roseType: 'angle', // 转变成南丁格尔图
    data: [
      {
        name: "衬衫",
        value: 5
      },
      {
        name: "羊毛衫",
        value: 20
      },
      {
        name: "雪纺裤",
        value: 36
      }
    ]
    },
```

#### 折线图

```js
{
    name: "10月销量",
    type: "line",
    data: [34, 20, 36, 10, 10, 20]
  }
```

#### 样式

```js
options:{
    textStyle: { // 文字样式,有时会没用???
        color: 'rgba(255, 255, 255, 0.3)'
    },
    backgroundColor: '#2c343c', // 背景颜色
    itemStyle: {
        // 阴影的大小
        shadowBlur: 200,
        // 阴影水平方向上的偏移
        shadowOffsetX: 0,
        // 阴影垂直方向上的偏移
        shadowOffsetY: 0,
        // 阴影颜色
        shadowColor: 'rgba(0, 0, 0, 0.5)',
            emphasis: { // 鼠标hover时的高亮样式
            shadowBlur: 200,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
    },
    label: {
        textStyle: {
            color: 'rgba(255, 255, 255, 0.3)'
        }
    },
    
}
```

### 异步加载

```js
function fetchData(cb) {
    // 通过 setTimeout 模拟异步加载
    setTimeout(function () {
        cb({
            categories: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
            data: [5, 20, 36, 10, 10, 20]
        });
    }, 3000);
}

// 初始 option
option = {
    title: {
        text: '异步数据加载示例'
    },
    tooltip: {},
    legend: {
        data:['销量']
    },
    xAxis: {
        data: []
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: []
    }]
};

myChart.showLoading();

fetchData(function (data) {
    myChart.hideLoading();
    myChart.setOption({
        xAxis: {
            data: data.categories
        },
        series: [{
            // 根据名字对应到相应的系列
            name: '销量',
            data: data.data
        }]
    });
});
```

#### 数据集映射

```js
option = {
    legend: {},
    tooltip: {},
    dataset: {
        // 这里指定了维度名的顺序，从而可以利用默认的维度到坐标轴的映射。
        // 如果不指定 dimensions，也可以通过指定 series.encode 完成映射，参见后文。
        dimensions: ['product', '2015', '2016', '2017'],
        source: [
            {product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7},
            {product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1},
            {product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5},
            {product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1}
        ]
    },
    xAxis: {type: 'category'},
    yAxis: {},
    series: [
        {type: 'bar'},
        {type: 'bar'},
        {type: 'bar'}
    ]
};
```

常用图表所描述的数据大部分是“二维表”结构，上述的例子中，我们都使用二维数组来容纳二维表。现在，当我们把系列（series）对应到“列”的时候，那么每一列就称为一个“维度（dimension）”，而每一行称为数据项（item）。反之，如果我们把系列（series）对应到表行，那么每一行就是“维度（dimension）”，每一列就是数据项（item）。

#### 条形图

```js
yAxis: {
    type: 'category',
    data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
},
```

