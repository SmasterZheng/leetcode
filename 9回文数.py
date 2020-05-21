"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

不能整数转为字符串!!!
"""


def isPalindrome(x: int):
    '''
    思路：根据题目可得，负数都为False，所以只要正整数和0即可
    :param x:
    :return:
    '''
    if (x < 0 or (x % 10 == 0 & x != 0)):
        return False
    s=0
    while x>s:
        s=s*10+x%10
        x/=10
    return x==s or x==s/10

if __name__ == '__main__':
    a=isPalindrome(111)
    print(a)
# 判断水仙花数
# num = int(input('请输入一个三位数'))
# ge_num = num % 10
# bai_num = num // 100
# shi_num = (num - bai_num * 100 - ge_num) // 10
# if ge_num ** 3 + shi_num ** 3 + bai_num ** 3 == num:
#     print('%d是水仙花数' % num)
# else:
#     print('%d不是水仙花数' % num)