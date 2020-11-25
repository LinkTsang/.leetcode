#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
from helper import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    current = root

    def dfs(root):
      nonlocal current
      if not root:
        return root
      dfs(root.left)
      if root.left:
        current = current.left
      dfs(root.right)
      if root.right:
        current = current.left
    return dfs(root)
# @lc code=end
