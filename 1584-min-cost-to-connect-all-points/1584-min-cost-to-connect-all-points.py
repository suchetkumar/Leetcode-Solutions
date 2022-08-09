from heapq import heapify, heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # find min spanning tree with Prims algorithm
        def distance(i1, i2):
            x1, y1 = points[i1]
            x2, y2 = points[i2]
            return abs(x1-x2) + abs(y1-y2)
            
        n = len(points)
        allpoints = set([i for i in range(n)])
        visited = set([])
        bfs = [(0,0)]
        heapify(bfs)
        
        t = 0
        count = 0
        while count < n:
            dist, idx = heappop(bfs)
            if idx in visited:
                continue
            visited.add(idx)
            t += dist
            count += 1
            for i in allpoints-visited:
                heappush(bfs, (distance(idx,i), i))
        return t
        

        
        