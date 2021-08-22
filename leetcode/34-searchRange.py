from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n == 0:
            return [-1,-1]
        
        # print("hello")
        head = 0
        tail = n - 1
        mid = (int)(head + (tail - head) / 2)

        while head < tail:
            mid = (int)(head + (tail - head) / 2)
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                tail = mid
            else:
                head = mid + 1


        if nums[tail] == target:
            mid = tail
        elif nums[mid] != target:
            return [-1, -1]
        # elif 

        print(mid)
        
        head = mid
        tail = mid

        while head >= 0 and nums[head] == target:
            head -= 1
        
        while tail < n and nums[tail] == target:
            tail += 1
        
        return [head+1, tail-1]


a = Solution()
b = [1,4]
c = 4
print(a.searchRange(b,c))