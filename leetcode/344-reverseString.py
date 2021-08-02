from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

a = Solution()
b = ["h","e","l","l","o"]
a.reverseString(b)
print(b)
