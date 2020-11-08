#
# @lc app=leetcode.cn id=1402 lang=python3
#
# [1402] 做菜顺序
#
from helper import *
# @lc code=start


class Solution:
  def maxSatisfaction(self, satisfaction: List[int]) -> int:
    satisfaction.sort()
    if satisfaction[-1] <= 0:
      return 0
    ans = 0
    s = 0
    dp = 0
    for i in reversed(range(len(satisfaction))):
      dp += s + satisfaction[i]
      s += satisfaction[i]
      ans = max(ans, dp)

    return ans


# @lc code=end

# @lc test=start
[-1, -8, 0, 5, -9]
14
[4, 3, 2]
20
[-1, -4, -5]
0
[-2, 5, -1, 0, 3, -3]
35
# @lc test=end

assertEqual(Solution().maxSatisfaction([-1, -8, 0, 5, -9]), 14)
assertEqual(Solution().maxSatisfaction([4, 3, 2]), 20)
assertEqual(Solution().maxSatisfaction([-1, -4, -5]), 0)
assertEqual(Solution().maxSatisfaction([-2, 5, -1, 0, 3, -3]), 35)
