#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from helper import *
# @lc code=start


class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    d = {w: 0 for w in wordDict}
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
      for j in range(i - 1, -1, -1):
        if dp[j] and s[j:i] in d:
          dp[i] = True
          break
    return dp[-1]
# @lc code=end
