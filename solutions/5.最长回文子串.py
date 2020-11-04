#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
from helper import *
# @lc code=start
class Solution:
  def longestPalindrome(self, s: str) -> str:
    dp = []
    n = len(s)
    m = 1
    for _ in range(n+1):
      dp.append([False] * n)
    for i in range(n):
      dp[1][i] = True
    for i in range(n - 1):
      if s[i] == s[i + 1]:
        dp[2][i] = True
        m = 2
    for k in range(3, n + 1):
      for i in range(n + 1 - k):
        if dp[k - 2][i + 1] and s[i] == s[i + k - 1]:
          dp[k][i] = True
          m = max(m, k)
    for i in range(n):
      if dp[m][i]:
        return s[i:i+m]
# @lc code=end
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("caba"))
print(Solution().longestPalindrome("aaaaa"))
print(Solution().longestPalindrome("aacabdkacaa"))


class Solution1:
  def longestPalindrome(self, s: str) -> str:
    dp = []
    n = len(s)
    m = 1
    for _ in range(n+1):
      dp.append([False] * n)
    for i in range(n):
      dp[1][i] = True
    for i in range(n - 1):
      if s[i] == s[i + 1]:
        dp[2][i] = True
        m = 2
    for k in range(3, n + 1):
      for i in range(n + 1 - k):
        if dp[k - 2][i + 1] and s[i] == s[i + k - 1]:
          dp[k][i] = True
          m = max(m, k)
    for i in range(n):
      if dp[m][i]:
        return s[i:i+m]
