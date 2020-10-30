#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#
from helper import *
# @lc code=start


class Solution:
  def canWinNim(self, n: int) -> bool:
    # return n % 4 != 0
    return (n & 3) != 0

# @lc code=end
assertEqual(Solution().canWinNim(1), True)
assertEqual(Solution().canWinNim(2), True)
assertEqual(Solution().canWinNim(3), True)
assertEqual(Solution().canWinNim(4), False)
assertEqual(Solution().canWinNim(5), True)
assertEqual(Solution().canWinNim(6), True)
assertEqual(Solution().canWinNim(7), True)
assertEqual(Solution().canWinNim(8), False)
assertEqual(Solution().canWinNim(9), True)
assertEqual(Solution().canWinNim(10), True)
assertEqual(Solution().canWinNim(11), True)

