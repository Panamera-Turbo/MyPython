class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pre = 0
        cur = 0
        ans = 0
        store = []
        n = len(s)

        while cur < n:
            # print(pre)
            if pre < cur and s[cur] in store:
                store.remove(s[cur])
                ans = max(ans, cur - pre)
                pre += 1
                continue
            else:
                store.append(s[cur])
                cur += 1
                

        ans = max(ans, cur - pre)
        return ans

a = Solution()
b =  "0123456789"
b =  "abcabcbb"
print(a.lengthOfLongestSubstring(b))