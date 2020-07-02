"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        '''
        思路：以0拆分，然后对比各个含1列表的长度，取出最大
        :param nums:
        :return:
        '''

        leg=[0]
        for i in range(len(nums)):
            if nums[i]==0:
                leg.append(i)
        leg.append(len(nums))
        a = leg[0] # 防止第一个数不是0，就先加上0
        print(leg) # 取出所有0的位置所在数[0, 0, 3, 7, 9]和整个nums的长度
        num=[]
        for i in range(len(leg)):
            if i>=1:
                s=leg[i]-leg[i-1] # 对比0所在位数[0, 0, 3, 7, 9]，利用冒泡排序，两两相减，得到的数减一即可
                if a>s:
                    num.append(a)
                a=s
        return num[0]-1


if __name__ == '__main__':
    Solution=Solution()
    print(Solution.findMaxConsecutiveOnes([0,1,1,0,1,1,1,0,1]))