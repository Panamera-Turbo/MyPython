from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if target > nums[n-1]:
            return n
        elif target < nums[0]:
            return 0
        
        l = 0
        r = n-1
        

        while l < r:
            m = (int)(l + (r - l) / 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m + 1
        
        return l


a = Solution()
nums = [1,3,5,6]
t = 2
print(a.searchInsert(nums, t))