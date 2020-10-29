#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
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
  def sumNumbers(self, root: TreeNode) -> int:
    ans = 0

    def dfs(root, s):
      nonlocal ans
      if not root:
        return
      s = s * 10 + root.val
      if not root.left and not root.right:
        ans += s
        return
      dfs(root.left, s)
      dfs(root.right, s)

    dfs(root, 0)
    return ans
# @lc code=end
