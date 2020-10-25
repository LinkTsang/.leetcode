#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#

# @lc code=start
class Solution:
  def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    m = {v: i for i, v in enumerate(intervals)}
    intervals_sorted = sorted(intervals, key=lambda x: x[0])

    def bsearch(intervals, begin, end, target):
        mid = begin + (end - begin) // 2
        while begin < end:
            if intervals[mid][0] >= target:
                end = mid
            else:
                begin = mid
        return 
# @lc code=end

'''
[[3, 4], [2, 3], [1, 2]]

[1, 2][2, 3][3, 4]
2         1    0
'''