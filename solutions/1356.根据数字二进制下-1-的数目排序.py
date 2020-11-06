#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#
from typing import *
# @lc code=start


class Solution:
  def sortByBits(self, arr: List[int]) -> List[int]:
    def count(x):
      r = 0
      while x:
        x &= x - 1
        r += 1
      return r

    return sorted(arr, key=lambda x: (count(x), x))
# @lc code=end
