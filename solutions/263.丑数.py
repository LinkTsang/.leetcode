#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#
from helper import *
# @lc code=start
class Solution:
    def isUgly(self, num: int) -> bool:
      if num <= 0:
        return False
      while num != 1:
        if num % 2 == 0:
          num //= 2
        elif num % 3 == 0:
          num //=3
        elif num % 5 == 0:
          num //= 5
        else:
          break
      return num == 1
# @lc code=end

assertEqual(Solution().isUgly(0), False)
assertEqual(Solution().isUgly(1), True)
assertEqual(Solution().isUgly(14), False)
assertEqual(Solution().isUgly(-6), False)
assertEqual(Solution().isUgly(-1000), False)
assertEqual(Solution().isUgly(-2147483648), False)
