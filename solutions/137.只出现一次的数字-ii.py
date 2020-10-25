#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        twos, ones = 0, 0
        for n in nums:
            ones = ones ^ n and ~twos
            twos = twos ^ n and ~ones
        return ones
# @lc code=end

