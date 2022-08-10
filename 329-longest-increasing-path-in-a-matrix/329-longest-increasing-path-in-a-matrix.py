class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
                
        lens = [[0]*len(matrix[0]) for i in range(len(matrix))]
        
        def dfs(matrix, i, j, prev):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                if matrix[i][j] > prev:
                    if lens[i][j] != 0:
                        return lens[i][j]
                    ret = max([1+dfs(matrix, i-1, j, matrix[i][j]), 
                                1+dfs(matrix, i+1, j, matrix[i][j]), 
                                1+dfs(matrix, i, j-1, matrix[i][j]), 
                                1+dfs(matrix, i, j+1, matrix[i][j])])
                    lens[i][j] = ret
                    return ret
                
                return 0
            return 0
        
        for i in range(len(lens)):
            for j in range(len(lens[i])):
                dfs(matrix, i, j, -1)
                
        return max([max(lens[i]) for i in range(len(lens))])