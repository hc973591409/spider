import urllib.request
import urllib.parse

"""
审查元素得到的ulr，translate_o要去掉_o
而且中-en
和en-中 地址是不一样的
POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
Host: fanyi.youdao.com
Connection: keep-alive
Content-Length: 202
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://fanyi.youdao.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://fanyi.youdao.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: OUTFOX_SEARCH_USER_ID=1049501019@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1487764529.0703373; JSESSIONID=aaa0mDsXzV8Lo4KaoRQxw; ___rl__test__cookies=1537240534979
"""


def main():
    form_data = {
        "i": "中国",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1537240535002",
        "sign": "82389c08a7cf94bd459a9d82b82fdb6f",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    data = urllib.parse.urlencode(form_data)
    data = data.encode('utf-8')

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 构建头
    ua_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    request = urllib.request.Request(url, data=data, headers=ua_header)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))


# 发生异常: TypeError
# POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
#   File "C:\Users\97359\Documents\GitHub\spider\post.py", line 45, in main
#     response = urllib.request.urlopen(request)
#   File "C:\Users\97359\Documents\GitHub\spider\post.py", line 50, in <module>
#     main()

# {"type":"ZH_CN2EN","errorCode":0,"elapsedTime":1,
# "translateResult":[[{"src":"中国","tgt":"China"}]]}

if __name__ == '__main__':
    main()
