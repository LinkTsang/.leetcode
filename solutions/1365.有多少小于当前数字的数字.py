#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#
from typing import *
from collections import *
# @lc code=start


class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    counter = Counter(nums)
    v = sorted(counter.items(), key=lambda x: x[0])
    a = [0] * len(nums)
    for i in range(1, len(v)):
      a[i] = a[i - 1] + v[i - 1][1]
    m = {x[0]: a[i] for i, x in enumerate(v)}
    return [m[n] for n in nums]
# @lc code=end

Solution().smallerNumbersThanCurrent([7,7,7,7])