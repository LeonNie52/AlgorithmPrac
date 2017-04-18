# Bubble Sort
def bubbleSort(data):
    if len(data) < 2:
        return data
    else:
        for i in range(len(data)):
            for j in range(0, len(data)-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

# Insert Sort


def insertSort(data):
    if len(data) < 2:
        return data
    for i in range(1, len(data)):
        key = data[i]
        for j in range(0, i)[::-1]:
            if data[j] > key:
                data[j+1] = data[j]
            else:
                break
        if j == 0 and data[0] > key:
            data[0] = key
        else:
            data[j+1] = key
    return data

# Quick Sort


def Partition(a, s, t):
    i, j = s, t
    tmp = a[s]
    while(i != j):
        while (j > i and data[j] >= tmp):
            j -= 1
        a[i] = a[j]
        while (i < j and data[i] <= tmp):
            i += 1
        a[j] = a[i]
    a[i] = tmp
    return i


def QuickSort(data, s, t):
    if (s < t):
        i = Partition(data, s, t)
        QuickSort(data, s, i - 1)
        QuickSort(data, i + 1, t)
    return data

# MergeSort
from math import floor


def merge(left, right):
    i, j = 0, 0
    tmp = []
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    tmp += left[i:]
    tmp += right[j:]
    return tmp


def mergeSort(lists):
    if len(lists) <= 1:
        return lists
    mid = int(floor(len(lists) / 2))
    left = mergeSort(lists[:mid])
    right = mergeSort(lists[mid:])
    return merge(left, right)

# Selection Sort


def selectSort(data):
    if len(data) < 2:
        return data
    else:
        for i in range(0, len(data)):
            minNum = min(data[i:])
            index = data.index(minNum)
            data[i], data[index] = minNum, data[i]
        return data
data = [2, 5, 4, 1, 3]
print bubbleSort(data)
print insertSort(data)
print QuickSort(data, 0, len(data)-1)
print mergeSort(data)
print selectSort(data)
