#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    ss = []
    for c in S:
      if c == '#':
        if len(ss) > 0:
          ss.pop()
      else:
        ss.append(c)
    st = []
    for c in T:
      if c == '#':
        if len(st) > 0:
          st.pop()
      else:
        st.append(c)
    return ss == st
# @lc code=end
