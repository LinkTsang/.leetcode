#
# @lc app=leetcode.cn id=1395 lang=python3
#
# [1395] 统计作战单位数
#

# @lc code=start
class Solution:
  def numTeams(self, rating: List[int]) -> int:
    ans = 0
    for j, r in enumerate(rating):
      i_less = sum(1 if x < r else 0 for x in rating[0:j])
      k_greater = sum(1 if x > r else 0 for x in rating[j + 1:])

      i_greater = sum(1 if x > r else 0 for x in rating[0:j])
      k_less = sum(1 if x < r else 0 for x in rating[j + 1:])

      ans += i_less * k_greater + i_greater * k_less
    return ans
# @lc code=end
