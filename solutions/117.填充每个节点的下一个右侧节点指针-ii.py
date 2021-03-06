#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if not root:
      return root
    q = deque([root, None])
    while q:
      while q:
        top = q.popleft()
        if top:
          top.next = q[0]
          if top.left:
            q.append(top.left)
          if top.right:
            q.append(top.right)
        elif q:
          q.append(None)
          break
    return root
# @lc code=end
