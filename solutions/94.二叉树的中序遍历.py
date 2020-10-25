#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
      return []
    s = []
    ans = []
    while root or s:
      while root:
        s.append(root)
        root = root.left
      root = s.pop()
      ans.append(root.val)
      root = root.right

    return ans
# @lc code=end


'''
def dfs(root):
  if not root:
    return
  dfs(root.left)
  ans.append(root.val)
  dfs(root.right)
'''
