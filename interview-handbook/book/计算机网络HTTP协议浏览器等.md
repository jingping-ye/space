# 计算机网络 HTTP 协议浏览器等

## 计算机网络

### tcp/ip 三次握手过程

### tcp/ip 模型和 osi 模型

- tcp/ip 模型：从下往上分别是链路层，网络层，传输层，应用层
- osi 模型：从下往上分别是物理层，链路层，网络层，传输层，会话层，表示层，应用层

### TCP 和 UDP 的区别？

TCP 是基于连接的协议，也就是说，在正式收发数据前，必须和对方简历可靠的连接。一个 TCP 连接必须要经过三次“对话”才能建立起来
UDP 是与 TCP 相应的协议。他是面向非连接的协议，他不与对方建立连接，而是直接就把数据包发送过去了
UDP 适用于一次只传送少量数据，对可靠性要求不高的应用环境

## HTTP协议

### 说说状态码的类别以及你常用的状态码?

> 借助状态码，我们可以知道服务端是是否正常处理了请求，还是出现了什么错误。

#### 状态码的类别

| 状态码 | 类别                             | 描述                   |
| ------ | -------------------------------- | ---------------------- |
| 1xx    | Informational（信息状态码）      | 接受请求正在处理       |
| 2xx    | Success（成功状态码）            | 请求正常处理完毕       |
| 3xx    | Redirection（重定向状态码）      | 需要附加操作已完成请求 |
| 4xx    | Client Error（客户端错误状态码） | 服务器无法处理请求     |
| 5xx    | Server Error（服务器错误状态码） | 服务器处理请求出错     |

#### 常用状态码

- 202：服务器已经接受请求，但尚未处理
- 204: 服务器成功处理了请求，但是没有返回任何内容
- 200: 请求已经处理
- 301: 永久重定向
- 302/307: 临时重定向
- 304: 资源已找到，但是未符合条件请求。
- 403：禁止访问
- 404：未找到页面
- 500: 服务器内部错误

### HTTP 和 HTTPS

HTTP 协议通常承载与 TCP 协议之上，在 HTTP 和 TCP 之间添加一个安全协议层（SSL 或 TSL），这个时候，就成了我们常说的 HTTPS
默认 HTTP 的端口号为 80，HTTPS 的端口号为 443

### 为什么 HTTPS 安全

因为网络请求需要中间有很多的服务器路由的转发，中间的节点都可能篡改信息，而如果使用 HTTPS，密钥在你和终点站才有，https 之所有说比 http 安全，是因为他利用 ssl/tls 协议传输。包含证书，流量转发，负载均衡，页面适配，浏览器适配，refer 传递等，保障了传输过程的安全性

### 关于 http 2.0

http/2 引入了“服务端推”的概念，它允许服务端在客户端需要数据之前就主动的将数据发送到客户端缓存中，从而提高性能
http/2 提供更多的加密支持
http/2 使用多路技术，允许多个消息在一个连接上同时交差
它增加了头压缩，因此即使非常小的请求，其请求和响应和 header 都只会占用小比例的带宽

### 分域名请求图片的原因和好处？

浏览器的并发请求数目限制是针对同一域名的，超过限制数目的请求会被阻塞
浏览器并发请求有个数限制，分域名可以同时并发请求大量图片

### 输入网站后到页面展现是过程？

通过 dns 解析获取 ip
通过 dns 解析获取 ip
tcp 链接
客户端发送 http 请求
tcp 传输报文
服务器处理请求返回 http 报文

### http 响应中 content-type 包含哪些内容？

请求中的消息主题是用何种方式解码
application/x-www-form-urlencoded
这是最常见的 post 提交数据的方式，按照 key1=val1&key2=val2 的方式进行编码
application/json
告诉服务器端消息主体是序列化后 json 字符串

### GET 和 POST 的区别

GET 和 POST 本质上就是 TCP 链接，并无差别。但是由于 HTTP 的规定和浏览器/服务器的限制，导致他们在应用过程中体现出一些不同。

需要注意的是，web 中的 get/post 只是 http 中的 get/post 的子集。http 中的 get 与 post 只是单纯的名字上的区别，get 请求的数据也可以放在 request body 中，只是浏览器没有实现它，但是 get 并不只是在 web 中使用。

