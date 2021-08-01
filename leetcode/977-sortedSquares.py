from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        zero = 0

        n = len(nums)
        while zero < n-1 and nums[zero] < 0:
            zero += 1
        
        base = zero
        


        for i in range(n):
            nums[i] = nums[i] * nums[i]

        if base == 0 or n <= 1:
            return nums
        
        i = base - 1
        j = base
        k = 0
        new_list = [None] * n


        while i >= 0 and j < n:
            if i == 0 and nums[i] <= nums[j]:
                new_list[k] = nums[i]
                k += 1
                while j < n:
                    new_list[k] = nums[j]
                    j += 1
                    k += 1
                break
            elif j == n - 1 and nums[i] >= nums[j]:
                new_list[k] = nums[j]
                k += 1
                while i > -1:
                    new_list[k] = nums[i]
                    k += 1
                    i -= 1
                break
            else:
                if nums[i] > nums[j]:
                    new_list[k] = nums[j]
                    k += 1
                    j += 1
                else:
                    new_list[k] = nums[i]
                    k += 1
                    i -= 1
        
        return new_list


a = Solution()
b = [-4,-1,0,3,10]
# b = [-7,-3,2,3,11]
print(a.sortedSquares(b))

