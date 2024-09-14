class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        uncommon = []
        count = Counter(s2)

        for i in s2:
            if i not in s1 and count.get(i) == 1:
                uncommon.append(i)
        count = Counter(s1)
        for i in s1:
            if i not in s2 and count.get(i) == 1:
                uncommon.append(i)
        return uncommon