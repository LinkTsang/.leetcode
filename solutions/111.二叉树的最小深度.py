#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def minDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    elif not root.left and not root.right:
      return 1
    left_depth = self.minDepth(root.left) if root.left else 10 ** 9
    right_depth = self.minDepth(root.right) if root.right else 10 ** 9
    return min(left_depth, right_depth) + 1
# @lc code=end
