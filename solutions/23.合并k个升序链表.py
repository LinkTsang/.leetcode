#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
from typing import List


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    def bsearch(lists, v):
      l, h = 0, len(lists)
      while l < h:
        m = (l + h) // 2
        if v < lists[m].val:
          h = m
        elif lists[m].val < v:
          l = m + 1
        else:
          return m
      return l

    lists = [l for l in lists if l]
    lists.sort(key=lambda l: l.val)
    dummy = ListNode()
    p = dummy

    while len(lists) > 1:
      current = lists[0]
      p.next = current
      p = p.next

      current = current.next
      lists = lists[1:]
      if current:
        index = bsearch(lists, current.val)
        lists = lists[:index] + [current] + lists[index:]

    if len(lists) == 1:
      p.next = lists[0]
    return dummy.next
# @lc code=end


result = Solution().mergeKLists([
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(4, ListNode(3))),
    ListNode(2, ListNode(6))
])
r = result
while r:
  print(r.val)
  r = r.next
'''
l1
l2
l3
l4
l5

'''
