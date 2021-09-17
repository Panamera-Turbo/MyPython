from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        i = 0
        j = n - 1

        tnums = nums.copy()
        tnums.sort()
        ans = [None for i in range(2)]
        print(nums)
        print(tnums)

        while i < j:
            if tnums[i] + tnums[j]  == target:
                ans = [i,j]
                break
            elif tnums[i] + tnums[j] < target:
                i += 1
            else:
                j -= 1

        print(ans)
        
        for k in range(n):
            if nums[k] == tnums[i]:
                ans[0] = k
                break

        for l in range(n):
            if nums[l] == tnums[j] and l != k:
                ans[1] = l
                break
            
        return ans

a = Solution()
b = [3,3]
t = 6
print(a.twoSum(b,t))