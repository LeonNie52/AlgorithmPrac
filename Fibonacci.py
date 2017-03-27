# -*- coding:utf-8 -*-
"""
大家都知道斐波那契数列，
现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        i,j = 0,1
        if n == 0:
            return 0
        if n==1:
            return 1
        for x in range(1, n):
            i,j = j,i+j
        return j