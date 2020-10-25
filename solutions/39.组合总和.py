#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
# @lc code=start


class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    current = []

    def dfs(i, target):
      if i >= len(candidates):
        return
      if target == 0:
        ans.append(current[:])
        return

      next_target = target - candidates[i]
      if next_target >= 0:
        current.append(candidates[i])
        dfs(i, next_target)
        current.pop()
      dfs(i + 1, target)
    candidates.sort()
    dfs(0, target)
    return ans
# @lc code=end
