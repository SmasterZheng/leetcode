"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

"""
class Solution:
    def majorityElement(self, nums):
        '''
        从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个
        :param nums:
        :return:
        '''
        # 本题在提交的时候显示超时了，因为系统传了个超级超级长的nums
        for i in range(len(nums)):
            if nums.count(nums[i])>(len(nums)/2):
                return nums[i]

if __name__ == '__main__':
    Solution=Solution()
    print(Solution.majorityElement([1, 1, 1, 2, 2, 2, 2]))