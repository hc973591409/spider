import urllib.request
# 用于转码
import urllib.parse


def main1():
    """直接请求"""
    # 首先需要导入用到的模块：urllib.request

    # 在导入了模块之后，我们需要使用urllib.request.urlopen
    # 打开并爬取一个网页，此时，可以输入如下代码爬取百度首页
    # (www.baidu.com)， 爬取后，将爬取的网页赋给了变量file：

    request = urllib.request.Request('http://www.baidu.com/')
    # 构建请求

    file = urllib.request.urlopen(request)
    # 打开请求

    # 一次读取全部内容
    data = file.read().decode('utf-8')

    print(data)


def main2():
    """包一层浏览器的皮访问"""
    ua_header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
                 'Upgrade-Insecure-Requests': '1'
                 }

    '''
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

    '''
    request = urllib.request.Request(
        'http://www.baidu.com/', headers=ua_header)
    # 也可以再构造后增加头

    request.add_header('Connection', 'keep-alive')

    response = urllib.request.urlopen(request)

    # print(response.read().decode('utf-8'))
    # 获取响应状态码
    print(response.code)


import random


def main3():
    """随机构建浏览器代理头"""
    url = 'http://www.baidu.com/'
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; ) Apple....) ",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0)...) ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X....) ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS... )"
    ]
    # 随机选择一个浏览器头
    user_agent = random.choice(ua_list)
    # 构建请求
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    print(user_agent)
    print(request.get_header('User-agent'))

    # 请求响应
    response = urllib.request.urlopen(request)

    html = response.read().decode('utf-8')
    print(html)

# https://www.baidu.com/s?wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2
# wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2(传智播客)
def main():
    """
    当我们需要传递参数的时候就需要编码解码工作
    """
    word = {'wd':'传智播客'}
    # 编码
    wd = urllib.parse.urlencode(word)

    print(wd)
    # wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2

    # 解码
    print(urllib.parse.unquote('wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2'))

if __name__ == '__main__':
    main()
