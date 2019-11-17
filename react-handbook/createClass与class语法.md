# createClass与class语法

> createClass在15.5.0版被废弃，在16中不再支持。

## createClass语法

~~~js
const TestComponent = require('./component/TestComponent');
let myAttr = 12;
const MyComponent = React.createClass({
    render:function(){
        return (<div>这个是组件</div>)
    },
    getInitialState:function(){
        return{
            name:"vine"
        }
    },
    getDefaultProps:function(){
      return {
          age:'12'
      }
    },
    propType:{
        age:React.PropTypes.string
    },
    componentDidMount:function(){},
    runMyMethods:function(){
        console.log('我的方法');
    }
    
})
module.exports = MyComponent
~~~

向React.createClass方法传入类json格式键值对

## class 语法

> es6类语法

~~~js
import TestComponent from './component/TestComponent';

const MyComponent extends React.Component{
    render(){
        return (<div>我是一个组件</div>)
    }
    constructor(props){
        super(props);
        this.state = {
            name:"vine"
        }
        this.myAttr = 12;
        this.runMyMethod = this.runMyMethod.bind(this);
    }
    static defaultProps={
        career:'programer'
    }
    static propTypes={
        name:PropTypes.string
    }
    runMyMethod(){
        console.log('调用方法')
    }
}
export default MyComponent;
~~~

## 其他

- 不管是哪种写法，组件名称的开头字母必须大写

