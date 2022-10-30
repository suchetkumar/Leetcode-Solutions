class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        a = self.grayCode(n-1)
        a2 = list(map(lambda x: x+2**(n-1),a))
        return a+a2[::-1]
        