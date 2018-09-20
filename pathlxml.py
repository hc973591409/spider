from lxml import etree

def test1():
    text = '''
    <div>
        <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
        </ul>
    </div>
    '''
    # 利用etree吧字符串解析为xml文档,返回一个xml对象
    html = etree.HTML(text)

    # html转换为字符串 ,k可以看到会自动闭合标签等
    result = etree.tostring(html)

    print(result)

def main1():

    # 利用etree.parse可以打开一个html文档，返回xml对象
    html = etree.parse("./1.html")

    # html转换为字符串 
    result = etree.tostring(html, pretty_print=True)

    print(result.decode('utf-8'))

def main():

    # 获取所有li
    html = etree.parse('./1.html')
    result = html.xpath('//li')
    print(result)

    # 获取li中的class属性
    result1 = html.xpath('//li/@class')
    print(result1)

    # 继续获取<li>标签下href 为 link1.html 的 <a> 标签
    result2 = html.xpath("//li/a[@href='link1.html']")

    # 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
    result2 = html.xpath("//li//span")

    # 获取li下a所有的class值 
    result = html.xpath("//li//a/@class")

    # 获取li最后一个下a的href
    result = html.xpath("//li[last()]//a/@href")

    # 获取li倒数第二个下a的文本值
    result = html.xpath("//li[last()-1]//a")
    # 这里返回的是只有一个数据的列表，取出第一个元素，利用text方法就可以获取文本
    print(result[0].text)

    # 获取class为bold的标签名
    result = html.xpath("//*[@class='bold']")
    # 用*代替任意标签，取出列表，用tag就可以取出标签
    print(result[0].tag)



if __name__ == '__main__':
    main()