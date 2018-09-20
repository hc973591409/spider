import requests

def main():
    header = {"User-Agent":"Mizalla 5.0"}
    url = 'http://www.baidu.com/s?'
    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    kw = {'wd':"长城"}
    html = requests.get(url,params=kw,headers=header)
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    # print(html.text)
    # # 查看响应内容，response.content返回的字节流数据
    # print(html.content.decode('utf-8'))
    # 查看完整url地址
    # print(html.url)

    # 查看响应头部字符编码
    print(html.encoding)
    # 查看响应的状态吗
    print(html.status_code)
    

if __name__ == '__main__':
    main()