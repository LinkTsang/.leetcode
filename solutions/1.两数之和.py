#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from helper import *
# @lc code=start


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    m = {}
    for i, num in enumerate(nums):
      if target - num in m:
        return [m[target - num], i]
      m[nums[i]] = i
    return []

# @lc code=end


# @lc test=start
[2, 7, 11, 15]
9
[1, 1]
2
# @lc test=end
