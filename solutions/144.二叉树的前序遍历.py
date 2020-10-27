#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
from .helper import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
      return []
    ans = []

    stack = []
    p = root
    while stack or p:
      while p:
        ans.append(p.val)
        stack.append(p)
        p = p.left
      p = stack.pop()
      p = p.right

    return ans

# @lc code=end
