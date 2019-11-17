import re
import json
import requests


class LetvSpider(object):
    COMMENT_URL = "http://api.my.le.com/vcm/api/list?jsonp=jQuery19108667127834739425_1568040457178&type=video&rows=20&page=2&sort=&cid={cid}&source=1&xid={xid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1&_=1568040457190"

    HEADERS = {
        "Referer": "http: // www.le.com/ptv/vplay/1333316.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }

    def __init__(self, url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()
        self.get_comment()

    def get_request(self, url, headers):
        return requests.get(url, headers).content.decode()

    def get_necessary_id(self):
        source = self.get_request(self.url, self.HEADERS)
        cid = re.search('cid: (\d+)', source).group(1)
        vid = re.search('vid: (\d+)', source).group(1)
        pid = re.search('pid: (\d+)', source).group(1)
        self.necessary_info['cid'] = cid
        self.necessary_info['vid'] = vid
        self.necessary_info['pid'] = pid

    def get_comment(self):
        url = self.COMMENT_URL.format(
            cid=self.necessary_info['cid'], xid=self.necessary_info['vid'], pid=self.necessary_info['pid'])
        source = self.get_request(url, self.HEADERS)
        source_json = source[source.find('{"'):-1]
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(
                f'发帖人:{comment["user"]["username"]}, 评论内容:{comment["content"]}')


if __name__ == "__main__":
    spider = LetvSpider('http://www.le.com/ptv/vplay/1333316.html')
