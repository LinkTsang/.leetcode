#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
from helper import *
# @lc code=start


class Solution:
  def reverse(self, x: int) -> int:
    INT_MAX = (2 ** 31 - 1) // 10
    INT_MIN = ceil((-2 ** 31) / 10)
    ans = 0
    if x > 0:
      while x:
        a = x % 10
        x //= 10
        if ans > INT_MAX or (ans == INT_MAX and a > 7):
          return 0
        ans = ans * 10 + a
    elif x < 0:
      while x:
        a = x % 10
        if a != 0:
          a -= 10
        x = ceil(x / 10)
        if ans < INT_MIN or (ans == INT_MIN and a < -8):
          return 0
        ans = ans * 10 + a
    return ans


# @lc code=end
assertEqual(Solution().reverse(0), 0)
assertEqual(Solution().reverse(-1), -1)
assertEqual(Solution().reverse(1), 1)
assertEqual(Solution().reverse(123), 321)
assertEqual(Solution().reverse(-123), -321)
assertEqual(Solution().reverse(2**31 - 1), 0)
assertEqual(Solution().reverse(-10), -1)
assertEqual(Solution().reverse(-1563847412), 0)
