#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
# @lc code=start


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    ans = []
    current = []

    def dfs(i):
      if i > n:
        return

      if len(current) == k:
        ans.append(current[:])
        return

      current.append(i + 1)
      dfs(i + 1)
      current.pop()
      dfs(i + 1)

    dfs(0)
    return ans
# @lc code=end


Solution().combine(4, 2)
