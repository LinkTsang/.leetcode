#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
from helper import *
# @lc code=start


class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:

    ans = 0
    n = len(points)
    for i in range(n):
      for j in range(i + 1, n):
        a = (points[j][0] - points[i][0], points[j][1] - points[i][1])
        for k in range(j + 1, n):
          b = (points[k][0] - points[i][0], points[k][1] - points[i][1])
          ans = max(ans,
                    abs(a[0] * b[1] - a[1] * b[0]))
    return 0.5 * ans
# @lc code=end
