#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#
from helper import *
# @lc code=start


class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    m = defaultdict(lambda: -1)
    s = []
    for n in nums2:
      while s and s[-1] < n:
        m[s.pop()] = n
      s.append(n)
    return [m[n] for n in nums1]
# @lc code=end
