#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#
from helper import *
# @lc code=start


class Solution:
  def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    max_d = R + C - 2
    ans = [[r0, c0]]
    for d in range(1, max_d + 1):
      for dr in range(0, d + 1):
        dc = d - dr

        if dr == 0:
          rcs = ((r0, c0 + dc),
                 (r0, c0 - dc))
        elif dc == 0:
          rcs = ((r0 + dr, c0),
                 (r0 - dr, c0))
        else:
          rcs = ((r0 + dr, c0 + dc),
                 (r0 + dr, c0 - dc),
                 (r0 - dr, c0 + dc),
                 (r0 - dr, c0 - dc))

        for r, c in rcs:
          if 0 <= r < R and 0 <= c < C:
            ans.append([r, c])
    return ans

# @lc code=end

# @lc test=start
2
2
0
1
# @lc test=end


class Solution:
  def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

    ret = [(i, j) for i in range(R) for j in range(C)]
    ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return ret
