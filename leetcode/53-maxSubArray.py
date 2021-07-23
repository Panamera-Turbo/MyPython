from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        n = len(nums)
        former_sum = 0
        for i in range(0, n):
            former_sum = max(former_sum + nums[i], nums[i])
            max_sum = max(max_sum, former_sum)

        return max_sum


            


nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
print(a.maxSubArray(nums))