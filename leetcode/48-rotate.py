from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # print(n)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # print(matrix)

        for i in range(n):
            for j in range(n):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

a = Solution()
b = [[1,2,3],[4,5,6],[7,8,9]]
a.rotate(b)
print(b)
