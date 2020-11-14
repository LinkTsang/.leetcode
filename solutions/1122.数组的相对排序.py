#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
from helper import *
# @lc code=start


class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    c = Counter(arr1)
    ans = []
    for a in arr2:
      ans += [a] * c[a]
      del c[a]
    for a in sorted(c.keys()):
      ans += [a] * c[a]
    return ans
# @lc code=end
