from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        field = 0
        curField = 0

        length = len(grid)
        width = len(grid[0])

       
        
        def DFS(x:int, y:int) -> int:
            if grid[x][y] == 1:
                ans = 1
                grid[x][y] = 0
                for x1, y1 in [(x + 1, y), (x, y + 1), (x-1,y), (x, y-1)]:
                    if 0 <= x1 < length and 0 <= y1 < width:
                        ans += DFS(x1, y1)
                
                return ans
            else:
                return 0

        for i in range(length):
            for j in range(width):
                field = max(field, DFS(i, j))
        print(grid)
        return field

a = Solution()
b = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# b = [[0,0,0,0,0,0,0,0]]
# b = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(a.maxAreaOfIsland(b))