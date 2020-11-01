class Solution:
  def countVowelStrings(self, n: int) -> int:
    if n == 1:
      return 5
    dp = [1, 1, 1, 1, 1]
    for i in range(2, n + 1):
      ndp = []
      s = 0
      for d in dp:
        s += d
        ndp.append(s)
      dp = ndp
    return sum(dp)


print(Solution().countVowelStrings(2))
print(Solution().countVowelStrings(33))
