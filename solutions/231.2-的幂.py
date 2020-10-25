#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n != 0 and (-n & n) == n
# @lc code=end


'''
0100

1011
1100

获取二进制中最右边的 1：
-x & x
去除二进制中最右边的 1：
x & (x - 1)
'''