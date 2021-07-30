from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        head = 0
        tail = n - 1
        i = (int)((head + tail) / 2)

        while head < tail - 1:
            if nums[i] == target:
                return i
            
            elif nums[i] > target:
                tail = i - 1
                i = (int)((head + tail) / 2)
            else :
                head = i + 1
                i = (int)((head + tail) / 2)
        
        if nums[head] == target:
            return head
        elif nums[tail] == target:
            return tail
        else:
            return -1

a = Solution()
nums = [0]
target = 0
print(a.search(nums, target))