- GET 产生一个 TCP 数据包；POST 产生两个 TCP 数据包。
- GET 在浏览器回退时是无害的，而 POST 会再次提交请求。
- GET 产生的 URL 地址可以被 Bookmark，而 POST 不可以。
- GET 请求会被浏览器主动 cache，而 POST 不会，除非手动设置。
- GET 请求只能进行 url 编码，而 POST 支持多种编码方式。
- GET 请求参数会被完整保留在浏览器历史记录里，而 POST 中的参数不会被保留。
- GET 请求在 URL 中传送的参数是有长度限制的，而 POST 么有。
- 对参数的数据类型，GET 只接受 ASCII 字符，而 POST 没有限制。
- GET 比 POST 更不安全，因为参数直接暴露在 URL 上，所以不能用来传递敏感信息。
- GET 参数通过 URL 传递，POST 放在 Request body 中。
  缓存:get 请求能够被缓存，post 请求默认不会被缓存(缓存是针对 URL 的)
  安全性:包含在 URL 中明文显示，且服务器的日志会记录，非常不安全 。
  数据量：没有规定，但是受限于浏览器平台。通常，get 较小。

### Accept 和 Content-Type

Accept 请求头用来告知客户端可以处理的内容类型，这种内容类型用 MIME 类型来表示。
服务器使用 Content-Type 应答头通知客户端它的选择。

```
Accept: text/html
Accept: image/*
Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8
```

1.Accept 属于请求头， Content-Type 属于实体头。 <br>
Http 报头分为通用报头，请求报头，响应报头和实体报头。 <br>
请求方的 http 报头结构：通用报头|请求报头|实体报头 <br>
响应方的 http 报头结构：通用报头|响应报头|实体报头<br>

2.Accept 代表发送端（客户端）希望接受的数据类型。 <br>
比如：Accept：text/xml; <br>
代表客户端希望接受的数据类型是 xml 类型<br>

Content-Type 代表发送端（客户端|服务器）发送的实体数据的数据类型。 <br>
比如：Content-Type：text/html; <br>
代表发送端发送的数据格式是 html。<br>

二者合起来， <br>
Accept:text/xml； <br>
Content-Type:text/html <br>
即代表希望接受的数据类型是 xml 格式，本次请求发送的数据的数据格式是 html。<br>

### http 缓存

### 强制缓存和协商缓存的区别

强制缓存

```
Expires或Cache-Control
```

协商缓存

- 第一对：Last-Modified、If-Modified-Since

- 第二对：ETag、If-None-Match

### 如何处理不让别人盗用你的图片，访问你的服务器资源(盗链)

- http header, 对 refer 做判断看来源是不是自己的网站，如果不是就拒绝
- 通过 session 校验，如果不通过特定服务生成 cookie 和 session 就不能请求得到资源

### http 协议缓存机制

https://segmentfault.com/a/1190000010690320

### Http 与 Https 的区别

- HTTP 的 URL 以 http:// 开头，而 HTTPS 的 URL 以 https:// 开头
- HTTP 是不安全的，而 HTTPS 是安全的
- HTTP 标准端口是 80 ，而 HTTPS 的标准端口是 443
- 在 OSI 网络模型中，HTTP 工作于应用层，而 HTTPS 的安全传输机制工作在传输层
- HTTP 无法加密，而 HTTPS 对传输的数据进行加密
- HTTP 无需证书，而 HTTPS 需要 CA 机构 wosign 的颁发的 SSL 证书

### 什么是 Http 协议无状态协议?怎么解决 Http 协议无状态协议?

无状态协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息也就是说，<br>
当客户端一次 HTTP 请求完成以后，客户端再发送一次 HTTP 请求，HTTP 并不知道当前客户端是一个”老用户“。<br>

可以使用 Cookie 来解决无状态的问题，Cookie 就相当于一个通行证，第一次访问的时候给客户端发送一个 Cookie，<br>
当客户端再次来的时候，拿着 Cookie(通行证)，那么服务器就知道这个是”老用户“。<br>

