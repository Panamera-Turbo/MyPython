class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        n = len(str)
        print(n)

        for i in range(n):
            while s2[i] in s1:
                i += 1
                

                
            