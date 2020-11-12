#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
from helper import *
# @lc code=start


class Solution:
  def sortArrayByParity(self, A: List[int]) -> List[int]:
    return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 != 0]
# @lc code=end
