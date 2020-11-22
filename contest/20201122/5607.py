import math


class Solution:
  def waysToMakeFair(self, nums: List[int]) -> int:
    n = len(nums)
    odd_n = n // 2
    even_n = math.ceil(n / 2)
    odd_presum = [0] * (odd_n + 1)
    even_presum = [0] * (even_n + 1)

    for i in range(odd_n):
      odd_presum[i + 1] = odd_presum[i] + nums[i * 2 + 1]
    for i in range(even_n):
      even_presum[i + 1] = even_presum[i] + nums[i * 2]


    ans = 0
    for i in range(n):
      if i % 2 == 1:
        k = (i - 1) // 2
        oddsum = odd_presum[k] + even_presum[even_n] - even_presum[k + 1]
        evensum = even_presum[k + 1] + odd_presum[odd_n] - odd_presum[k + 1]
      else:
        k = i // 2
        oddsum = odd_presum[k] + even_presum[even_n] - even_presum[k + 1]
        evensum = even_presum[k] + odd_presum[odd_n] - odd_presum[k]
      if oddsum == evensum:
        ans += 1

    return ans