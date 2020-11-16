#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    s = []
    for n in num:
      while s and k and s[-1] > n:
        s.pop()
        k -= 1
      s.append(n)
    if k > 0:
      s = s[:-k]
    return "".join(s).lstrip('0') or "0"

# @lc code=end
