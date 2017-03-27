"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1
        reverse = str(sign*x)[::-1]

        return sign*int(reverse)

if __name__ == '__main__':
    num = 123
    solution = Solution()
    print(solution.reverse(num))
    print(solution.reverse(-num))
