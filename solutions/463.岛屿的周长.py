#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
from helper import *
# @lc code=start


class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    m = len(grid)
    if m == 0:
      return 0
    n = len(grid[0])
    ans = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = i + di, j + dj
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != 1:  
              ans += 1
            
    return ans


# @lc code=end
assertEqual(Solution().islandPerimeter([[0, 1, 0, 0],
                                        [1, 1, 1, 0],
                                        [0, 1, 0, 0],
                                        [1, 1, 0, 0]]), 16)
assertEqual(Solution().islandPerimeter([]), 0)
