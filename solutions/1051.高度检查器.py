#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#
from typing import *
# @lc code=start


class Solution:
  def heightChecker(self, heights: List[int]) -> int:
    if len(heights) <= 1:
      return 0
    bucket = [0] * 101
    for h in heights:
      bucket[h] += 1
    sorted_heights = []
    for i, c in enumerate(bucket):
      if c > 0:
        sorted_heights += [i] * c
    ans = 0
    for x, y in zip(heights, sorted_heights):
      if x != y:
        ans += 1
    return ans


# @lc code=end
print(Solution().heightChecker([5, 1, 2, 3, 4]))  # 5
print(Solution().heightChecker([1, 1, 4, 2, 1, 3]))  # 3
# [1, 1, 4, 2, 1, 3]
# [1, 1, 1, 2, 3, 4]