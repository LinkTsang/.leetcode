#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from helper import *
# @lc code=start


class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
      return
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
      i -= 1
    j = len(nums) - 1
    if i >= 0:
      while j >= 0 and nums[i] >= nums[j]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    i += 1
    j = len(nums) - 1
    while i < j:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
      j -= 1


# @lc code=end

# @lc test=start
[1, 2, 3]
[3, 2, 1]
# @lc test=end
