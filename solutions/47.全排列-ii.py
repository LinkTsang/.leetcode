#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def bt(i, n):
      if i >= n:
        ans.append(perm[:])
        return
      for j in range(0, len(nums)):
        if visited[j] or (j > 0 and nums[j] == nums[j-1] and not visited[j-1]):
          continue
        perm.append(nums[j])
        visited[j] = True
        bt(i + 1, n)
        visited[j] = False
        perm.pop()

    ans = []
    nums.sort()
    visited = [False] * len(nums)
    perm = []
    bt(0, len(nums))
    return ans
# @lc code=end
