import requests


def main1():
    """获取cookie"""
    response = requests.get("http://www.baidu.com")

    # 返回cookieJar对象
    cookieJar = response.cookies

    print(cookieJar)
    # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

    # 吧cookie转化为字典
    cookie_dict = requests.utils.dict_from_cookiejar(cookieJar)
    # {'BDORZ': '27315'}
    print(cookie_dict)


def main():
    header = {"User-Agent": "Mizalla 5.0"}
    # 人人网登录页面
    url = 'http://www.renren.com/PLogin.do'

    data = {
        "email": "973591409@qq.com",
        "password": "huchao435"
    }

    # 利用requests构建session对象，用于保存cookie
    sess = requests.session()
    response = sess.post(url, data=data, headers=header)
    # 主页
    main_url = "http://www.renren.com/410129709"
    # 此时的sess对象有session信息，可以直接访问
    html = sess.get(main_url,headers = header)
    print(html.text)


if __name__ == '__main__':
    main()
