#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#
from collections import *
from typing import *
# @lc code=start


class Solution:
  def findLucky(self, arr: List[int]) -> int:
    m = defaultdict(lambda: 0)
    for a in arr:
      m[a] += 1
    ans = -1
    for k, v in m.items():
      if k == v:
        ans = max(ans, k)
    return ans
# @lc code=end
