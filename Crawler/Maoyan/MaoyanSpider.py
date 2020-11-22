import requests
from requests.exceptions import RequestException
import re
import json
import time

#获取单页的html
def get_one_page(url):
    headers = {
        'Host':'maoyan.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

#通过正则表达式解析html
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>',re.S)
    results = re.findall(pattern,str(html))
    for result in results:
        yield {
            'rate':result[0],
            'image':result[1],
            'name':result[2],
            'actor':result[3].strip()[3:],
            'time':result[4].strip()[5:],
            'score':result[5]+result[6]
        }

#保存到文件
def save_to_file(content):
    with open('MaoYanTop100.txt','w',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

#实现多个页面的自动爬取和文件保存
def main():
    for i in range(10):
        offset = i*10
        url = 'http://maoyan.com/board/4?offset='+str(offset)
        print(url)
        html = get_one_page(url)
        for content in parse_one_page(html):
            print(content)
            save_to_file(content)
        time.sleep(1)

if __name__=='__main__':
    main()