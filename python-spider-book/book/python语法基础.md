# Python语法基础

## windows安装

1. 安装>3的版本，默认安装即可
2. 如何确定安装

在cmd输入`python`，如果出现提示，那么安装成功

## 数据结构和控制结构

### 整数、浮点数和变量

#### 加减乘除

> 浮点数运行将会有偏差，不应该在Python中直接进行浮点数的运算，这种情况在java、c、c++等语言都存在

```python
# 加减乘除
print(1234)
print("1.234")
print(1-10)
print(3+2-5*0)
print((3+2-5)*0)

# 0.30000000000000004
print(0.1+0.2)
```

#### 变量

> 变量就是一个存放数据的盒子

```python
# 变量
长 = 10
宽 = 15
高 = 2

底面积 = 长 * 宽
体积 = 底面积 *高

print(底面积)
print(体积)
```

py3支持中文变量，但是最好使用英文名

##### 预定义变量

`__name__`: 模块名称，默认为`__main__`。系统自动判断，如果是导入的模块，那么`__name__`等于导入的模块名称。否则，默认为当前的主模块`__main__`

### 字符串、列表、元祖

#### 字符串

> 用单引号或者双引号括起来的

#### 列表

> 列表的每一项就做元素

```python
a = [1,2,3,4,5]
print("数字列表:",a)
a = ['1','2','3','4','5']
print("字符串列表:",a)
a = []
print("空列表",a)

a = ['1','2',1,2,'abc',['1','2']]
print("混合列表",a)

# 添加元素
a.append('4')

# 合并列表
a.extend(['6', '7', '8'])

# 移除末尾元素
a.pop()
```

##### 列表生成

```python
# 生成1-10的列表
 range(1, 11)
    
    
# 生成[1x1, 2x2, 3x3, …, 10x10]
list_1 = []
for x in range(1, 11):
    list_1.append(x*x)

#	列表生成式
list_1 = [x*x for x in range(1, 11)]
```



#### 元祖

> 元祖是不可以修改元素的列表

```python
# 元祖
tup1 = ('a','b','c','d')
print(tup1)
tup1 = ()
print(tup1)
tup1 = ('a','b','c')
print(tup1)
```

### 数据的读取

```js
my_str = "我是字符串"
my_list = ['我', '是', '列', '表']
my_tuple = ('我', '是', '元', '组')
# 我 我 我
print("第一个元素", my_str[0], my_list[0], my_tuple[0])
# 字 列 元
print("下表为2的元素", my_str[2], my_list[2], my_tuple[2])
# 串 表 组
print("最后一个元素", my_str[-1], my_list[-1], my_tuple[-1])
# 符 列 元
print("倒数第二个元素", my_str[-2], my_list[-2], my_tuple[-2])
# 我 ['我'] ('我',)
print("切片0:1", my_str[0:1], my_list[0:1], my_tuple[0:1])
# 我是 ['我','是']  ('我','是')
print("切片0:2", my_str[0:2], my_list[0:2], my_tuple[0:2])
# 字符 ['列', '表']  ('元','组')
print("切片2:4", my_str[2:4], my_list[2:4], my_tuple[2:4])

print("从第一个元素到下标为1的元素", my_str[0:2], my_list[0:2], my_tuple[0:2])
print("从第一个元素到下标为1的元素", my_str[:2], my_list[:2], my_tuple[:2])

print("从下标为1的元素直到全部", my_str[1:], my_list[1:], my_tuple[1:])

print("切片去掉最后一个元素", my_str[:-1], my_list[:-1], my_tuple[:-1])

print("切片去掉最后两个元素", my_str[:-2], my_list[:-2], my_tuple[:-2])

# 我 字 串 ['我','列'] ('我','元')
print("每两个字取一个字", my_str[::2], my_list[::2], my_tuple[::2])
# 串符字是我 ['表', '列', '是', '我'] ('组','元', '是', '我')
print("倒序输出", my_str[::-1], my_list[::-1], my_tuple[::-1])
```

#### 切片的读取

切片的格式

```js
变量名[开始位置下标:结束位置下标:步长]
```

切片不包括结束的元素

#### 拼接和修改

```js
# 我是
str1 = '我'
str2 = '是'
print("字符串拼接", str1 + str2)
# ['我','是']
list1 = ['我']
list2 = ['是']
print("列表的拼接", list1 + list2)
# 我是
tuple1 = ('我')
tuple2 = ('是')
print("元祖的拼接", tuple1 + tuple2)
```

元祖拼接将会是字符串

修改列表：直接通过下标修改

列表在末尾可单独添加元素 `list1.append('element')`

元祖和字符串不能添加新内容，不能修改元祖内的非可变容器元素

### **字典与集合**

- 字典里面的键名不能重复，里面的元素是无序的。
- 集合是没有值的字典，里面的元素是无序的。

#### 字典

```python
dict_1 = {"name": "vine", "age": 12}
# vine
print(dict_1['name']) 
# vine
print(dict_1.get('name')
# unknown
print(dict_1.get('me', 'unknown'))// unknown 找不到键名用这个替换
```

> 字典多重控制

```python
# 字典多重控制
state = "read"
state_dict = {"read": 1, "run": 2, "other": 3}
cur_state = state_dict.get(state, 3)
print(cur_state)
```

#### 集合

> 集合去重

```js
# 去重
list4 = ['1', '2', '3', '4', '1', '2', '3'];
# ['1', '2', '3', '4']
print(list(set(list4)))
```

