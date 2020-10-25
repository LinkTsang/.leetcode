#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def deepestLeavesSum(self, root: TreeNode) -> int:
    if not root:
      return 0
    q = deque([root])
    ans = 0
    while q:
      size = len(q)
      ans = 0
      for _ in range(size):
        node = q.popleft()
        ans += node.val
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
    return ans
# @lc code=end
