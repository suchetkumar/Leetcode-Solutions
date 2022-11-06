class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            l = min(s)
            seen = set()
            best = None
            idx = s.find(l)
            s = s[idx:]+s[:idx]
            while s not in seen:
                seen.add(s)
                if best == None or s < best:
                    best = s
                idx = s.find(l, 1)
                s = s[idx:]+s[:idx]
            return best
        else:
            return ''.join(sorted(list(s)))