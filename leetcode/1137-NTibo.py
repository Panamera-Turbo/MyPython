# 泰波那契序列 Tn 定义如下： 

# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            a = 0
            b = 1
            c = 1
            while n > 2:
                d = a + b + c
                a = b
                b = c
                c = d
                n = n -1 
            return c