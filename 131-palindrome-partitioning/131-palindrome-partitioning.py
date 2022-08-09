class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ret = []
        def pal(x):
            for i in range(len(x)//2):
                if x[i] != x[-1-i]:
                    return False
            return True
        
        def traverse(m, st):
            if len(st) == 0:
                self.ret.append(m)
                return
            for i in range(len(st)):
                n = st[:i+1]
                if pal(n):
                    traverse(m+[n], st[i+1:])
                    
        traverse([], s)
        return self.ret