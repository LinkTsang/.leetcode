#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    ans = []
    current = []

    def solve(root: TreeNode, sum: int):
      if not root:
        return
      if not root.left and not root.right and root.val == sum:
        current.append(root.val)
        ans.append(current[:])
        current.pop()
      current.append(root.val)
      solve(root.left, sum - root.val)
      solve(root.right, sum - root.val)
      current.pop()
    solve(root, sum)
    return ans
# @lc code=end
