"""
都是列表元素的列表去重
如输入
[['20200105', '20200107'], ['20200105', '20200107'],['20200205', '20200206'], ['20200205', '20200206']]
输出：
[['20200105', '20200107'],['20200205', '20200206']]
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

if __name__ == '__main__':
    Solution=Solution()
    list1=[['20200105', '20200107'], ['20200105', '20200107'],['20200205', '20200206'], ['20200205', '20200206']]
    print(Solution.listset(list1))
