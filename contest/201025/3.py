from typing import *
from collections import *


class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    print(heights)
    m, n = len(heights), len(heights[0])
    consumed = [[0] * n for _ in range(m)]

    def dfs(x, y):
      if x - 1 >= 0 and consumed[x][y] == 0:
        a = max(abs(heights[x][y] - heights[x - 1][y]), consumed[x][y])
        dfs(x - 1, y)
      else:
        a = float('inf')
      if y - 1 >= 0 and consumed[x][y] == 0:
        b = max(abs(heights[x][y] - heights[x][y - 1]), consumed[x][y])
        dfs(x, y - 1)
      else:
        b = float('inf')
      if x + 1 < m and consumed[x][y] == 0:
        c = max(abs(heights[x][y] - heights[x + 1][y]), consumed[x][y])
        dfs(x + 1, y)
      else:
        c = float('inf')
      if y + 1 < n and consumed[x][y] == 0:
        d = max(abs(heights[x][y] - heights[x][y + 1]), consumed[x][y])
        dfs(x, y + 1)
      consumed[x][y] = min(a, b, c, d)
    dfs(0, 0)

    print(consumed)
    return consumed[-1][-1]


print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
print(Solution().minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]))  # 9
print(Solution().minimumEffortPath([[1, 2, 1, 1, 1],
                                    [1, 2, 1, 2, 1],
                                    [1, 2, 1, 2, 1],
                                    [1, 2, 1, 2, 1],
                                    [1, 1, 1, 2, 1]]))  # 0

[0, 1, 1, 1, 1],
[0, 1, 1, 1, 1],
[0, 1, 1, 1, 1],
[0, 1, 1, 1, 1],
[0, 0, 0, 1, 1]
