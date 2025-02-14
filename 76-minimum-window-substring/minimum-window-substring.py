class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        min_len = float('inf')
        ans = ""
        t_count = Counter(t) 
        window = Counter()  
        l = 0   
        def check(window, t_count):
            for key in t_count:
                if window[key] < t_count[key]:
                    return False
            return True
        for r in range(len(s)):
            window[s[r]]  = window.get(s[r],0) + 1
            while check(window,t_count):
                if (r-l+1) < min_len:
                    ans = s[l:r+1]
                    min_len = r - l + 1
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return ans