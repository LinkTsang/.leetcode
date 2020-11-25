#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

  def __init__(self):
    """
    initialize your data structure here.
    """
    self.min_s = [float('inf')]
    self.s = []

  def push(self, x: int) -> None:
    self.s.append(x)
    self.min_s.append(min(x, self.min_s[-1]))

  def pop(self) -> None:
    self.s.pop()
    self.min_s.pop()
    
  def top(self) -> int:
    return self.s[-1] if self.s else None

  def getMin(self) -> int:
    return self.min_s[-1] if self.min_s else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
