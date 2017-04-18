#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/6
# @Author  : Leon.Nie
# @Site    : 
# @File    : test.py

# import sys
# for line in sys.stdin:
#     a = line.split()
#     print int(a[0]) + int(a[1])

import sys


def comSum(values, n, target):
    if len(values) != n:
        return
    if not values:
        return []
    values.sort()
    result = []
    com(values, target, [], result)
    return result


def com(values, target, current, result):
    s = sum(current) if current else 0
    if s > target:
        return
    elif s == target:
        result.append(current)
        return
    else:
        for i, v in enumerate(values):
            com(values[i:], target, current + [v], result)


if __name__ == "__main__":
    # 读取第一行的n
    target = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip()
    values = map(int, line.split())

    result = comSum(values, n, target)
    for i in range(len(result)):
        for j in range(len(result[i])):
            print result[i][j],
        print