### 网页从输入网站到渲染经历了哪些过程?

1. 输入网址
2. 发送到 dns 服务器，并获取域名对应的 web 服务器对应的 ip 地址
3. 与 web 服务器建立 TCP 连接
4. 浏览器向 web 服务器发送 http 请求
5. web 服务器响应请求，并返回指定 url 的数据
6. 浏览器下载 web 服务器返回的数据及解析 html 源文件
7. 生成 DOM 树，解析 css 和 js,渲染页面，直至显示完成

### 常用的 HTTP 方法有哪些

- GET：用于请求访问已经被 URL（统一资源标识符）识别的资源，可以通过 URL 传参给服务器。
- POST：用于传输信息给服务器，主要功能与 Get 方法类似，但一般推荐 POST 方式。
- PUT：传输文件，报文主体包含文件内容，保存到对应 URL 位置。
- HEAD：获取报文首部，与 GET 方法类似，只是不返回报文主体，一般用于验证 URL 是否有效。
- DELET：删除文件，与 PUT 方法相反，删除对应 URL 位置的文件。OPTIONS：查询相应 URL 支持的 HTTP 方法。

## 浏览器

### 浏览器渲染过程

> 四个步骤。打油诗曰:先是生成 DOM 树，再次生成规则树，二者合为渲染树，遍历计算树节点，绘制节点至屏幕。

- 解析 html 生成 DOM 树
- 解析 css 生成 cssDOM 规则树
- 将 html DOM 树和 cssDOM 规则树合并在一起，生成渲染树
- 遍历渲染树，开始布局，计算渲染书节点的大小和位置
- 将每个节点绘制到屏幕上

### 域名收敛

PC 时代为了突破浏览器的域名并发限制。有了域名发散。
浏览器有并发限制，是为了防止 DDOS 攻击。
域名收敛：就是将静态资源放在一个域名下。减少 DNS 解析的开销。
域名发散：是将静态资源放在多个子域名下，就可以多线程下载，提高并行度，使客户端加载静态资源更加迅速。
域名发散是 pc 端为了利用浏览器的多线程并行下载能力。而域名收敛多用与移动端，提高性能，因为 dns 解析是是从后向前迭代解析，如果域名过多性能会下降，增加 DNS 的解析开销。

#### 如何实现渐进式渲染

