#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return None
    p1, p2 = head, head
    while True:
      if not p2 or not p2.next:
        return None

      p1 = p1.next
      p2 = p2.next.next

      if p1 == p2:
        while head != p1:
          head, p1 = head.next, p1.next
        return head

# @lc code=end
