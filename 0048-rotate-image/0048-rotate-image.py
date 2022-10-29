class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                temp[j][n-1-i] = matrix[i][j]
        # print(temp)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j]
        