#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
  def totalNQueens(self, n: int) -> int:
    ans = 0
    board = [["."] * n for _ in range(n)]

    valid = [True] * n

    def isValid(i, j):
      if not valid[j]:
        return False

      x, y = i - 1, j - 1
      while x >= 0 and y >= 0:
        if board[x][y] == 'Q':
          return False
        x, y = x - 1, y - 1

      x, y = i - 1, j + 1
      while x >= 0 and y < n:
        if board[x][y] == 'Q':
          return False
        x, y = x - 1, y + 1

      return True

    def bt(i):
      nonlocal ans
      if i >= n:
        ans += 1
        return
      for j in range(n):
        if isValid(i, j):
          board[i][j] = 'Q'
          valid[j] = False
          bt(i + 1)
          valid[j] = True
          board[i][j] = '.'

    bt(0)
    return ans
# @lc code=end
