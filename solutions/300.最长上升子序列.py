#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
from helper import *
# @lc code=start


class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    dp = [1] + [0] * (len(nums) - 1)
    for i in range(1, len(nums)):
      last = -1
      for j in range(i):
        if nums[j] < nums[i]:
          if last == -1:
            last = j
          elif dp[j] > dp[last]:
            last = j
          # elif dp[j] == dp[last] and nums[j] < nums[last]:
          #   last = j
      dp[i] = dp[last] + 1 if last != -1 else 1
    # print(dp)
    return max(dp)


# @lc code=end
assertEqual(Solution().lengthOfLIS([]), 0)
assertEqual(Solution().lengthOfLIS([1]), 1)
assertEqual(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
