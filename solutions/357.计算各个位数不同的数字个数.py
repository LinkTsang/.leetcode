#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution:
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    dp = [1, 9] + [0] * 9
    if n <= 1:
      return sum(dp[:n + 1])
    for i in range(2, min(10, n) + 1):
      dp[i] = dp[i - 1] * (11 - i)
    return sum(dp)
# @lc code=end


'''
2 => [xx ...] 11,22,33,44,55,66,77,88,99   9
3 => [xx., x.x, .xx, ...]   9 * 8 * 3
4 => [.xxx, x.xx, xx.x, xxx., ...]
5 => [xxxx, xxxx, xxxx, xxxx, ...]

f(3) = 9 + f(2) * 8 * 3 + f(2) * 2
f(n) = f(n-1)
'''
