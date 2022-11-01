import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = list(collections.Counter(s).values())
        freqs.sort(reverse=True)
        seen = set()
        c = 0
        for f in freqs:
            n = f
            while n in seen:
                n -= 1
            c += f-n
            if n > 0:
                seen.add(n)
        return c
        
        
        