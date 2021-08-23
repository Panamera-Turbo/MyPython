from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tmp = [int] * 2

        intervals.sort(key=lambda x: x[0])

        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][0], ans[-1][1] = min(ans[-1][0], interval[0]), max(ans[-1][1], interval[1])

        return ans

