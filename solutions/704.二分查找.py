#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import *
# @lc code=start


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l, h = 0, len(nums)
    while l < h:
      m = l + (h - l) // 2
      if nums[m] < target:
        l = m + 1
      elif target < nums[m]:
        h = m
      else:
        return m
    return -1
# @lc code=end
