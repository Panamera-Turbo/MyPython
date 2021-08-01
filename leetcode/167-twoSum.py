from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i = 0
        j = n - 1

        ans = [None] * 2

        while i < j:
            if numbers[i] + numbers[j] == target:
                ans[0] = i + 1
                ans[1] = j + 1
                return ans
            elif numbers[i + 1] + numbers[j] > target:
                j -= 1
                continue
            else:
                i += 1

a = Solution()
b = [2,7,11,15]
t = 9
print(a.twoSum(b,t))