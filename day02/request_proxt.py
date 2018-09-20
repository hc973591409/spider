import requests

# 公开代理
def main1():
    proxies = {
        "http": "114.113.126.86:80",
        "https": "114.113.126.87:80",
    }

    url = 'http://www.baidu.com'

    html = requests.get(url,proxies = proxies)
    print(html.content.decode('utf-8'))


# 私密代理
def main():
    proxies = {
       "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816"
    }

    url = 'http://www.baidu.com'

    html = requests.get(url,proxies = proxies)
    print(html.content.decode('utf-8'))

if __name__ == '__main__':
    main()