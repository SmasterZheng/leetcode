# -*- coding: utf-8 -*-
# @Time    : 20201229
# @Author  : zhengxz
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd

from work.耗时装饰器 import spend_time

info={}
info['columns']=['邮编', '地址', '机构名称', '联系人', '证书号', '资质认定部门', '证书状态', '有效截止日期']

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

    data={
        'pageNo': page
    }
    url="http://cma.cnca.cn/cma/infoQuery/tBzQualificationQuery/tBzQualificationQueryList"
    strhtml = requests.post(url,headers=headers,data=data,verify=False)
    return strhtml.text

# def paging():
#     '''将页面page传递给requests进行翻页处理'''
#     for i in range(113):
#
#         get_html(page=i)


def add_parse_html(html):
    '''解析机构地址页面'''

    soup =BeautifulSoup(html,'lxml')
    address = soup.select('#contentTable div input')  # 机构地址及邮编
    table = soup.select('#contentTable tr td') # 其他信息
    addlist=[]
    for add in address:
        # print(add["value"]) # 机构地址及邮编
        addlist.append(add["value"])
    info_list = []
    for i in table:
        if i.string != None:
            info_list.append(i.string.strip())
    addlist=clip_list(a=addlist,c=2) # 把机构地址和邮编切片出来
    info_list = clip_list(a=info_list,c=6) # 把其他信息切片出来
    all_info=[]
    for i in range(len(addlist)):
        all_info.append(addlist[i]+info_list[i])
        # ['310101', '局门路427号201-301', '上海生物材料研究测试中心', '黄晢玮', '180015143968', '国家认证认可监督管理委员会', '有效', '2024-06-21']
    df = pd.DataFrame(all_info, columns=info['columns'])
    return df



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


@spend_time
def main():
    df=pd.DataFrame(None,columns=info['columns'])
    for i in range(1,113):
        #共计112页
        html=get_html(page=i)
        print('正在爬取第',i,'页...')
        df1=add_parse_html(html)
        df=df.append(df1) #把每页数据汇总
    print('爬取完成！')
    df.reset_index(drop=True,inplace=True) #重建行索引
    # print(df)
    # df.to_excel('资质认证企业信息.xlsx',encoding='utf-8')


if __name__ == '__main__':
    main()