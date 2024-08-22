class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        s = list(s)
        count = {}
        j = 0
        goodString = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1


            if i >= 2:
                if len(count) == 3:
                    goodString += 1                
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    del count[s[j]]
                j += 1
        return goodString