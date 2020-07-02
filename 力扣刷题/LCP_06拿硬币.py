"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：
输入：[4,2,1]
输出：4
解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2:
输入：[2,3,10]
输出：8

限制：
1 <= n <= 4
1 <= coins[i] <= 10
"""
import math
class Solution:
    def minCount(self, coins):
        '''
        思路：四种写法，本质是一样的，都是和2做除法，好理解点就是+1再整除2
        :param coins:
        :return:
        '''
        # num=0
        # for i in coins:
        #     num+=math.ceil(i/2)
        # return num

        return sum(math.ceil(i/2) for i in coins)

        # num=0
        # for i in coins:
        #     num+=(i+1)//2
        # return num
        #
        # return sum((c + 1) // 2 for c in coins)

if __name__ == '__main__':
    Solution=Solution()
    print(Solution.minCount([1,1,1,2]))