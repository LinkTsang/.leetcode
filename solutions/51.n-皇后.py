#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    ans = []
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
      if i >= n:
        ans.append([''.join(r) for r in board])
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


Solution().solveNQueens(4)


'''
FFTF => FTTT

TFTF => 


'''
