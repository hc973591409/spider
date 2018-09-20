# ajax找数据，后台数据都是json格式，只需要找到json的传输 url
# 就可以
import urllib.request
import urllib.parse


def main():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

    form_data = {
        "start": "0",
        "limit": "20"
    }

    data = urllib.parse.urlencode(form_data)
    data = data.encode('utf-8')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

    resquest = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(resquest)

    with open('douban.json', 'w', encoding="utf-8") as f:
        f.write(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