- 图片懒加载——页面上的图片不会一次性全部加载。当用户滚动页面到图片部分时，JavaScript 将加载并显示图像。
- 确定显示内容的优先级（分层次渲染）——为了尽快将页面呈现给用户，页面只包含基本的最少量的 CSS、脚本和内容，然后可以使用延迟加载脚本或监听`DOMContentLoaded`/`load`事件加载其他资源和内容。
- 异步加载 HTML 片段——当页面通过后台渲染时，把 HTML 拆分，通过异步请求，分块发送给浏览器。更多相关细节可以在[这里](http://www.ebaytechblog.com/2014/12/08/async-fragments-rediscovering-progressive-html-rendering-with-marko/)找到。

### cookie、localStorage、sessionStorage 的异同

#### 相同点

- 都是客户端存储机制
- 数据都是以键值对的形式存储在客户端
- 存储的数据都为字符串

#### 不同点

- 存储的大小:cookie 为 4kb,localStorage 和 sessionStorage 为 5M.
- 有效期:cookie 为手动设置的时间;localStorage 一直存在，直至浏览器清理掉缓存;sessionStorage 为页面关闭时
- 服务器是否可以直接访问和设置:cookie 可以，其余二者不可.
- 访问权限:cookie 和 localStorage 为域名下的任意窗口,sessionStorage 为当前页面
- 在浏览器会话的期间是否会更改:cookie 取决于是否设置过期时间,localStorage 不会更改,sessionStorage 则会更改。
  cookie 在浏览器和服务器间来回传递。 sessionStorage 和 localStorage 不会

#### 如何设置

- cookie:document.cookie="userId=828; userName=hulk";
- localStorage: localStorage.setItem("username","hulk");
- sessionStorage: sessionStorage.setItem("username","hulk");

### 兼容性问题

> 2 个方向:兼容性问题产生的原因、如何解决兼容性问题；解决问题又分为:要不要做，要做的话做到什么程序、怎么做。

#### 产生原因

- 无统一的浏览器:浏览器产商根据自己对浏览器的需求开发不同的浏览器、浏览器功能不一
- 浏览器版本:用户使用的浏览器版本不一:有的使用版本较新，有的使用版本较老。

#### 如何解决兼容性问题

##### 要不要做

- 产品的目标客户：大部分目标用户使用的浏览器版本、对产品本身的要求(是以功能为主，还是以呈现页面为主)
- 成本:投入产出比是否高，是否有盈利的空间

##### 做到什么程序

- 需要支持什么浏览器
- 浏览器要支持到哪个版本

##### 怎么做

- 根据兼容性要求选择相应的库，比如 bootstrap
- 使用兼容性工具，比如(html5shiv.js、respond.js、css reset、normalize.css、Modernizr)
- 条件注释、CSS Hack、js 能力检测做一些修补
- 渐进增强和优雅降级
  - 渐进增强:先针对低版本浏览器做开发，保证一些基本的需求，然后再对高浏览器进行交互、效果等功能的改进，以期达到提高用户体验的要求。
  - 优雅降低:按照版本高的浏览器进行完整功能的开发，再按照需要兼容的低版本浏览器，进行功能和效果的改进
- 使用 `autoprefixer` 自动生成 CSS 属性前缀。
- 使用 Reset CSS 或 Normalize.css。

### 同源策略

协议、域名、端口三者相同。 由于同源策略产生安全问题。

同源策略是浏览器的一个安全功能。URL 由协议、域名、端口和路径组成。比较两个 url,如果协议、域名或端口三者有一个不同，那就是不同源。浏览器采用同源策略，禁止页面加载或执行与自身来源不同的域的脚本。比如，如果客户端与服务器的域名不一，那么服务器将不允许客户端访问。不受同源策略影响的标签:script、img、iframe、link。

### 跨域

跨域是指从一个域的网页去请求另一个域。（域名）  
方法:
jsonp、 iframe、window.name、window.postMessage、服务器上设置代理页面

- jsonp，允许 script 加载第三方资源
- 反向代理(ngix 服务内部配置 Access-Control-Allow-Origin\*)
- cors 前后端协作设置请求头部,Access-Controll-Allow-Origin 等头部信息
- iframe 嵌套通讯,postmessage

#### cors 跨域

当你使用 XMLHttpRequest 发送请求时，浏览器发现该请求不符合同源策略，会给该请求加一个请求头：Origin，后台进行一系列处理，如果确定接受请求则在返回结果中加入一个响应头：Access-Control-Allow-Origin;浏览器判断该相应头中是否包含 Origin 的值，如果有则浏览器会处理响应，我们就可以拿到响应数据，如果不包含浏览器直接驳回，这时我们无法拿到响应数据。

#### jsop 与 cors 的区别

- JSONP 只能实现 GET 请求，而 CORS 支持所有类型的 HTTP 请求。
- JSONP 无法判断是否请求失败，

#### 什么是 jsonp

有一些标签不受同源策略影响，我们就把数据封装好，返回给这些标签。jsonp 指的是其中的一种非正式传输协议，它的要点是允许用户传递一个**callback**参数给服务端，然后服务端返回数据会将整个 callback 参数作为函数名来包裹住 json 数据。仅用于 get 请求

### 当你在浏览器输入一个地址会发生什么

https://github.com/skyline75489/what-happens-when-zh_CN/blob/master/README.rst?utm_medium=social&utm_source=wechat_session&from=timeline&isappinstalled=0
查找浏览器缓存
DNS 解析、查找该域名对应的 IP 地址、重定向（301）、发出第二个 GET 请求
进行 HTTP 协议会话
客户端发送报头(请求报头)
服务器回馈报头(响应报头)
html 文档开始下载
文档树建立，根据标记请求所需指定 MIME 类型的文件
文件显示
[
浏览器这边做的工作大致分为以下几步：

加载：根据请求的 URL 进行域名解析，向服务器发起请求，接收文件（HTML、JS、CSS、图象等）。

解析：对加载到的资源（HTML、JS、CSS 等）进行语法解析，建议相应的内部数据结构（比如 HTML 的 DOM 树，JS 的（对象）属性表，CSS 的样式规则等等）
}

### 分域名请求图片的原因和好处？

浏览器的并发请求数目限制是针对同一域名的，超过限制数目的请求会被阻塞
浏览器并发请求有个数限制，分域名可以同时并发请求大量图片

### 页面的加载顺序

html 顺序加载，其中 js 会阻塞后续 dom 和资源加载，css 不会阻塞 dom 和资源的加载
浏览器会使用 prefetch 对引用的资源提前下载
没有 defer 或 async，浏览器会立即加载并执行指定的脚本
有 async，加载和渲染后续文档元素的过程将和 script.js 的加载与执行并行进行（下载一部，执行同步，加载完就执行）
有 defer，加载后续文档元素的过程将和 script.js 的加载并行进行（异步），但是 script.js 的执行要在所有元素解析完成之后，DOMContentLoaded 事件触发之前完成

### 常见浏览器的内核有哪些?

- Trident 内核，也称 IE 内核。 IE,360,搜狗浏览器
- Webkit 内核, safari,chrome 等
- Gecko 内核,Firefox,
- Presto 内核,opera7 以上

## ajax

### 创建 ajax 的过程

1. 创建 XMLHttpRequest 对象，也就是创建一个异步调用对象
2. 创建一个新的 HTTP 请求，并指定改 HTTP 请求的方法、URL 以及验证信息
3. 设置响应 HTTP 状态变化的函数
4. 发送 HTTP 请求
5. 获取异步调用返回的数据
6. 使用 javascript 和 DOM 实现局部刷新
   代码实现:

```javascript
<script type="text/javascript">
    window.onload = function(){
        //第一步：创建xhr对象
        //xhr是一个对象；里面可以放很多东西，数据；
        var xhr = null;
        if(window.XMLHttpRequest){//标准浏览器
            xhr = new XMLHttpRequest();//创建一个对象
        }else{//早期的IE浏览器
            xhr = new ActiveXObject('Microsoft.XMLHTTP');//参数是规定的；
        }
        console.log("状态q"+xhr.readyState);//0
        //第二步：准备发送请求-配置发送请求的一些行为
        //open即打开链接，第一个参数是以什么方式；第二个是往哪儿发送请求，第三个可以不写，默认true,表示异步，false表示同步；；
        xhr.open('get','03form.php',true);
        console.log("状态w"+xhr.readyState);//1

        //第三步：执行发送的动作
        //send也可以写在前面，推荐写在后面；写null是兼容问题；
        xhr.send(null);
        console.log("状态e"+xhr.readyState);//1

        //第四步：指定一些回调函数，也属于事件函数；不触发不执行，触发条件是xhr.readyState;z这个值有0-4，共5个状态，是由浏览器控制的；
        xhr.onreadystatechange = function(){
            if(xhr.readyState == 4){//4指服务器返回的数据可以使用；
                if(xhr.status == 200){ //判断已经成功的获取了数据；200表示hTTP请求成功；404表示找不到页面；503表示服务器端有语法错误；
                    var data = xhr.responseText;//json，文本，主角；
                    // var data1 = xhr.responseXML;
                }
            }
            // console.log("状态t"+xhr.readyState);//2表示已经发送完成；

            // console.log(1234);
        }

        // console.log(456);
        console.log("状态r"+xhr.readyState);//1


    }
    </script>
```

### ajax 的 readstate 有几种类型，分别代表的是什么意思?

- 0:代表未初始化,还没有调用 open 方法
- 1:代表正在加载，open 方法已被调用，但是 send 方法还没有被调用
- 2:代表已加载完毕，send 已被调用，请求以及开始
- 3:代表交互中，服务器正在发送响应
- 4:代表完成，响应发送完毕

### 如何解决 ajax 无法后退的问题

- html5 里引入了新的 API，即：history.pushState,history.replaceState
- 可以通过 pushState 和 replaceSate 接口浏览器历史，并且改变当前页面的 URL
- onpopstate 监听后退