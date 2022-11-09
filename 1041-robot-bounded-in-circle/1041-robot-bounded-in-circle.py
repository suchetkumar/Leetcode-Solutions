class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0,0)
        direction = (0,1)
        instructions *= 4
        for i in instructions:
            if i == 'G':
                pos = (pos[0] + direction[0], pos[1] + direction[1])
            elif i == 'L':
                newdirection = (-direction[1], direction[0])
                direction = newdirection
            elif i == 'R':
                newdirection = (direction[1], -direction[0])
                direction = newdirection
        return pos == (0,0)