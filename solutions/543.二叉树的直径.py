#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
from helper import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    ans = 0

    def solve(root):
      nonlocal ans

      if not root:
        return 0
      leftD = solve(root.left) + 1 if root.left else 0
      rightD = solve(root.right) + 1 if root.right else 0
      ans = max(ans, leftD + rightD)
      return max(leftD, rightD)

    solve(root)
    return ans
# @lc code=end
