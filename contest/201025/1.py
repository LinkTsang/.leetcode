from collections import *
from typing import *

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        t = defaultdict(lambda :0)
        releaseTimes = [0] + releaseTimes
        for i in range(len(releaseTimes) - 1):
            t[keysPressed[i]] = max(t[keysPressed[i]], releaseTimes[i+1] - releaseTimes[i])
        ans, max_n = None, 0
        for k, v in sorted(t.items()):
            if v >= max_n:
                ans = k
                max_n = v
        return ans

# Solution().slowestKey([9,29,49,50],"cbcd")