class TimeMap:
    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        a = self.m[key]
        # get the latest prev timestamp <= timestamp
        l = 0
        r = len(a)
        while l < r:
            mid = (l+r)//2    
            if a[mid][0] <= timestamp:
                l = mid+1
            elif a[mid][0] > timestamp:
                r = mid
            
        if r == 0:
            return ""
        return a[r-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)