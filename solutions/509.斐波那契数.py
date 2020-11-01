#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
  def fib(self, N: int) -> int:
    table = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
             4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
    return table[N]
# @lc code=end


def fib(N: int) -> int:
  first, second = 0, 1
  if N <= 1:
    return N
  for _ in range(2, N + 1):
    first, second = second, first + second
  return second


print([fib(i) for i in range(31)])
