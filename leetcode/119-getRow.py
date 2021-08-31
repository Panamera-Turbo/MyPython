from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [None] * (rowIndex + 1)
        row = [None] * (rowIndex + 1)

        if rowIndex == 0:
            return [1]
        
        i = 1
        pre[0] = 1
        row[0] = 1
        while i < rowIndex + 1:
            j = 1
            # print(i)
            # print(pre)
            while j < i:
                # print(i,j)
                row[j] = pre[j] + pre[j - 1]
                j += 1
                # print(pre)
                # print(row)
                # print()

            row[j] = 1
            pre = row.copy()
            i += 1
            # print(pre)
            # print(row)
            # print()



        return row

a = Solution()
print(a.getRow(3))