#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    def build(nums, low, high):
      if low >= high:
        return None
      max_value = nums[low]
      index = low
      for i in range(low + 1, high):
        if nums[i] > max_value:
          max_value = nums[i]
          index = i
      root = TreeNode(nums[index])
      root.left = build(nums, low, index)
      root.right = build(nums, index + 1, high)
      return root
    return build(nums, 0, len(nums))
# @lc code=end
