#
# @lc app=leetcode.cn id=514 lang=python3
#
# [514] 自由之路
#
from helper import *
# @lc code=start


class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    n = len(ring)
    m = len(key)
    pos = defaultdict(lambda: [])
    for i, k in enumerate(ring):
      pos[k].append(i)

    dp = []
    for _ in range(m):
      dp.append([9999] * n)

    for i in pos[key[0]]:
      dp[0][i] = min(i, n - i) + 1

    for i in range(1, m):
      for j in pos[key[i]]:
        for k in pos[key[i - 1]]:
          t = dp[i - 1][k] + min(abs(j - k), n - abs(j - k)) + 1
          dp[i][j] = min(dp[i][j], t)

    return min(dp[m - 1])
# @lc code=end
