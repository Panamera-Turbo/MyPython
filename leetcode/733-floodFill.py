from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], \
        sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        length = len(image)
        width = len(image[0])
        origin_color = image[sr][sc]

        def DFS(x:int, y:int):
            if image[x][y] == origin_color:
                image[x][y] = newColor
            
                for x1, y1 in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if 0 <= x1 < length and 0 <= y1 < width and image[x1][y1] == origin_color:
                        DFS(x1, y1)

        if origin_color != newColor:
            DFS(sr,sc)    # 千万不要忽视这个判断  

        return image
