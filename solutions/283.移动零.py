#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from helper import *
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums)):
          if nums[i] == 0:
            k = i
            break

        for i in range(k + 1, len(nums)):
          if nums[i] != 0 and k != -1:
              nums[i], nums[k] = nums[k], nums[i]
              k = k + 1 if nums[k+1] == 0 else -1

# @lc code=end
nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
assertEqual(nums, [1,3,12,0,0])

nums = [0]
Solution().moveZeroes(nums)
assertEqual(nums, [0])

nums = [1]
Solution().moveZeroes(nums)
assertEqual(nums, [1])

nums = [1,0,1]
Solution().moveZeroes(nums)
assertEqual(nums, [1,1,0])
'''
[x,x,x,0,0,0,z,z,z,...]

'''