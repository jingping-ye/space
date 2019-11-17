import os
import requests
import lxml.html


def query(url):
    html_page = requests.get(url).content
    return html_page


# 开始抓取
html_content = query('http://tieba.baidu.com/f?ie=utf-8&kw=%E8%AE%B8%E5%B5%A9&fr=search&red_tag=i0173573712')
selector = lxml.html.fromstring(html_content)
info = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
file_path = os.path.join(os.getcwd(), 'xusong.txt')
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines([x+'\n' for x in info])

