from typing import *


class OrderedStream:

  def __init__(self, n: int):
    self.stream = [None] * (n + 1)
    self.ptr = 1

  def insert(self, id: int, value: str) -> List[str]:
    self.stream[id] = value
    if self.stream[self.ptr] != None:
      end = self.ptr + 1
      for i in range(self.ptr + 1, len(self.stream)):
        if self.stream[i]:
          end += 1
        else:
          break
      ans = self.stream[self.ptr:end]
      self.ptr = end
      return ans
    else:
      return []

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
