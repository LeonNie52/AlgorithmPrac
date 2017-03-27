"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(nums, target):
        if len(nums) <= 1:
            return "Need more than two elements in Array"
        else:
            myDict = {}
            for i in range(len(nums)):
                if nums[i] in myDict.keys():
                    return [myDict[nums[i]], i]
                else:
                    myDict[target-nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))
