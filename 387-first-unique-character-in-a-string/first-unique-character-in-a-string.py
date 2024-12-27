class Solution:
    def firstUniqChar(self, s: str) -> int:
        # {l:2,o:2,v:1,e:4,t:1,c:1,d:1}
        # loveleetcode
        occur = {}
        for i in s:
            occur[i] = occur.get(i,0) + 1
        for i in occur:
            if occur[i] == 1:
                ch = i
                return s.index(ch)
        return -1
       
        