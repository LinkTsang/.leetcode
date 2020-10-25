#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import *
# @lc code=start


class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans = []
    for i in range(len(nums)):
      target = -nums[i]
      m = set()
      for j in range(i + 1, len(nums)):
        x = target - nums[j]
        if x in m:
          ans.append([nums[i], x, nums[j]])
        else:
          m.add(nums[j])
    return ans
# @lc code=end
