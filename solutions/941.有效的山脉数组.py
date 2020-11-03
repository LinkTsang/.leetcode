#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#
from typing import *
# @lc code=start


class Solution:
  def validMountainArray(self, A: List[int]) -> bool:
    N, i = len(A), 0
    while i + 1 < N and A[i] < A[i + 1]:
      i += 1
    if i == 0 or i == N - 1:
      return False
    while i + 1 < N and A[i] > A[i + 1]:
      i += 1
    return i == N - 1
# @lc code=end
