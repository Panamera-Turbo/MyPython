from typing import *

# Do not return anything, modify nums in-place instead.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        for i in range(k):
            nums.insert(0,nums.pop(n-1))
    

a = Solution()
b = [1,2,3,4,5,6,7]
k = 3
a.rotate(b,k)
print(b)