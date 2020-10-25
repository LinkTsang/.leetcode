#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import *
# @lc code=start
class Solution:
  def partitionLabels(self, S: str) -> List[int]:
    end_position = [0] * 26
    base = ord('a')
    for i in range(len(S)):
      end_position[ord(S[i]) - base] = i + 1
    ans = []
    i, l, h = 0, 0, end_position[ord(S[0]) - base]
    while i < len(S):
      while i < h:
        h = max(h, end_position[ord(S[i]) - base])
        i += 1
      ans.append(h - l)
      if h < len(S):
        l = h
        h = end_position[ord(S[l]) - base]
        i = l
      else:
        break
    return ans

# @lc code=end
S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
S = "a"
print(Solution().partitionLabels(S))
S = "aaaa"
print(Solution().partitionLabels(S))
S = "azzzzza"
print(Solution().partitionLabels(S))