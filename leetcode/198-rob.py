class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            a = nums[0]
            b = max(a, nums[1])
            max_sum = 0
            for i in range(2, n):
                max_sum = max(a + nums[i], b)
                a = b
                b = max_sum
            return b
        

m = Solution()
l = [1,2,3,1]
l = [2,7,9,3,1]
print(m.rob(l))