#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    if not root:
      return True

    prev = float('-inf')

    def dfs(root):
      nonlocal prev

      if not root:
        return True
      if not dfs(root.left):
        return False
      if root.val <= prev:
        return False
      prev = root.val
      if not dfs(root.right):
        return False
      return True

    return dfs(root)
# @lc code=end
