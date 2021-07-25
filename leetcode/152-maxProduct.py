from typing import List, NoReturn


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre_max = nums[0]
        pre_min = nums[0]
        max_ans = nums[0]

        for i in range(1, n):
            if nums[i] < 0:     # 出现负数使得最大变最小，最小变最大
                x = pre_min
                pre_min = pre_max
                pre_max = x

            pre_min = min(pre_min * nums[i], nums[i])   
            pre_max = max(pre_max * nums[i], nums[i])
            max_ans = max(max_ans, pre_max)

        return max_ans

nums = [2,3,-2,4,-4]
nums = [-2,0,-1]
nums = [-2, 3, -4]
a = Solution()
print(a.maxProduct(nums))