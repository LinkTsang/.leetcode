#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import List
# @lc code=start


class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    current = []

    def dfs(i, target):
      if target == 0:
        ans.append(current[:])
        return
      if i >= len(candidates):
        return

      next_target = target - candidates[i]
      if next_target >= 0:
        current.append(candidates[i])
        dfs(i + 1, next_target)
        current.pop()
      j = i + 1
      while j < len(candidates) and candidates[i] == candidates[j]:
        j += 1
      dfs(j, target)
    candidates.sort()
    dfs(0, target)
    return ans
# @lc code=end


Solution().combinationSum2([2,5,2,1,2], 5)