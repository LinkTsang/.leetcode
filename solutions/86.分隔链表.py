#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
    head1 = ListNode(None)
    head2 = ListNode(None)
    curr1 = head1
    curr2 = head2
    while head:
      print(head.val)
      if head.val < x:
        curr1.next = head
        curr1 = curr1.next
      else:
        curr2.next = head
        curr2 = curr2.next
      head = head.next
    curr2.next = None
    curr1.next = head2.next
    return head1.next
# @lc code=end
