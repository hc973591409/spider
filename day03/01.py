from bs4 import BeautifulSoup


html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <!--<head> 123 </head>-->
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
print(html)
# 创建 Soup对象,用来解析html ,要指定解析库为lxml,不然会有警告
soup = BeautifulSoup(html, 'lxml')


def main1():

    # 打开本地文件
    # soup = BeautifulSoup(open('1.html'))
    # 格式化输出
    print(soup.prettify())

# Tag


def main2():
    # <title>The Dormouse's story</title>获取title标签
    print(soup.title)

    print(soup.p)

    print(soup.head)

    print(soup.a)

    # 获取name


def main3():
    # soup相当于整个文档 [document]
    print(soup.name)

    # head #对于其他内部标签，输出的值便为标签本身的名称
    print(soup.head.name)

    # {'class': ['title'], 'name': 'dromouse'}
    print(soup.p.attrs)

    print(soup.p['class'])  # soup.p.get('class')


def main4():
    # 获取p的文字内容
    print(soup.p.string)

# 子节点


def main5():
    #  .content 属性可以将tag的子节点以列表的方式输出
    print(soup.head.contents)
    # [<title>The Dormouse's story</title>]
    # 得到第一个的字符串
    print(soup.head.contents[0].string)

    # .children 返回的是一个list生成器
    print(soup.head.children)
    # <list_iterator object at 0x01037650>
    print('*'*50)
    # 接下来我们可以遍历他
    for child in soup.body.children:
        print(child)

# 所有子孙节点


def main7():
    #  .descendants 属性
    for child in soup.descendants:
        print(child)


# 节点内容
def main6():
    print(soup.head.string)
    print(soup.title.string)
    # 如果一个标签里面没有标签了，那么 .string 就
    # 会返回标签里面的内容。如果标签里面只有唯一的一个标签了，
    # 那么 .string 也会返回最里面的内


# 搜索文档树 # A.传字符串
def main8():
    # 最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容
    # 查找所有的b标签
    print(soup.find_all('b'))
    # 返回一个列表
    print(soup.find_all('a'))

import re
# B.传正则表达式
def main9():
    for tag in soup.find_all(re.compile(r"^b")):
        print(tag.name)
    # body b

# B.传列表
def main10():
    # 神奇,列表里面也可以正则
    print(soup.find_all(['a',re.compile(r"^b")]))

# keyword 参数
def main11():
    print(soup.find_all(id='link2'))

# 3）text 参数
def main12():
    print(soup.find_all(text=re.compile(r'Dormouse')))
    # print(soup.find_all(text="The Dormouse's story"))
    # 支持正则

# CSS选择器
# 通过标签名查找
def main13():
    # 标签选择器
    print(soup.select('title'))
    # 注意,这里是选择所有
    print(soup.select('a'))
    print(soup.select('b'))

# （2）通过类名查找
def main14():
    print(soup.select('.sister'))

# （3）通过 id 名查找
def main15():
    print(soup.select('#link1'))

# 组合查找
# 查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
def main16():
    print(soup.select('p #link1'))
    # 直接子标签查找，则使用 > 分隔 head的子标签titile
    print(soup.select("head > title"))

# 属性查找
def main17():
    # 查找lei为sister的a标签
    print(soup.select('a[class="sister"]'))

# 获取内容
def main():
    # 查找lei为sister的a标签
    print(soup.select('head'))



if __name__ == '__main__':
    main()
