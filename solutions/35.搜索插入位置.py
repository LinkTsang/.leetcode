#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import *
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      l, h = 0, len(nums)
      while l < h:
        m = l + (h - l) // 2
        if nums[m] < target:
          l = m + 1
        elif nums[m] > target:
          h = m
        else: 
          return m
      return l
# @lc code=end

