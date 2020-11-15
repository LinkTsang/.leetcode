from helper import *


class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    ans = [0] * len(code)
    if k > 0:
      for i in range(len(ans)):
        for j in range(k):
          ans[i] += code[(i + j + 1) % n]
    elif k < 0:
      for i in range(len(ans)):
        for j in range(-k):
          ans[i] += code[(i - j - 1) % n]
    return ans
