#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from helper import *

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      if len(nums) <= 2:
        return max(nums)
      dp = [nums[0], max(nums[:2])] + [0] * (len(nums) - 2)
      for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
      return dp[-1]
      
# @lc code=end
assertEqual(Solution().rob([]), 0)
assertEqual(Solution().rob([3]), 3)
assertEqual(Solution().rob([3, 6]), 6)
assertEqual(Solution().rob([6, 3]), 6)

assertEqual(Solution().rob([1,2,3,1]), 4)
# dp = [1, 2, 4, 4]
assertEqual(Solution().rob([2,7,9,3,1]), 12)
# dp = [2, 7, 11, 11, 12]
assertEqual(Solution().rob([2,7,9,3,1]), 12)
