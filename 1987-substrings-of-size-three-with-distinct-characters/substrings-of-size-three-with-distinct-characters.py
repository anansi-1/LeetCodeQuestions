class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dict = {}
        count = 0
        window_start = 0
        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i],0) + 1
            if i>=2:
                if len(dict) == 3:
                    count += 1
                dict[s[window_start]] -= 1
                if dict[s[window_start]] == 0:
                    del dict[s[window_start]]
                window_start += 1
        return count