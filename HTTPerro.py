# 异常错误处理

import urllib.request
import urllib.error

# 没有网络连接
# 服务器连接失败
# 找不到指定的服务器

def main1():
    # 构建一个不存的站点请求
    request = urllib.request.Request("http://www.ajkfhafwjqh.com")
    try:
        # 请求站点，设置超时时间
        urllib.request.urlopen(request,timeout=5)
    except urllib.error.URLError as err:
        # <urlopen error timed out>
        # 这样就能捕获错误类型
        print(err)


def main():
    # 构建一个不存的站点请求
    request = urllib.request.Request("http://www.ajkfhafwjqh.com")
    try:
        # 请求站点，设置超时时间
        urllib.request.urlopen(request)
    except urllib.error.HTTPError as err:
        # <urlopen error timed out>
        # 这样就能捕获错误类型
        print(err)
        print(err.code)
        # <urlopen error [WinError 10060] 
        # 由于连接方在一段时间后没有正确答复或连接的主机
        # 没有反应，连接尝试失败。>

if __name__ == '__main__':
    main()