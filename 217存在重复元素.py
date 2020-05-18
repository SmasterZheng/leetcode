"""
217 简单
给定一个整数数组，判断是否存在重复元素。
如果任意- -值在数组中出现至少两次，函数返回true。如果数组中每个元素都不相同，则返回false。

示例1:
输入: [1,2,3,1]输出: true

示例2:
输入: [1,2,3,4]输出: false

示例3:
输入: [1,1,1,3,3,4,3,2,4,2]输出: true
"""

def cf(listdata):
    return False if len(set(listdata))==len(listdata) else True

if __name__ == '__main__':
    a=cf([1,2,2,4])
    print(a)