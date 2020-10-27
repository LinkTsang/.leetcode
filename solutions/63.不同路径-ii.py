#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from helper import *
# @lc code=start


class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
    for i in range(1, n):
      dp[i] = dp[i - 1] if obstacleGrid[0][i] == 0 else 0

    for i in range(1, m):
      if obstacleGrid[i][0] == 1:
        dp[0] = 0
      for j in range(1, n):
        if obstacleGrid[i][j] == 1:
          dp[j] = 0
        else:
          up = dp[j] if obstacleGrid[i - 1][j] == 0 else 0
          left = dp[j - 1] if obstacleGrid[i][j - 1] == 0 else 0
          dp[j] = up + left
    return dp[-1]


# @lc code=end
assertEqual(Solution().uniquePathsWithObstacles([[1, 0]]), 0)
assertEqual(Solution().uniquePathsWithObstacles([[0]]), 1)
assertEqual(Solution().uniquePathsWithObstacles(
    [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]), 2)
assertEqual(Solution().uniquePathsWithObstacles([[0], [1]]), 0)
