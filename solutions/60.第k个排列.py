#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
  def getPermutation(self, n: int, k: int) -> str:
    p = [str(i) for i in range(1, n + 1)]
    current = 0
    ans = []

    def bt(i):
      nonlocal current
      nonlocal ans

      if i == len(p):
        current += 1
        if current == k:
          ans = p[:]
        return
      for j in range(i, len(p)):
        p[i], p[j] = p[j], p[i]
        bt(i + 1)
        if current == k:
          return
        p[i], p[j] = p[j], p[i]

    bt(0)
    return ''.join(ans)


# @lc code=end
print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(3, 5))
assert Solution().getPermutation(3, 5) == "312"