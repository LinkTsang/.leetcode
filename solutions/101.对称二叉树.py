#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
from helper import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
  def isSymmetric(self, root: TreeNode) -> bool:
    def dfs(left: TreeNode, right: TreeNode):
      return not left and not right or left and right and left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

    return not root or dfs(root.left, root.right)
# @lc code=end
