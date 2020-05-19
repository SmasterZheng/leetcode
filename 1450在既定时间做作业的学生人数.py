"""
给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。
已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。
请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。

 
示例 1：

输入：startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
输出：1
解释：一共有 3 名学生。
第一名学生在时间 1 开始写作业，并于时间 3 完成作业，在时间 4 没有处于做作业的状态。
第二名学生在时间 2 开始写作业，并于时间 2 完成作业，在时间 4 没有处于做作业的状态。
第三名学生在时间 3 开始写作业，预计于时间 7 完成作业，这是是唯一一名在时间 4 时正在做作业的学生。

输入：startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
输出：5

"""
class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        """
        思路：
        判断两个列表里在同一位置处于queryTime的个数，先遍历两个列表的同一位置数，再比较

        """
        num=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                num+=1
        return num


if __name__ == '__main__':
    result=Solution() # 类的实例化
    results=result.busyStudent([9,8,7,6,5,4,3,2,1],[10,10,10,10,10,10,10,10,10],5)
    print(results)
