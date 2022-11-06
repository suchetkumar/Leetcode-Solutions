class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # start, hit every 0, end
        zeros = 0
        for row in grid:
            zeros += row.count(0)
        out = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            nonlocal out
            if not 0 <= i < rows or not 0 <= j < cols or (i,j) in visited or grid[i][j] == -1 or grid[i][j] == 1:
                return
            if grid[i][j] == 2:
                if len(visited) == zeros:
                    out += 1
                return
            visited.add((i,j))    
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            visited.remove((i,j))
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    dfs(y-1, x)
                    dfs(y+1, x)
                    dfs(y, x+1)
                    dfs(y, x-1)
        
        return out