from typing import *


class Solution:
  def minOperations(self, nums: List[int], x: int) -> int:
    n = len(nums)
    if n == 1:
      return 1 if nums[0] == x else -1

    prefix_sum = [0] * (n + 1)
    postfix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
      prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    for i in range(1, n + 1):
      postfix_sum[i] = postfix_sum[i - 1] + nums[n - i]

    # print(nums)
    # print(prefix_sum)
    # print(postfix_sum)

    ans = n + 1
    for i in range(n + 1):
      if prefix_sum[i] > x:
        break
      t = x - prefix_sum[i]
      low, high = 0, len(postfix_sum)
      while low < high:
        m = low + (high - low) // 2
        if t < postfix_sum[m]:
          high = m
        elif t > postfix_sum[m]:
          low = m + 1
        else:
          # print(x, i, m, prefix_sum[i], postfix_sum[m])
          ans = min(ans, i + m)
          break

    return -1 if ans > n else ans


# print(nums)
# print(prefix_sum)
# print(postfix_sum)

# for k in range(1, n + 1):
#   for i in range(k + 1):
#     j = n - k + i

#     # print(x, i, j, prefix_sum[i], postfix_sum[j])

#     if prefix_sum[i] > x:
#       break
#     s = prefix_sum[i] + postfix_sum[j]
#     if s == x:
#       return k


# class Solution:
#   def minOperations(self, nums: List[int], x: int) -> int:
#     def dfs(nums, x):
#       if x == 0:
#         return 0
#       if x < 0 or len(nums) == 0:
#         return -1
#       if len(nums) == 1:
#         if x == nums[0]:
#           return 1
#         else:
#           return -1

#       left = self.minOperations(nums[1:], x - nums[0]) if x >= nums[0] else -1
#       right = self.minOperations(
#           nums[:-1], x - nums[-1])if x >= nums[-1] else -1
#       if left == -1 and right == -1:
#         return -1
#       if left == -1:
#         return right + 1
#       if right == -1:
#         return left + 1
#       return min(left, right) + 1
#     return dfs(nums, x)
