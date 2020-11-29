#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
from helper import *
# @lc code=start


class Solution:
  def largestPerimeter(self, A: List[int]) -> int:
    n = len(A)
    A.sort()
    for i in reversed(range(2, n)):
      if A[i - 2] + A[i - 1] > A[i]:
        return A[i - 2] + A[i - 1] + A[i]
    return 0
# @lc code=end
