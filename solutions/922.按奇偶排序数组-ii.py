#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#
from helper import *
# @lc code=start


class Solution:
  def sortArrayByParityII(self, A: List[int]) -> List[int]:
    ans = [0] * len(A)
    i, j = 0, 1
    for a in A:
      if a % 2 == 0:
        ans[i] = a
        i += 2
      else:
        ans[j] = a
        j += 2
    return ans
# @lc code=end
