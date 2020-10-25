#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#
from typing import *
# @lc code=start
class Solution:
  def longestMountain(self, A: List[int]) -> int:
    state = 0
    ans = 0
    count = 0
    for i in range(len(A) - 1):
      if state == -1:
        if A[i] < A[i + 1]:
          count += 1
        elif A[i] > A[i + 1]:
          count += 1
          ans = max(ans, count)
          state = 1
        else:
          count = 0
          state = 0
      elif state == 1:
        if A[i] < A[i + 1]:
          count = 1
          state = -1
        elif A[i] > A[i + 1]:
          count += 1
          ans = max(ans, count)
        else:
          count = 0
          state = 0
      else:
        if A[i] < A[i + 1]:
          count += 1
          state = -1
    return ans + 1 if ans > 0 else 0


# @lc code=end
print(Solution().longestMountain([875,884,239,731,723,685]))  # 4