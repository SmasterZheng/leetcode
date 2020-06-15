"""
原版是取每个月第四个交易日，但现在由于交易日没有数据库，所以就截取列表里每个月的第四个日期
如：['20200104','20200105','20200107','20200109','20200110','20200112',
     '20200204','20200205','20200206','20200208','202002011']
输出：['20200109','20200208']
"""
class Solution:
    def month4(self, dates):
        '''
        思路:按照月份进行分类，取第四个日期
        :param dates:
        :return:
        '''
        months=[]
        days = []
        for i in range(len(dates)):
            if dates[i][:6]==dates[i-1][:6]:
                days.append(dates[i-1])
            else:
                days=[]
            months.append(days)

        print(months)

if __name__ == '__main__':
    Solution=Solution()
    dates=['20200104','20200105','20200107','20200109','20200110','20200112',
     '20200204','20200205','20200206','20200208','202002011']
    Solution.month4(dates)