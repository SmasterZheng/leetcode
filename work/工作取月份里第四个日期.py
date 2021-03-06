"""
原版是取每个月第四个交易日，但现在由于交易日没有数据库，所以就截取列表里每个月的第四个日期
如：['20200104','20200105','20200107','20200109','20200110','20200112',
     '20200204','20200205','20200206','20200208','202002011']
输出：['20200109','20200208']
"""
class Solution:
    def listset(self, dates):
        '''
        :param dates: [[],[]]
        :return: [[]]
        '''
        list1=[]
        for i in dates:
            if i not in list1:
                list1.append(i)
        return list1

    def month4(self, dates):
        '''
        思路:按照月份进行分类，取第四个日期
        :param dates:
        :return:
        '''
        months,days,allmon,redata=[],[],[],[]
        for i in range(1,len(dates)):
            if dates[i-1][:6]==dates[i][:6]:
                days.append(dates[i-1])
                days.append(dates[i])
                # days=self.listset(days)
            else:
                days=[]
            months.append(days)
        for i in months: # 去重days里重复添加的日期
            allmon.append(self.listset(i))
        newallmon = self.listset(allmon) #[[],[]]得到按月份分类的日期

        for i in newallmon:
            if len(i)>=4:# 判断月份中存在第四个日期的
                redata.append(i[3])
        return redata



if __name__ == '__main__':
    Solution=Solution()
    dates=['20200104','20200105','20200109','20200107','20200110','20200112',
           '20200204','20200205','20200206','20200209','20200211',
           '20200304','20200305','20200306','20200208','20200211']
    print(Solution.month4(dates))