from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        # print(ans)

        i = 0

        l = 0
        r = n - 1
        u = 0
        d = n - 1

        digit = 1
        
        n_2 = n * n

        while digit <= n_2 :
            for i in range(l, r + 1):
                ans[u][i] = digit
                # print(u,i,ans[u][i])
                digit += 1
            u += 1
            # print()
            
            for i in range(u, d + 1):
                ans[i][r] = digit
                # print(i,r,ans[i][r])
                digit += 1
            r -= 1
            # print()

            for i in range(r, l - 1, -1):
                ans[d][i] = digit
                # print(d,i,ans[d][i])
                digit += 1
            d -= 1
            # print()

            for i in range(d, u - 1, -1):
                ans[i][l] = digit    
                # print(i,l,ans[i][l])
                digit += 1
            l += 1
            # print()

        return ans
                
                


    
# a = Solution()
# print(a.generateMatrix(2))
