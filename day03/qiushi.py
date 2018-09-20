import requests
from lxml import etree
import json


def main():
    start_page = 1
    end_page = 10
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    items = []
    for page in range(start_page, end_page+1):
        url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
        print(url)
        html = requests.get(url, headers=headers, verify=False).text
        xml = etree.HTML(html)
        node_list = xml.xpath('//div[contains(@id,"qiushi_tag")]')

        for node in node_list:
            item = {}
            item['content'] = (node.xpath('.//div[@class="content"]/span')[0].text).strip()
            item['fun'] = node.xpath('.//span[@class="stats-vote"]/i')[0].text
            item['comment'] = node.xpath('.//a/i[@class="number"]')[0].text
            item['img'] = node.xpath('.//a/img[@class="illustration"]/@src')
            items.append(item)

    # 把字典转化为json存起来
    js_obj = json.dumps(items, ensure_ascii=False)
    with open("糗事.json", 'w', encoding='utf-8') as f:
        f.write(js_obj+'\n')


if __name__ == '__main__':
    main()
