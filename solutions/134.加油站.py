#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from helper import *
from itertools import chain

# @lc code=start


class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    delta = [g - c for g, c in zip(gas, cost)]
    n = len(delta)
    for i in range(n):
      if delta[i] < 0:
        continue
      s = delta[i]
      ok = True
      for j in chain(range(i + 1, n), range(0, i)):
        s += delta[j]
        if s < 0:
          ok = False
          break
      if ok:
        return i
    return -1


# @lc code=end
