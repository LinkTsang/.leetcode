#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution:
  def isAdditiveNumber(self, num: str) -> bool:
    n = len(num) // 2
    for i in range(n):
        print(num[:i])
# @lc code=end


'''
len(a) + len(b)
len(c) >= len(a)
len(c) >= len(b)

len(a) <= len(num) // 2
'''
