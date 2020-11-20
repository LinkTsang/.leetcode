#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from .helper import *

# @lc code=start


class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    count = 0
    c = None
    for n in nums:
      if count == 0:
        c = n
      count += 1 if n == c else -1
    return c
# @lc code=end
