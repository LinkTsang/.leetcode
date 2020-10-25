#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start


class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    current = []

    def dfs(i):
      if i >= n:
        ans.append(current[:])
        return

      current.append(nums[i])
      dfs(i + 1)
      current.pop()
      dfs(i + 1)

    dfs(0)
    return ans
# @lc code=end


Solution().subsets([1, 2, 3])
