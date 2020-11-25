#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#
from helper import *
# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        c = Counter(s)
        ans = []
        while c:
          for k in sorted(c.keys()):
            c[k] -= 1
            ans.append(k)
          c += Counter()
          for k in sorted(c.keys(), reverse=True):
            c[k] -= 1
            ans.append(k)
          c += Counter()
        return ''.join(ans)
# @lc code=end

