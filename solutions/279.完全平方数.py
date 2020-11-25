#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from helper import *
# @lc code=start


class Solution:
  def numSquares(self, n: int) -> int:
    if n <= 3:
      return n
    c = list(range(n + 1))
    max_a = ceil(sqrt(n))
    perfect_square = [a ** 2 for a in range(1, max_a + 1)]
    for i in range(4, n + 1):
      min_c = c[i]
      for s in perfect_square:
        if s > i:
          break
        min_c = min(min_c, c[i - s])
      c[i] = min_c + 1
    return c[n]
# @lc code=end
