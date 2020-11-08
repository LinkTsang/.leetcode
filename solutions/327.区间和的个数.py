#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
from helper import *
# @lc code=start


class Solution:
  def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    pre_sums = [0]
    s = 0
    for x in nums:
      s += x
      pre_sums.append(s)

    def count(left, right):
      if left == right:
        return 0
      m = (left + right) // 2
      n1 = count(left, m)
      n2 = count(m + 1, right)
      ret = n1 + n2

      i = left
      l, r = m + 1, m + 1
      while i <= m:
        while l <= right and pre_sums[l] - pre_sums[i] < lower:
          l += 1
        while r <= right and pre_sums[r] - pre_sums[i] <= upper:
          r += 1
        ret += (r - l)
        i += 1

      sorted_ = []
      p1, p2 = left, m + 1
      while p1 <= m or p2 <= right:
        if p1 > m:
          sorted_.append(pre_sums[p2])
          p2 += 1
        elif p2 > right:
          sorted_.append(pre_sums[p1])
          p1 += 1
        elif pre_sums[p1] < pre_sums[p2]:
          sorted_.append(pre_sums[p1])
          p1 += 1
        else:
          sorted_.append(pre_sums[p2])
          p2 += 1
      # print(pre_sums)
      pre_sums[left:left + len(sorted_)] = sorted_
      # print(pre_sums)

      return ret

    return count(0, len(pre_sums) - 1)
# @lc code=end


# @lc test=start
[-2, 5, -1]
-2
2
[-1, 1]
0
0
# @lc test=end
