from collections import deque
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mem = {}
        self.d = deque([])
        
    def get(self, key: int) -> int:
        # print(f"get {key}")
        if key in self.mem:
            self.d.remove(key)
            self.d.appendleft(key)
            # print(self.d)
            return self.mem[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print(f"put {key} {value}")
        if key in self.mem:
            self.mem[key] = value
            self.d.remove(key)
            self.d.appendleft(key)
            return
        if len(self.d) == self.cap:
            r = self.d.pop()
            del self.mem[r]
        self.mem[key] = value
        self.d.appendleft(key)
        # print(self.mem, self.d)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)