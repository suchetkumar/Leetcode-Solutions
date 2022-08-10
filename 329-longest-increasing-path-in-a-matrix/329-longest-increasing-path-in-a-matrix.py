class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # this is a 2d dynamic programming problem
        h = len(matrix)
        w = len(matrix[0])
        mem = [[1]*w for i in range(h)]
        
        path = 1
        # every iteration, if you find a cell that is greater than a neighbor, 
        # set the neighbor to max(neighbor, cell+1)
        self.change = True
        while self.change:
            self.change = False
            newmem = mem
            for row in range(h):
                for col in range(w):
                    # check all neighbors
                    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                        ny = row+dy
                        nx = col+dx
                        if 0 <= ny < h and 0 <= nx < w:
                            if matrix[ny][nx] < matrix[row][col]:
                                if newmem[ny][nx] <= mem[row][col]:
                                    self.change = True
                                    newmem[ny][nx] = mem[row][col]+1
                                    path = max(path, newmem[ny][nx])
            mem = newmem
        return path
                    