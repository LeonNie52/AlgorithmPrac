# -*- coding:utf-8 -*-

"""
有 n 个字符串，每个字符串都是由 A-J 的大写字符构成。
现在你将每个字符映射为一个 0-9 的数字，不同字符映射为不同的数字。
这样每个字符串就可以看做一个整数，唯一的要求是这些整数必须是正整数且它们的字符串不能有前导零。
现在问你怎样映射字符才能使得这些字符串表示的整数之和最大？

输入描述:
每组测试用例仅包含一组数据，每组数据第一行为一个正整数 n ， 接下来有 n 行，每行一个长度不超过 12 且仅包含大写字母 A-J 的字符串。 
n 不大于 50，且至少存在一个字符不是任何字符串的首字母。

输出描述:
输出一个数，表示最大和是多少。

输入例子:
2
ABC
BCA

输出例子:
1875
"""

from collections import defaultdict


class Solution(object):

    def maxMapSum(self, input):
        weightDict = defaultdict(int)
        n = input[0]
        for i in range(1, n+1):
            for j in range(len(input[i])):
                weight = len(input[i]) - input[i].index(input[i][j])-1
                weightDict[input[i][j]] = 10**weight+weightDict[input[i][j]]
        weight = weightDict.values()
        weight.sort(reverse=True)
        Max = 9
        Sum = 0

        for i in range(len(weight)):
            Sum = Sum+Max*weight[i]
            Max = Max-1
        return Sum

if __name__ == '__main__':
    s = Solution()
    input = [2,'ABC','BCA']

    print(s.maxMapSum(input))
