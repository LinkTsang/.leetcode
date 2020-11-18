from collections import *


class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    c1, c2 = Counter(word1), Counter(word2)
    return len(c1) == len(c2) and sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())