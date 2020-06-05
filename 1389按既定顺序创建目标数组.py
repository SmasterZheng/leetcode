"""
给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组：

目标数组 target 最初为空。
按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。
重复上一步，直到在 nums 和 index 中都没有要读取的元素。
请你返回目标数组。

题目保证数字插入位置总是存在。

示例 1：

输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
输出：[0,4,1,3,2]
解释：
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
示例 2：

输入：nums = [1,2,3,4,0], index = [0,1,2,3,0]
输出：[0,1,2,3,4]
解释：
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

解释：index列表的数，对应是输出列表target插入位置的下标，然后数就从nums里对应的index位置的数取出来

"""
class Solution:
    def createTargetArray(self, nums, index):
        '''
        思路：python插入指定位置，利用insert()
        :param nums:
        :param index:
        :return:
        '''
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

if __name__ == '__main__':
    Solution=Solution()
    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]
    result = Solution.createTargetArray(nums,index)
    print(result)