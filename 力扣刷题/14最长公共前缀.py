'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

'''



class Solution:
    def longestCommonPrefix(self, strs):
        # 判断最小的字符串，再拿最小的里面的部分依次对比其他两个
        if not strs:return ''
        s1 = min(strs)
        # print(s1)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
        # 以上是看了评论区的，自愧不如
        # 利用python的max()
        # 和min()，在Python里字符串是可以比较的，按照ascII值排，
        # 举例abb， aba，abac，最大为abb，最小为aba。所以只需要
        # 比较最大最小的公共前缀就是整个数组的公共前缀
        # 以下是自己写的暴力解法。。。。
        # m,n='',''
        # for i in range(len(strs)):
        #     if strs[i][0]!=strs[0][0]:
        #         # 不存在公共前缀
        #         return ''
        #     elif len(m) < len(strs[i]):
        #         m=strs[i]
        #     for j in range(len(m)):
        #         print(m,j)
        #         if m[j]==strs[i][j]:
        #             n+=m[j]
        #             continue
        #         return n

if __name__ == '__main__':
    Solution=Solution()
    result=Solution.longestCommonPrefix(["flower","flow","flight"])
    print(result)