### 条件语句

```python
a = 1
b = 2

# 普通的if-else语句
if a+b == 3:
    print("正确")
else:
    print("错误")
# 逻辑表达式 and
if 1+1 == 2 and 2+2 == 4:
    print("答案正确")
# 逻辑表达式 or
if 1+1 == 2 or 2+2 == 4:
    print("答案正确")
# if-and 读取元素
list6 = []
if len(list6) > 0 and list6[100]:
    print(list6)
else:
    print("列表或者元素有误")

# if-elif
name = "回锅肉"
if name == "回锅肉":
    print('15元')
elif name == "水煮肉片":
    print("20元")
elif name == "米饭":
    print("1元")
elif name == "鸡汤":
    print("1角")
else:
    print("没有该道菜")


```

### for循环与while循环

#### for循环

```python
# 控制循环次数
for i in range(5):
    print("现在是第{}次循环".format(i))

# 循环列表
list_1 = [1, 2, 3, 4]
for item in list_1:
    print(item)

# 循环字符串
name = "vine"
for character in name:
    print(character)

# 循环字典
fruit_price = {"苹果": 10.11, "香蕉": 12.11,  "榴莲":12.11}
for key in fruit_price:
    print("水果:{}".format(key))
    print("价格:{}".format(fruit_price[key]))
    print("=========================")
```

#### while 循环

> while循环主要用知道循环要执行多少次的情况

#### 普通while循环
```python
# while循环
i = 0
while i < 10:
    print("现在是第{}次循环".format(i))
    i += 1
    
```

#### 永久运行

```python
import time
while True:
    print('执行')
    time.sleep(1)
```

ps: time.sleep(1): 间隔一秒。防止循环超过速运行，爬虫被封。

跳出循环break，跳出本次循环continue

## 函数

### 函数

> 按照python变成规范，一个函数的函数体不超过20行代码，如果超过了，就说明需要将该函数拆分为更小的函数，也意味着在函数体里面可以调用其他的函数

#### 定义函数

```python
def basic_calculate(a, b):
    print("和：{}".format(a + b))
    print("差：{}".format(a - b))
    print("乘积：{}".format(a * b))
    print("除余：{}".format(a / b))


basic_calculate(3, 4)
```

#### return 

没有return === return; ==== return None

## 面向对象与类

### 面向对象基本概念

- **类(Class):** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- **方法：**类中定义的函数。
- **类变量：**类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- **数据成员：**类变量或者实例变量用于处理类及其实例对象的相关的数据。
- **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- **局部变量：**定义在方法中的变量，只作用于当前实例的类。
- **实例变量：**在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
- **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- **实例化：**创建一个类的实例，类的具体对象。
- **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

### python类的特殊之处

- `__init__()`:构造方法，在实例化的时候会自动调用, init可以有参数，参数可以通过`__init__()`传递到类的实例化操作上。

- `self`:代表的是类的实例，而非类,代表的是当前对象的地址，self.calss指向类。

- 类的方法必须有一个额外的第一个参数名称，为self，代表的是类的实例
- 

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5

```

- **__private_method**：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。**self.__private_methods**。

参考: [python面向对象](runoob.com/python3/python3-class.html)

### 示例

- 类名
- 父类
- 初始化方法（构造函数）
- 属性
- 方法

### 示例

> 新式类

```python
class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.jump()

    def walk(self):
        print("我的名字叫做：{}，我正在走路".format(self.name))

    def eat(self):
        print("我的名字叫做：{},我正在吃饭".format(self.name))

    def jump(self):
        print("我的名字叫做:{},我跳了一下".format(self.name))


zhang_san = People('张三', 12)
li_si = People('李四', 15)
print("=============执行类的属性=============")
print(zhang_san.name)
print(zhang_san.age)
print(li_si.name)
print(li_si.age)
print("=============执行类的方法=============")
zhang_san.walk()
zhang_san.eat()
li_si.walk()
li_si.eat() 
```

## 其他

### print

print(f'我的名字是{name}'):加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，如果字符串里面没有表达式，那么前面加不加f输出应该都一样

### join和split

join将列表中的元素用某个分隔符连接起来

split  将字符串按照某个分隔符分隔为列表

## 实例：猜数小游戏

```python
import random

history = {}


def try_to_guess(name, answer):
    try_num = 0
    while try_num < 10:
        guess_answer = int(input('请输入一个数字:'))
        if guess_answer < answer:
            print("你输入的数字比正确答案小")
        elif guess_answer == answer:
            print("你猜对了！")
            history[name].append('成功')
            break
        else:
            print("你输入的数字比正确答案大")
        try_num += 1
    else:
        print("猜错次数太多，失败")
        history[name].append('失败')


def show_history():
    if len(history) > 0:
        for name, data in history.items():
            print('用户:{},记录如下:{}'.format(name, data))
    else:
        print('当前无历史记录')


def start():
    name = input('请输入你的名字:')
    if name == "退出":
        return
    if name not in history:
        history[name] = []
    answer = random.randint(0, 1024)
    try_to_guess(name, answer)


def default():
    pass


if __name__ == '__main__':
    select_dict = {'1': show_history, '2': start, '3': exit}
    while True:
        select = input('1.历史记录\n2.继续游戏\n3.退出游戏\n输入数字选择:')
        select_dict.get(select, default())()

```