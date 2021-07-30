from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        pre = 0
        cur = 1
        n = len(values)

        score = values[cur] - cur + values[pre] + pre
        for i in range(1, n):
            if(values[i] + values[pre] + pre - i < values[i] + values[i-1] - 1):
                pre = i - 1
                score = max(score, values[i] + values[i - 1] - 1)    
            else:
                score = max(score, values[i] + values[pre] + pre - i)



        return score

a = Solution()
nums = [1,2]
print(a.maxScoreSightseeingPair(nums))