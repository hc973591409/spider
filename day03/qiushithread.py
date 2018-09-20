# 指定请求库
import requests
# 解决移除ssl验证以后的警告
import urllib3
# 解析库
from lxml import etree
# 存放为json格式
import json
# 多线程
from threading import Thread
from queue import Queue


class CrawlThread(Thread):
    def __init__(self, thread_name, page_q, data_q):
        super(CrawlThread, self).__init__()
        self.name = thread_name
        self.page_q = page_q
        self.data_q = data_q
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def run(self):
        print(self.name+'开始采集')
        while not self.page_q.empty():
            page = self.page_q.get()
            url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
            html = requests.get(url, headers=self.headers, verify=False).text
            self.data_q.put(html)
        print(self.name + '结束采集')


class ParseThread(Thread):
    def __init__(self, parse_name, data_q, filename):
        super(ParseThread, self).__init__()
        self.parse_name = parse_name
        self.data_q = data_q
        self.items = []
        self.filename = filename

    def run(self):
        print(self.parse_name + '开始本地写入')
        while not self.data_q.empty():
            page_html = self.data_q.get()
            xml = etree.HTML(page_html)
            node_list = xml.xpath('//div[contains(@id,"qiushi_tag")]')

            for node in node_list:
                item = {}
                item['content'] = (node.xpath('.//div[@class="content"]/span')[0].text).strip()
                item['fun'] = node.xpath('.//span[@class="stats-vote"]/i')[0].text
                item['comment'] = node.xpath('.//a/i[@class="number"]')[0].text
                item['img'] = node.xpath('.//a/img[@class="illustration"]/@src')
                self.items.append(item)

        # 把字典转化为json存起来
        js_obj = json.dumps(self.items, ensure_ascii=False)
        self.filename.write(js_obj)
        print(self.parse_name + '结束本地写入')


THREAD_COUNT = 5
PARSE_COUNT = 5
PAGE_COUNT = 50


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page_q = Queue(PAGE_COUNT)
    data_q = Queue()
    for page in range(1, PAGE_COUNT+1):
        page_q.put(page)

    try:
        filename = open('qiushi.json', 'a', encoding='utf-8')

    except Exception as e:
        print(e)
        return

    thread_name = ["采集线程1", "采集线程2", "采集线程3", "采集线程4", "采集线程5"]
    crawl_thread = []
    for i in range(THREAD_COUNT):
        thread = CrawlThread(thread_name[i], page_q, data_q)
        thread.start()
        crawl_thread.append(thread)

    for i in range(THREAD_COUNT):
        crawl_thread[i].join()

    # 开始解析线程
    parse_name = ["解析线程1", "解析线程2", "解析线程3", "解析线程4", "解析线程5"]
    parse_thread = []
    for i in range(PARSE_COUNT):
        thread = ParseThread(parse_name[i], data_q, filename)
        thread.start()
        parse_thread.append(thread)

    for i in range(PARSE_COUNT):
        crawl_thread[i].join()

    print("结束爬取")


if __name__ == '__main__':
    main()
