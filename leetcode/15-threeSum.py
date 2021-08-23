from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        if n < 3:
            return ans
        
        for i in range(n-2):
            # print(i)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1
            j = i + 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue

                x = nums[i] + nums[j] + nums[k]
                if x == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif x < 0:
                    j += 1
                else:
                    k -= 1

        return ans

a = Solution()
b = [-1,0,1,2,-1,-4]
b = [0,0,0,0,0,0,0]
b = [-1,0,1,0]
print(a.threeSum(b))