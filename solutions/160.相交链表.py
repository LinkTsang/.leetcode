#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
from helper import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
      return None

    s1, s2 = 0, 0
    count = 0

    p = headA
    while p:
      s1 += p.val
      count += 1
      p = p.next

    p = headB
    while p:
      p.val += 1
      p = p.next

    p = headA
    while p:
      s2 += p.val
      p = p.next

    p = headB
    while p:
      p.val -= 1
      p = p.next

    if s2 == s1:
      return None

    count -= (s2 - s1)
    ans = headA
    for _ in range(count):
      ans = ans.next

    return ans

# @lc code=end
