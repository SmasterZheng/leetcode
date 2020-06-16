"""
输入一个日期，判断它和月中的一个日期，然后大于等于的话则返回月末，小于则正常输出
如：月中的日期为'20200516'
输入:'20200512'
输出:'20200512'

输入:'20200518'
输出:'20200531'
"""
import datetime
import calendar

class Solution:
    def get_the_last_month_day(self, date,ndate):
        '''

        :param date: 输入日期
        :param ndate: 指定月中的日期
        :return: 月末
        '''
        start = datetime.datetime.strptime(date, '%Y%m%d')
        end = datetime.datetime.strptime(ndate, '%Y%m%d')
        next_month = start + datetime.timedelta(days=calendar.monthrange(start.year, start.month)[1])
        month_end = next_month - datetime.timedelta(days=1)
        print(datetime.datetime.strftime(start, '%Y%m%d'))


if __name__ == '__main__':
    Solution=Solution()
    Solution.get_the_last_month_day('20200518','20200516')
