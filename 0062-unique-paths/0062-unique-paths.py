class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        def fact(x):
            r = 1
            for i in range(1, x+1):
                r *= i
            return r
        return int(fact(m+n)/(fact(m)*fact(n)))