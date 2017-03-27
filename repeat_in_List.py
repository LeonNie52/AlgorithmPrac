# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        numbers.sort()
        for i in range(len(numbers)-1):
            if numbers[i]==numbers[i+1]:
                tmp=numbers[i]
                if tmp not in duplication:
                    duplication[0]=tmp
                    return True
        return False
                    