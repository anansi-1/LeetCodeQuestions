class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        total = s - t
        count = 0
        for i in total:
            count += total[i]
        return count
            