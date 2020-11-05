#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#
from helper import *
# @lc code=start
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
      return min(len(candies) // 2, len(set(candies)))

# @lc code=end

