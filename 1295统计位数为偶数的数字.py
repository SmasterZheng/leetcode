"""
给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。

示例 1：
输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数） 
345 是 3 位数字（位数为奇数）  
2 是 1 位数字（位数为奇数） 
6 是 1 位数字 位数为奇数） 
7896 是 4 位数字（位数为偶数）  
因此只有 12 和 7896 是位数为偶数的数字

示例 2：
输入：nums = [555,901,482,1771]
输出：1
解释：
只有 1771 是位数为偶数的数字。

提示：
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""
class Solution:
    def findNumbers(self, nums):
        '''
        思路：因为限制了数组中最大的数为100000，所以最大位数即6位 偶数位就仅有[2,4,6]
        :param nums:
        :return:
        '''
        num=0
        for i in nums:
            if len(str(i)) in [2,4,6]:
                num+=1
        return num
        # 下面为评论里的写法，利用map函数进行映射
        # return sum(map(lambda x: len(str(x)) & 1 ^ 1, nums))

if __name__ == '__main__':
    Solution=Solution()
    print(Solution.findNumbers([22,1,100000]))