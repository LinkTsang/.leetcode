#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> int:
    ans = 0

    def solve(root: TreeNode, sum: int):
      nonlocal ans

      if not root:
        return
      if root.val == sum:
        ans += 1

      solve(root.left, sum - root.val)
      solve(root.right, sum - root.val)

    def choose(root: TreeNode, sum: int):
      if not root:
        return

      solve(root, sum)
      choose(root.left, sum)
      choose(root.right, sum)

    choose(root, sum)
    return ans
# @lc code=end
