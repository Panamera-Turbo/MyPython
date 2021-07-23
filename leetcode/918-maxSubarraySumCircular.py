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

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        temp_nums = nums
        # print(temp_nums)
        max_sum = self.maxSubArray(nums)
        for i in range(0, n):
            x = temp_nums.pop(0)
            temp_nums.append(x)
            max_sum = max(max_sum, self.maxSubArray(temp_nums))

                

        return max_sum

nums = [3,-1,2,-1]
a = Solution()
print(a.maxSubarraySumCircular(nums))