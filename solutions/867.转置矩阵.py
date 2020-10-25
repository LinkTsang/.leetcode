#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
from typing import *
# @lc code=start


class Solution:
  def transpose(self, A: List[List[int]]) -> List[List[int]]:
    m, n = len(A), len(A[0])
    B = []

    for i in range(n):
      row = []
      for j in range(m):
        row.append(A[j][i])
      B.append(row)
    return B
# @lc code=end


Solution().transpose([[1, 2, 3], [4, 5, 6]])
