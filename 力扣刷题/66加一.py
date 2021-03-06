"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

示例 3:
输入: [9],[9,9]
输出: [1,0],[1,0,0]
解释: 输入数组表示数字 4321。
"""
class Solution:
    def plusOne(self, digits) :
        '''
        思路：''.join(map(str,digits)) 利用map，将单个整型拼接转成字符串，然后利用eval再转成合成的整型
        再利用map(int,str),再转成字符型
        :param digits:
        :return:
        '''
        return list(map(int,str(int(''.join(map(str,digits)))+1)))

if __name__ == '__main__':
    Solution=Solution()
    print(Solution.plusOne([9,9]))
