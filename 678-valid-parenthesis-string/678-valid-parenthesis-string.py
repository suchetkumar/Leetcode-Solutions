class Solution:
    def checkValidString(self, s: str) -> bool:
        # let ( be 1, * be 1, 0, or -1, ) be -1
        # at any point, we must be positive and must end with 0
        m = [0]
        for c in s:
            if c == '(':
                m = [i+1 for i in m]
            elif c == ')':
                if m[0] == 0:
                    m = m[:-1]
                else:
                    m = [i-1 for i in m]
            else:
                if m[0] == 0:
                    m.append(m[-1]+1)
                else:
                    m = [m[0]-1] + m + [m[-1]+1]
                    
            if not len(m):
                return False
        return 0 in m