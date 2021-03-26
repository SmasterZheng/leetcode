import requests
from bs4 import BeautifulSoup as bs
import re


def get_html(page):
    '''获取html'''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Referer':'http://cx.cnca.cn/'
    }


    url="https://neris.csrc.gov.cn/alappl/home/gongshi2.do?pageNo={}".format(page)
    strhtml = requests.get(url,headers=headers,verify=False)
    return strhtml.text

def parse_one_page():
    html=get_html(page=100)
    re.findall('嘉实基金')


if __name__ == '__main__':
    a=get_html(3)
    print(a)