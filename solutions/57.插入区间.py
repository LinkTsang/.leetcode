#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from helper import *
# @lc code=start


class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    if n == 0:
      return [newInterval]
    ans = []

    l1, h1, p1 = 0, n, -1
    while l1 < h1:
      m = l1 + (h1 - l1) // 2
      if intervals[m][0] < newInterval[0]:
        l1 = m + 1
      elif intervals[m][0] > newInterval[0]:
        h1 = m
      else:
        p1 = m
        break

    # print(p1, l1, flush=True)

    if p1 == -1:
      if l1 > 0 and intervals[l1 - 1][1] >= newInterval[0]:
        p1 = l1 - 1
      else:
        p1 = l1

    l2, h2, p2 = 0, n, -1
    while l2 < h2:
      m = l2 + (h2 - l2) // 2
      if intervals[m][1] < newInterval[1]:
        l2 = m + 1
      elif intervals[m][1] > newInterval[1]:
        h2 = m
      else:
        p2 = m
        break

    # print(p2, l2, flush=True)

    if p2 == -1:
      if l2 == n or l2 < n and intervals[l2][0] <= newInterval[1]:
        p2 = l2
      else:
        p2 = l2 - 1

    # print(p1, p2, flush=True)

    v1, v2 = newInterval[0], newInterval[1]
    if 0 <= p1 < n and intervals[p1][0] < v1:
      v1 = intervals[p1][0]
    if 0 <= p2 < n and intervals[p2][1] > v2:
      v2 = intervals[p2][1]

    ans = intervals[:p1] + [[v1, v2]] + intervals[p2 + 1:]
    return ans

# @lc code=end


class Test(TestCase):
  def test_1(self):
    self.assertEqual(
        Solution().insert(
            [[1, 3], [6, 9]],
            [2, 5]
        ),
        [[1, 5], [6, 9]]
    )

  def test_2(self):
    self.assertEqual(
        Solution().insert(
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8]
        ),
        [[1, 2], [3, 10], [12, 16]]
    )

  def test_empty(self):
    self.assertEqual(
        Solution().insert(
            [],
            [4, 8]
        ),
        [[4, 8]]
    )

  def test_head(self):
    self.assertEqual(
        Solution().insert(
            [[4, 8]],
            [1, 2]
        ),
        [[1, 2], [4, 8]]
    )

  def test_tail(self):
    self.assertEqual(
        Solution().insert(
            [[1, 2]],
            [4, 8]
        ),
        [[1, 2], [4, 8]]
    )


run_tests()
