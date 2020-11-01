from typing import List


class Solution:
  def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    count = 0
    for i in range(len(arr)):
      for j in range(len(pieces)):
        if arr[i] == pieces[j][0]:
          s = len(pieces[j])
          if arr[i:i + s] != pieces[j]:
            return False
          else:
            count += s
    return count == len(arr)


print(Solution().canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
print(Solution().canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]]))
