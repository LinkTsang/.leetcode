#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
from helper import *
# @lc code=start


class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    return all([c == 1 for c in Counter(Counter(arr).values()).values()])


# @lc code=end
assertEqual(Solution().uniqueOccurrences([]), True)
assertEqual(Solution().uniqueOccurrences([1]), True)
assertEqual(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]), True)
assertEqual(Solution().uniqueOccurrences([1, 2]), False)
assertEqual(Solution().uniqueOccurrences(
    [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]), True)
