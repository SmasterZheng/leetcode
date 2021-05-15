# -*- coding: utf-8 -*-
# @Time    : 20210515
# @Author  : zhengxz
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from work.耗时装饰器 import spend_time
import re

info={}
info['columns']=['公司名称', '电话']

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

    url="http://www.szbda.cn/index.php?m=company&c=index&a=gz_list&page={}".format(page)
    strhtml = requests.post(url,headers=headers)
    # print(strhtml.text)
    return strhtml.text


def add_parse_html(html):
    '''解析地址页面'''

    soup =BeautifulSoup(html,'lxml')
    company_infos = soup.select('.comp_list_ul li div')  # 每个公司的信息
    # print(company_infos)
    companys=[]
    for i in company_infos:
        # print(str(i.a)[110:-4],str(i.p)[158:171])
        # print(i.p)
        company_name = str(i.a)[110:-4]
        phone=re.search(r'.*电话：(.*?)</i>',str(i.p)).group(1)
        companys.append((company_name,phone))
    companys=pd.DataFrame(companys,columns=info['columns'])
    return companys




@spend_time
def main():
    df=pd.DataFrame(None,columns=info['columns'])
    for i in range(1,21):
        #共计20页
        html=get_html(page=i)
        print('正在爬取第',i,'页...')
        df1=add_parse_html(html)
        df=df.append(df1) #把每页数据汇总
    print('爬取完成！')
    df.reset_index(drop=True,inplace=True) #重建行索引
    print(df)
    df.to_excel('深圳市装饰行业协会公司及电话.xlsx',encoding='utf-8')


if __name__ == '__main__':
    main()