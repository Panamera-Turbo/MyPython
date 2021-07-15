class Solution(object):
    def rob_1(self, nums):
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
            nums1 = nums[:n-1]
            nums2 = nums[1:]
            return max(self.rob_1(nums1), self.rob_1(nums2))   