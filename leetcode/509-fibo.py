'''
solution1:
执行用时：624 ms, 在所有 Python 提交中击败了26.00%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.03%的用户
'''
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

aa = Solution()
a = aa.fib(4)
print(a)


'''
solution2:
执行用时：20 ms, 在所有 Python 提交中击败了67.51%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了25.47%的用户
'''
class Solution2(object):
    def fib(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            a = 0, b = 1
            while n > 1:
                a = a + b
                t = b
                b = a
                a = t
                n = n-1
            return b