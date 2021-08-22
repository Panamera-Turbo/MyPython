from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return None
        
        m = nums[0]
        count = 1
        

        for i in range(1,n):
            if count == 0:
                m = nums[i]
                count = 1
                continue
            else:
                if m == nums[i]:
                    count += 1
                    # continue
                else:
                    count -= 1

        return m