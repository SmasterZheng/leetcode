"""
给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

 

示例 1：

输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
示例 2：

输入：head = [0]
输出：0
示例 3：

输入：head = [1]
输出：1
示例 4：

输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
输出：18880
示例 5：

输入：head = [0,0]
输出：0
 

提示：

链表不为空。
链表的结点总数不超过 30。
每个结点的值不是 0 就是 1。

"""
class Solution:
    def getDecimalValue(self, head):
        '''
        思路：把列表的数都提出来形成一个整数
        :param head:
        :return:
        '''
        new = [str(i) for i in head]
        fie = ''.join(new)  # 得到二进制
        return int(fie,2) # 转化为十进制

    # 此题需要改进，因为传进来的其实是个链表


if __name__ == '__main__':
    Solution=Solution()
    print(Solution.getDecimalValue([0,0,0,0,0,0]))