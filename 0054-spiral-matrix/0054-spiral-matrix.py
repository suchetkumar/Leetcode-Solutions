class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        # directions 0:left, 1:down, 2:up, 3:right
        direction = 0
        x = 0
        y = 0
        i = 0
        out = []
        while i < rows*cols:
            out.append(matrix[y][x])
            matrix[y][x] = None
            if direction == 0:
                if x == cols-1 or matrix[y][x+1] == None:
                    direction = 1
                    y += 1
                else:
                    x += 1
            elif direction == 1:
                if y == rows-1 or matrix[y+1][x] == None:
                    direction = 2
                    x -= 1
                else:
                    y += 1
            elif direction == 2:
                if x == 0 or matrix[y][x-1] == None:
                    direction = 3
                    y -= 1
                else:
                    x -= 1
            else:
                if y == 0 or matrix[y-1][x] == None:
                    direction = 0
                    x += 1
                else:
                    y -= 1
            i += 1
        return out
        