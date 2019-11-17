# 快速解析HTML

> 正则表达式匹配HTML元素过于麻烦。而网页又是基于文档对象模型产生的节点树。基于此，我们可以根据节点数去获取节点中的内容，而不是自己使用正则去手动匹配

## XPath

> XPath(XML Path)是一种查询语言，它能够在XML和HTML中寻找节点

### 安装`lxml`

要使用XPath，首先要安装`lxml`库

直接在`pycharm`里面`import lxml`即可，选择自动下载安装`lxml`

### 语法

```python
import lxml.html
selector = lxml.html.fromstring("网页源代码")
info = selector.xpath('xPath语句')
# info = selector.xpath('//div[@class='useful']/ul/li/text()')
```

#### 语句

> 写XPath就是写地址

##### 获取文本

```python
//标签[@属性1=属性值]/标签2[@属性2=属性值]/..../text()
```

##### 获取属性值

```python
//标签1[@属性1=属性值]/标签2[@属性2=属性值]/.../@属性n
```

#### 其他

##### 相同标签不同属性

- 相同属性开头：使用`start-with`

```python
div[starts-with(@id, "test")]/text()
```

以上语句写明，查找一个div, 且div的id属性是以test开头

- 含有相同属性:使用`contains`

```python
div[contains(@id, "key")]/text()
```

以上语句写明，查找一个div, 且div的id属性包含key

##### 使用XPath查找返回XPath对象

```python
useful = selector.xpath('//div[@class='useful']') # 返回一个列表
info_list = useful[0].xpath('ul/li/text()')
```

再搜索的时候开头不需要加上`//`，直接以标签名开头即可

##### 搜索子标签内容

XPath只会搜索当前标签当前层级的文字，不会搜索子标签的内容，我们可以使用`string(.)`关键字

```python
data = selector.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
```

#### 注意

- 当以html开头的时候，前面是单斜线

```python
/html/body/div[@class="useful"/ul/li/text()]
```

- 属性非必写
- 以标志性标签开头：倒着找
- XPath中的标签属性是从1开始的

### 实例：使用XPath抓取百度贴吧中许嵩相关的帖子标题，并保存为txt

[抓取许嵩相关帖子](./抓取许嵩相关帖子.md)

## Beautiful Soup 4

### 安装

直接写入`from bs4 import BeautifulSoup`, pycharm将会自动安装

### 使用步骤

1. 处理源代码生成BeautifulSoup对象
2. 使用find_all()或者find()来查找内容

### 语法

soup = BeautifulSoup(网页源代码，'解析器')

解析器:

- html.parse
- lxml

```python
soup = BeatifulSoup(source, 'lxml')
```

#### find和find_all

- 用class_替代class

##### find

>  返回BeautifulSoup的Tag对象。如果找到多个符合要求的标签，返回第一个。如果没有找到，返回None。通过string方法可以读取标签中的文字

```python
soup = BeautifulSoup(html, 'lxml')
info = soup.find(class_="test")
prinf(info.string)
```

##### find_all

> 返回的是Beautiful-Soup Tag对象组成列表，如果没有找到符合要求的标签，就会返回空列表

```python
find_all(name, attrs, recursive, text, **kwargs)
- name: 标签名
- attrs: 字典,属性名-属性值
	attrs = {'class': 'useful'}
- recursive true/false false的时候bs4不会搜索子标签
- text 字符串或者正则表达式，用于搜索标签里面的文本信息
content = soup.find_all(text=compile('我需要'))
- **kwargs 键值对
	find_all('div', class_ = "iamstrange")
    支持正则:
    find_all('div', class=re.compile('iam'))
```

```python
soup = BeautifulSoup(html, 'lxml')
useful = soup.find(class_='userful')
all_content = useful.find_all('li')
```

### 实例：使用bs4抓取百度贴吧中全职高手相关的帖子标题，并保存为txt

与XPath类似，需要注意的是bs4不在意class是否有空格，而XPath中对是否有空格特别关注

```python
import os
import requests
from bs4 import BeautifulSoup
import lxml


def query(url):
    html = requests.get(url).content.decode()
    return html


def save(title):
    file_path = os.path.join(os.getcwd(), 'the_king_avatar.txt')
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(title)


# 开始抓取
content = query('https://tieba.baidu.com/f?ie=utf-8&kw=全职高手&fr=search')
soup = BeautifulSoup(content, 'lxml')
block = soup.find_all(class_='threadlist_title pull_left j_th_tit')
for item in block:
    sub_title = item.find('a')
    save(sub_title.text + '\n')

```

## 实例:抓取大麦网演出爬虫

[抓取大麦网爬虫](抓取大麦网爬虫.md)