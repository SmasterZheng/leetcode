"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

汉明距离是以理查德·卫斯里·汉明的名字命名的。在信息论中，两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成另外一个字符串所需要替换的字符个数。例如：
1011101 与 1001001 之间的汉明距离是 2。
2143896 与 2233796 之间的汉明距离是 3。
"toned" 与 "roses" 之间的汉明距离是 3。
"""
class Solution:
    def hammingDistance(self, x, y):
        '''
        思路：先利用bin将整数转化成二进制数，对比两个二进制字符串里同位置相同数的数量，再用长度减去这个数量就是汉明距离数了
        :param x:
        :param y:
        :return:
        '''
        # x,y,humsnum=bin(x),bin(y),0
        # for i in range(len(x)):
        #     if x[i]!=y[i]:
        #         humsnum+=1
        # return humsnum
        # 评论看到的 ^是按位异或逻辑运算符，比如5^6，其实是101^110，结果是011，所以5^6的答案是3
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    Solution=Solution()
    result=Solution.hammingDistance(1,4)
    print(result)
