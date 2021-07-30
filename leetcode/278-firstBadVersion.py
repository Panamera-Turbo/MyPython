# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

START_BAD_VERSION = 2
def isBadVersion(n:int) -> bool:
    return n >= START_BAD_VERSION
        
    

class Solution:
    

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