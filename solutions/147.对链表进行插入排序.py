#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
from helper import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
  def insertionSortList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
      return head
    current = head.next
    last = head
    while current:
      if current.val >= last.val:
        last = last.next
        current = current.next
      elif current.val < head.val:
        last.next = current.next
        current.next = head
        head = current
        current = last.next
      else:
        last.next = current.next
        p, q = head, head.next
        while q and current.val > q.val:
          p, q = p.next, q.next
        p.next = current
        current.next = q
        current = last.next
    return head


# @lc code=end
