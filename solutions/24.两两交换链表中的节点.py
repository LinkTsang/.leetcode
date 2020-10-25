#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def swapPairs(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return head
    node1, node2 = head, head.next
    head = node2
    last_tail = ListNode(next=head)
    next_head = None
    while node1 and node2:
      next_head = node2.next

      last_tail.next = node2
      node1.next = next_head
      node2.next = node1
      last_tail = node1

      if not next_head or not next_head.next:
        return head

      node1, node2 = next_head, next_head.next
    return head
# @lc code=end
