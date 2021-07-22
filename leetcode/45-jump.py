from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minJump = n
        
        if n == 0 | n == 1:
            return 0

        reachJump = [None] * n
        reachJump[0] = 0
        reachJump[1] = 1

        for k in range(2, n):
            reachJump[k] = n

        for i in range(1,n):
            for j in range(0, i):
                if nums[j] + j < i:
                    continue
                reachJump[i] = min(reachJump[j] + 1, reachJump[i])


        return reachJump[n-1]




nums = [2,3,0,1,4]

a = Solution()
print(a.jump(nums))