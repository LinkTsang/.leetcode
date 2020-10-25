#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def solve(left, right):
      if left > right:
        return None

      v = postorder.pop()
      root = TreeNode(v)
      index = m[v]
      root.right = solve(index + 1, right)
      root.left = solve(left, index - 1)
      return root

    m = {v: i for i, v in enumerate(inorder)}
    return solve(0, len(inorder) - 1)

# @lc code=end
