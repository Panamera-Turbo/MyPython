class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        l = len(cost)
        if l == 0:
            return 0
        elif l == 1:
            return cost[0]
        elif l == 2:
            return min(cost[0] + cost[1], cost[0], cost[1])
        else:
            a = cost[0]
            b = cost[1]
            c = cost[2] + min(a,b)
            for i in range(3,l):
                a = b
                b = c
                c = cost[i] + min(a, b)
            return min(b, c)


a = Solution()
print(a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))