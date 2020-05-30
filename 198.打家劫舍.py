"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""
class Solution:
    def rob(self, nums):
        '''
        思路：对比奇数偶数位置的和，返回更大的
        :param nums:
        :return:
        '''
        ret = [0 for i in range(len(nums) + 2)]

        for i in range(len(nums)):
            ret[i + 2] = max(nums[i], ret[i + 1], nums[i] + ret[i])
        return ret[-1]
        # 以下为自己的写法，一开始只单纯的考虑取奇数位置的了，多加了三个if都没取对，唉~
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 2:
        #     return max(nums)
        # if len(nums) == 3 and nums[0] + nums[2] < nums[1]:
        #     return nums[1]
        # num, i = nums[0], 0
        # while i + 2 <= len(nums) - 1:
        #     num = num + nums[i + 2]
        #     i += 2
        # return num

if __name__ == '__main__':
    Solution = Solution()
    # 位数0,2,4,6
    # 长度1,3,5,7
    print(Solution.rob([1,2]))