class Solution:
  def getSmallestString(self, n: int, k: int) -> str:
    ans = []
    while n > 0:
      x = min(k - n + 1, 26)
      ans.append(x)
      n -= 1
      k -= x

    if ans:
      return ''.join([chr(ord('a') + c - 1) for c in reversed(ans)])


# Solution().getSmallestString(4, 100)
Solution().getSmallestString(74657, 743771)


# class Solution:
#   def getSmallestString(self, n: int, k: int) -> str:

#     def dfs(n, k):
#       # print(n, k)
#       if k < n or k < 1:
#         return None
#       if n == 1:
#         return [chr(ord('a') + k - 1)] if 1 <= k <= 26 else None
#       if k == n:
#         return ['a'] * n
#       for x in range(26, 0, -1):
#         r = dfs(n - 1, k - x)
#         if r:
#           return r + [chr(ord('a') + x - 1)]
#       return None

#     ans = dfs(n, k)
#     if ans:
#       return ''.join(ans)
