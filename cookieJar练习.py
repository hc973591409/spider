import http.cookiejar
import urllib.request,urllib.parse

# 管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象。
# 整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
cookie_jar = http.cookiejar.CookieJar()

# 构建cookie处理器啊
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 构建opener
opener = urllib.request.build_opener(cookie_handler)

opener.addheaders = [('User-Agent',"Mazilla/5.0")]

# 注册为全局的opener，以后就可以urlopen中用
urllib.request.install_opener(opener)

# 这是人人遗落没设置动态token的后端，可以仅仅使用cookie就可以登陆
url = "http://www.renren.com/PLogin.do"

# 输入账户密码
data = {"email":"973591409@qq.com","password":"huchao435"}

# 编码成16进制数据
data = urllib.parse.urlencode(data)

# post数据必须编码才能转换成二进制数据
data = data.encode('utf-8')

# 构建请求
request = urllib.request.Request(url,data=data)


response = opener.open(request)

# print(response.read().decode('utf-8'))
# 访问朋友的主页试试
# http://www.renren.com/387660126/profile

request1 = urllib.request.Request("http://www.renren.com/387660126/profile")

response1 = urllib.request.urlopen(request1)

print(response1.read().decode('utf-8'))
