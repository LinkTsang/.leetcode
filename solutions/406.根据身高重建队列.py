#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
from helper import *
# @lc code=start


class Solution:
  def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda p: (-p[0], p[1]))
    ans = []
    for p in people:
      k = p[1]
      ans[k:k] = [p]
    return ans
# @lc code=end
