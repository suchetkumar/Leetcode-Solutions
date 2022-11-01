class Solution:
    def minOperations(self, s: str) -> int:
        c = 0
        one = False
        if s[0] == '1':
            one = True
        for i in range(1, len(s)):
            one = not one
            if s[i] == '1' and not one:
                c += 1
            elif s[i] == '0' and one:
                c += 1
        return min(c, len(s)-c)