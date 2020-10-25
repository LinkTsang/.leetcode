from typing import *


class Solution:
  def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    ans = []
    for a, b in zip(l, r):
      subnums = nums[a:b + 1]
      subnums.sort()
      s = True
      diff = subnums[1] - subnums[0]
      for i in range(1, len(subnums) - 1):
        if subnums[i + 1] - subnums[i] != diff:
          s = False
          break
      ans.append(s)
    return ans


Solution().checkArithmeticSubarrays(
    [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10])


'''
Bilibili video
'''