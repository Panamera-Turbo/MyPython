from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a:int
        n = len(nums)
        if n == 1:
            return nums[0]

        a = nums[0]

        for i in range(1,n):
            a = a ^ nums[i]
        
        return a

