#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x == 0:
      return True
    if x < 0 or x % 10 == 0:
      return False
    r = 0
    while r < x:
      r *= 10
      r += x % 10
      x //= 10
    return r == x or r // 10 == x
# @lc code=end
