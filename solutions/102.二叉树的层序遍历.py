#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []
    q = deque([root, None])
    ans = []
    while q:
      current = []
      while q:
        top = q.popleft()
        if top:
          current.append(top.val)
          if top.left:
            q.append(top.left)
          if top.right:
            q.append(top.right)
        elif q:
          q.append(None)
          break
      ans.append(current)
    return ans

# @lc code=end
