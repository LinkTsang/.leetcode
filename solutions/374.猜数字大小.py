#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
  def guessNumber(self, n: int) -> int:
    l, h = 1, n + 1
    while l < h:
      m = l + (h - l) // 2
      r = guess(m)
      if r < 0:
        h = m
      elif r > 0:
        l = m
      else:
        return m
    return l
# @lc code=end
