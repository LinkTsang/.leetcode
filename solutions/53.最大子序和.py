#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import *


class Solution1:
  def maxSubArray(self, nums: List[int]) -> int:
    dp = [0] * len(nums)
    ans = dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
      ans = max(dp[i], ans)
    return ans


assert Solution1().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
# @lc code=start


class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    dp = [0] * len(nums)
    ans = dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
      ans = max(dp[i], ans)
    return ans
# @lc code=end
