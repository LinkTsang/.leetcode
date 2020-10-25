#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import *
# @lc code=start


class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    c = 0
    digits[-1] += 1
    c = digits[-1] // 10
    digits[-1] %= 10
    i = len(digits) - 2
    while i >= 0 and c != 0:
      digits[i] += c
      c = digits[i] // 10
      digits[i] %= 10
      i -= 1
    if c == 1:
      digits = [1] + digits
    return digits
# @lc code=end


print(Solution().plusOne([9]))  # [1,0]
print(Solution().plusOne([9, 9]))  # [1,0,0]
