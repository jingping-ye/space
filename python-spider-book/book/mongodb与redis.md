# MongoDB与Redis

## MongoDB

> 数据库，用来保存大量数据

数据在MongpDB中是按照库(Database) - 集合(Collections) - 文档(Document)的层级关系来存储的。

文档 字典

集合 包含很多字典的列表

### MongoDB的增删改查

#### pymongo

> 在安装完MongoDB之后再安装pymongo

```python
import pymongo
```

#### **连接/创建数据库**

```python
from pymongo import MongoClient

# 建立连接
# client = MongoClient("localhost", 27017)
# client = MongoClient("mongodb://localhost:27017/"")
client = MongoClient()

# 指定要进行操作的databse和collection
# database = client.Chapter6
# collection = database.spider
database = client['Chapter6']
collection = database['spider']
```

#### 插入数据

- insert_one 插入文档
- insert_many 插入集合

```python
# 写入数据
data1 = {'id': 123, 'name': 'kingname', 'age': '20', 'salary': '9999'}
collection.insert_one(data1)

data2 = [{'id': 123, 'name': 'kingname', 'age': '20', 'salary': '9999'}, {'id': 124, 'name': 'kingname', 'age': '20', 'salary': '9999'}]
collection.insert_many(data2)

data3 = []
data3.append(data1)
collection.insert_many(data3)

```

mongoDB会自动添加一列`_id`,里面的数据叫做ObjectId, ObjectId是在数据被插入mongoDB的瞬间，通过一定算法计算出来的。因此，_id这一列就代表数据插入的时间，它不重复，而且始终递增，通过一定的算法，可以把ObjectId反向恢复为时间

#### 删除数据

- delete_one 删除一条数据 参数为字典
- delete_many 删除多条数据 参数为字典

#### 修改数据

- replace_one
- update_one:该方法第一个参数为查询的条件，第二个参数为要修改的字段。 只能修改匹配到的第一条记录。
- update_many :该方法第一个参数为查询的条件，第二个参数为要修改的字段。 修改匹配到的所有记录。

```js
import pymongo
from pymongo import MongoClient
client = MongoClient()
database = client['Chapter6']
collection = database['spider']

# 修改数据
query_condition = {'age': 20}
new_value = {"$set": {'name': '叶敬平'}}
collection.update_one(query_condition, new_value)

# update_many
myquery = {"id":  123}
newvalues = {"$set": {"salary": 9000}}
collection.update_many(myquery, newvalues)
```

#### 查询数据

##### 普通查询

- find 返回满足条件的集合
- find_one 返回满足条件的文档

```python
from pymongo import MongoClient
client = MongoClient()
database = client['Chapter6']
collection = database['spider']

content1 = collection.find_one({'id':123})
print(content1)

content2 = collection.find({'id': 123})
for i in content2:
    print(i)

```

### 去重查询结果

```python
collection.distinct('列名')
```

## Redis

>  作为缓存和队列保存临时数据。基于内存的数据库，速度快于MongDB

设计一个开关，实现在不结束程序进程的情况下，从全世界任何一个有网络的地方既能随时暂停程序，又能随时恢复程序的运行。

### 操作列表

redis的列表是一个可读可写的双向队列，可以把数据从左侧或者右侧插入到列表中，也可以从左侧或者右侧读出数据，还可以查看列表的长度。

```python
# 左侧写入数据
lpush key value1 value2 value3 
# 左侧读取数据并从列表删除
lpop chapter_6
# 右侧写入数据
rpush key valu1 value2 value3
# 右侧读取数据并从列表删除
rpop chapter_6
# 查看列表的长度
llen
# 读取数据（不删除列表中的数据）
lrange key start end
```

python中的切片是左闭右开区间 test[0:3]读取的列表中的第0,1,2共3个值

### 操作集合

```python
# 添加数据
sadd key value1 value2 value3
# 读取数据并从集合中删除 count 读取多少个值
spop key count 
# 查看集合中有多少值
scard key

```

### python中使用redis

```python
import redis
client = redis.StrictRedis()


# 列表左侧添加
client.lpush('chapter_6', 123)
# 查看长度
list_len = client.llen('chapter_6')
print(list_len)
# 左侧读取并删除
client.lpop('chapter_6')
# 集合添加
client.sadd("test_set", "https://www.baidu.com")
# 集合读取并删除
client.spop("url")
# 读取长度
set_length = client.scard("url")
print(set_length)
```

## 优化操作

- 少读少写少更新
  - 批量插入，将值组合到一个列表中再插入
  - 一次性将数据读入内存
  - 如果要逐条更新，不如删除原来的数据，再重新批量插入
- 能用Redis就不用MongoDB
  - 拒绝频繁去数据库查询

## 实验:抓取小说白夜行的正文内容

要求：

- 抓取网址，并存到redis中名为url_queue的列表中
- 获取具体内容，并将内容保存到mongoDB中
- 使用XPath或者BS4

[抓取小说白夜行的正文内容](./抓取小说白夜行的正文内容.md)

