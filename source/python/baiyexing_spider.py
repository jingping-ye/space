import time
import redis
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 配置数据库
client = MongoClient()
database = client['baiyexing']
collection = database['content']

# 使用redis
client = redis.StrictRedis()

# url_queue 访问队列 content_list 文章标题和内容
url_queue = []
content_list = []


# get请求
def query(url):
    html = requests.get(url).content.decode()
    return html


# 添加小说内容url至url_queue列队
def add_content_url(url):
    client.rpush('url_queue', url)


# 弹出url
def pop_content_url():
    return client.lpop('url_queue')


# 保存至数据库
def save_to_db():
    collection.insert_many(content_list)


# 获取小说详细url并添加至redis队列
def get_content_url():
    page = query('https://www.qisuu.la/du/24/24704/')
    soup = BeautifulSoup(page, 'lxml')
    toc_link = soup.find_all(class_='pc_list')[1].find_all('a')
    for link in toc_link:
        add_content_url('https://www.qisuu.la/du/24/24704/'+link['href'])


# 获取小说章节内容
def get_content(url):
    source = query(url)
    page = BeautifulSoup(source, 'lxml')
    title = page.find('h1').get_text()
    chapter = page.find(id='content1').get_text(strip=True)
    content_list.append({'title': title, 'chapter': chapter})


# 运行
def run():
    start = time.time()
    get_content_url()
    while client.llen('url_queue') > 0:
        url = pop_content_url()
        print(url)
        get_content(url)
    save_to_db()
    end = time.time()
    # 99.84998893737793
    print(f'用时{end - start}')


run()
