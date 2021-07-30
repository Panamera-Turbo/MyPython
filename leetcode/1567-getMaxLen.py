from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0

        while nums[0] == 0:
            if len(nums) == 1:
                if nums[0] > 0:
                    return 1
                else:
                    return 0
                    
            nums.pop(0)
            

        n = len(nums)
        positive = [None] * n
        negative = [None] * n
        
        positive[0] = (int)(nums[0] > 0)
        negative[0] = 1 - positive[0]
        ans = max(ans, positive[0])

        for i in range(0+1,n):
            print("\nRound" + str(i))
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                if negative[i-1] == 0:
                    negative[i] = 0
                else :
                    negative[i] = negative[i - 1] + 1


            elif nums[i] < 0:
                negative[i] = positive[i - 1] + 1
                if negative[i - 1] != 0:
                    positive[i] = negative[i - 1] + 1
                else:
                    positive[i] = 0

            else:
                positive[i] = 0
                negative[i] = 0

            ans = max(ans, positive[i-1])

            print("p=" + str(positive[i]))
            print("n=" + str(negative[i]))
        ans = max(ans, positive[n-1])
        return ans

nums = [0,0,0,0]
a = Solution()
print(a.getMaxLen(nums))