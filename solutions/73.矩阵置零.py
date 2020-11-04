#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
from helper import *
# @lc code=start


class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows, columns = [], []
    m = len(matrix)
    if m == 0:
      return
    n = len(matrix[0])
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          rows.append(i)
          columns.append(j)
    for r in rows:
      for j in range(n):
        matrix[r][j] = 0
    for c in columns:
      for i in range(m):
        matrix[i][c] = 0

# @lc code=end


class Solution1:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows, columns = [], []
    m = len(matrix)
    if m == 0:
      return
    n = len(matrix[0])
    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 0:
          rows.append(i)
          columns.append(j)
    for r in rows:
      for j in range(n):
        matrix[r][j] = 0
    for c in columns:
      for i in range(m):
        matrix[i][c] = 0
