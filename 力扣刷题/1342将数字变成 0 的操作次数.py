"""
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

示例 1：
输入：num = 14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。

示例 2：
输入：num = 8
输出：4
解释：
步骤 1） 8 是偶数，除以 2 得到 4 。
步骤 2） 4 是偶数，除以 2 得到 2 。
步骤 3） 2 是偶数，除以 2 得到 1 。
步骤 4） 1 是奇数，减 1 得到 0 。

"""

def numberOfSteps (num: int) -> int:
    '''
    思路：判断奇偶即可
    :param num:
    :return:
    '''
    # s=0
    # while num!=0:
    #     if num%2==0:
    #         num=num/2
    #         s+=1
    #     else:
    #         num=num-1
    #         s+=1
    # return s
    # 经典看评论
    #大佬回复：en(binary)是计算除2的次数，但需要实际的二进制长度减1，len(binary)是看二进制的长度，
    #         有符号两位所以最后减3 count 1 是看减一次数
    binary = bin(num)
    return len(binary) + binary.count('1') - 3

if __name__ == '__main__':
    s=numberOfSteps(10)
    print(s)