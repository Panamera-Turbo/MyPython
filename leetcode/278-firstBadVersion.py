# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):



class Solution:
    def tryBad(self,n,m):
        if isBadVersion(n) == True & isBadVersion(m) == False:
            return 1
        elif isBadVersion(m):
            return 0
        else :
            return -1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1

        head = 1
        tail = n

        while head < tail:
            i = (int)(head + (tail - head) / 2)
            
            if isBadVersion(i):
                tail = i
            else:
                head = i + 1

        return head