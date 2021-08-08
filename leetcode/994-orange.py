from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0

        length = len(grid)
        width = len(grid[0])
        count = 0

        return minute

a = Solution()
b = [[2,1,1],[1,1,0],[0,1,1]]
b = [[2,1,1],[0,1,1],[1,0,1]]
b = [[0,2]]
print(a.orangesRotting(b))