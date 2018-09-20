# 用resquets完成有道翻译

# POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1

import requests

def main():
    header = {"User-Agent":"Mizalla 5.0"}
    data={
        "i":"中国",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"1537287070130",
        "sign":"f84b3944dd41a290db12e93df5e0e1c8",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_CLICKBUTTION",
        "typoResult":"false"
        }
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    js = requests.post(url,data=data, headers=header)
    # js.json()按json格式显示
    print(js.json())

if __name__ == '__main__':
    main()
