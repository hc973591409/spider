import urllib.parse
import urllib.request


def main():
    '''带参数的百度搜索'''

    ua_header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
                 'Upgrade-Insecure-Requests': '1'
                 }

    url = 'http://www.baidu.com/s'
    word = {'wd': '传智播客'}
    word = urllib.parse.urlencode(word)
    newurl = url + '?' + word

    request = urllib.request.Request(newurl, headers=ua_header)

    response = urllib.request.urlopen(request)

    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()
