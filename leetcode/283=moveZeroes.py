from typing import List
# Do not return anything, modify nums in-place instead.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        zero_count = 0
        
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
        for m in range(zero_count):
            nums.remove(0)
        print(zero_count)
        for k in range(zero_count):
            # n = len(nums)
            nums.append(0)


a = Solution()
b = [0,1,0,3,12]
a.moveZeroes(b)
print(b)