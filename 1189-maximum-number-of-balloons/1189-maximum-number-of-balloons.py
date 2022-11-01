from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = Counter(text)
        d = {
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1,
        }
        r = 10**4
        for k in d:
            if k not in f:
                return 0
            r = min(r, f[k]//d[k])
        return r