from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # print(n)
        # print(matrix)

        for i in range(n):
            for j in range(i+1,n):
                if i == j:
                    continue
                t = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = t
        
        # print(matrix)
        k = (int)(n / 2)
        for i in range(n):
            for j in range(k):
                # print(i, j)
                x = matrix[i][j]
                matrix[i][j] = matrix[i][-j-1]
                matrix[i][-j-1] = x
                # print(x)

a = Solution()
b = [[1,2,3],[4,5,6],[7,8,9]]
a.rotate(b)
print(b)
