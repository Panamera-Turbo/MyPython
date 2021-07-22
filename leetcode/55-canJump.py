from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0 | n == 1:
            return True
        elif n == 2:
            if nums[0] > 0:
                return True 
            else:
                return False
        else:
            nowMax = nums[0]
            for i in range(1, n):
                if nowMax < i:
                    return False
                nowMax = max(nowMax, nums[i] + i)
                if nowMax > n - 2:
                    return True

            if nowMax >= n:
                 return True
            return False

nums = [2,5,0,0]

a = Solution()
print(a.canJump(nums))