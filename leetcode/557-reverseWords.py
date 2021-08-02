class Solution(object):
    def reverseWords(self, s:str)->str:
        new_s = " ".join(s.split(" ")[::-1])[::-1]
        return new_s

