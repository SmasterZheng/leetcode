# -*- coding: utf-8 -*-
# @Time    : 20201228
# @Author  : zhengxz
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

def get_html():
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
        'Referer':'http://data.gdcic.net/Dop/Open/PersonList.aspx'
    }
    data={
        '__VIEWSTATEGENERATOR': '70BB3DB9',
        '_EVENTTARGET': 'ctl00$ContentPlaceHolder1$AspNetPager1',
        '__EVENTARGUMENT':15
    }
    url="http://data.gdcic.net/Dop/Open/PersonList.aspx"
    strhtml = requests.post(url,headers=headers,data=data)
    return strhtml.text


def bs_parse_html(html):
    '''解析页面'''
    soup =BeautifulSoup(html,'lxml')
    table = soup.select('.data-list td')
    info_list=[]
    n=1
    for tr in table:
        if tr.a != None:
            name=tr.a.string
            info_list.append(name)
        else:
            infos=tr.string.strip()
            info_list.append(infos)

    info_lists=clip_list(a=info_list,c=4)
    df=pd.DataFrame(info_lists,columns=['姓名','身份证号码','性别','学历'])
    print(df)


def clip_list(a,c):  #a为原列表，c为等分长度
    clip_back=[]
    if len(a)>c:
        for i in range(int(len(a) / c)):
            # print(i)
            clip_a = a[c * i:c * (i + 1)]
            clip_back.append(clip_a)
            # print(clip_a)
        # last 剩下的单独为一组
        last = a[int(len(a) / c) * c:]
        if last:
            clip_back.append(last)
    else:  #如果切分长度不小于原列表长度，那么直接返回原列表
        clip_back = a
    return clip_back



def main():
    html=get_html()
    bs_parse_html(html)


if __name__ == '__main__':
    main()