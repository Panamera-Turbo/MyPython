from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        head = 0
        tail = n - 1
        i = tail + (int)((head - tail) / 2)
        while head < tail:
            if nums[i] == target:
                return i
            elif nums[i] > target:
                tail = i
                i = tail + (int)((head - tail) / 2)
            else :
                head = i
                i = tail + (int)((head - tail) / 2)
        
        return -1

a = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(a.search(nums, target))