#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    s = 0
    def dfs(root):
      nonlocal s
      if not root:
        return
      dfs(root.right)
      root.val += s
      s = root.val
      dfs(root.left)
    dfs(root)
    return root
# @lc code=end
'''
s = 0
def dfs(root):
  if not root:
    return
  dfs(root.right)
  root.val += s
  s = root.val
  print(root.val)
  dfs(root.left)
'''