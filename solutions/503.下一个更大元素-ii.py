#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#
from helper import *
# @lc code=start


class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    ans = [-1] * len(nums)
    s = []
    for i, n in enumerate(nums):
      while s and s[-1][1] < n:
        ans[s.pop()[0]] = n
      s.append((i, n))
    for n in nums:
      while s and s[-1][1] < n:
        j = s.pop()[0]
        if j >= 0:
          ans[j] = n
      s.append((-1, n))
    return ans
# @lc code=end
