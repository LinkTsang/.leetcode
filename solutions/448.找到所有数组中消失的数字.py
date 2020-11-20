#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
from helper import *
# @lc code=start


class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    ans = list(range(1, len(nums) + 1))
    for n in nums:
      ans[n - 1] = 0
    return list(filter(lambda n: n != 0, ans))

# @lc code=end
