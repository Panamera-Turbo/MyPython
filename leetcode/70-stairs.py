class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else :
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # 不行，超时了
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n == 2:
            return 2
        else:
            a = 1
            b = 2
            while n > 2:
                a = a + b
                t = b
                b = a
                a = t
                n = n-1
            return b


a = Solution()
print(a.climbStairs(2))
print(a.climbStairs(44))