#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
from helper import *
# @lc code=start


class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    ans = 0
    nums.sort()
    for i in range(len(nums)):
      if nums[i] == 0:
        continue
      k = i + 2
      for j in range(i + 1, len(nums)):
        k = bisect_left(nums, nums[i] + nums[j], k, len(nums))
        ans += k - j - 1
    return ans


# @lc code=end
'''
a + b > c
|a - b| < c

'''


assertEqual(Solution().triangleNumber([2, 2, 3, 4]), 3)
assertEqual(Solution().triangleNumber([1, 1, 3, 4]), 0)


class Solution:
  def triangleNumber_1(self, nums: List[int]) -> int:
    ans = 0
    nums.sort()

    for i in range(len(nums)):
      if nums[i] == 0:
        continue
      for j in range(i + 1, len(nums)):
        t = nums[i] + nums[j]

        l, h = j + 1, len(nums)
        while l < h:
          m = l + (h - l) // 2
          if nums[m] < t:
            l = m + 1
          else:
            h = m

        ans += l - j - 1

    return ans
