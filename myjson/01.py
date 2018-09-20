import json
import jsonpath
import requests


def main():
    url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.106 Safari/537.36 "
    }
    response = requests.get(url, headers=headers, verify=False)
    content = response.text
    # content 是json格式字符串
    py_obj = json.loads(content)
    # json.loads(content)把json格式字符串转为python格式字符串
    city_list = jsonpath.jsonpath(py_obj, '$..name')
    # 得到一个python数组
    json_city_list = json.dumps(city_list, ensure_ascii=False)          # 转为json格式 ensure_ascii为
    # True转为ascii编码，我们需要unicode字符串，所以禁用即可
    with open('city1.json', 'w', encoding='utf-8') as f:
        f.write(json_city_list)


if __name__ == '__main__':
    main()
