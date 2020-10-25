#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    def bt(i, n):
      if i == n:
        ans.append(nums[:])
      for j in range(i, n):
        nums[i], nums[j] = nums[j], nums[i]
        bt(i + 1, len(nums))
        nums[i], nums[j] = nums[j], nums[i]
    ans = []
    bt(0, len(nums))
    return ans
# @lc code=end
