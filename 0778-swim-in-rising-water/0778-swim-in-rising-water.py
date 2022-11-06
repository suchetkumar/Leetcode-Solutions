from heapq import heapify, heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # find paths from top left to bottom right
        # find path with smallest maximum
        # increment water values to next and next until destination is wet
        water_values_next = [grid[-1][-1]]
        
        rows=len(grid)
        cols=len(grid[0])
        
        wet = [[False]*cols for i in range(rows)]
        
        visited = set()
        
        def dfs(i, j, water):
            if not 0 <= i < rows or not 0 <= j < cols or (i,j) in visited:
                return
            visited.add((i,j))
            
            if grid[i][j] <= water:
                wet[i][j] = True
                dfs(i+1, j, water)
                dfs(i-1, j, water)
                dfs(i, j+1, water)
                dfs(i, j-1, water)
            else:
                heappush(water_values_next, grid[i][j])
            
        water = -1
        while True:
            last_water = water
            while water == last_water:
                water = heappop(water_values_next)
            visited = set()
            dfs(0,0, water)   
            if wet[-1][-1]:
                return water
        
        
            
        