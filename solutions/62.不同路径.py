#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      dp = [1] * n
      for _ in range(1, m):
        for i in range(1, n):
          dp[i] += dp[i - 1]
      return dp[-1]
# @lc code=end

