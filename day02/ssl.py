import requests

# 我们可以不用处理ssl了

def main():
    # verify=False 不验证ssl
    # verify=True  验证ssl
    html = requests.get("https://www.baidu.com/", verify=False)
    print(html.text)

if __name__ == '__main__':
    main()