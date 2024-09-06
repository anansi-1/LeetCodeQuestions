class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        rel = {}
        j = 0
        for i in indices:
            rel[i] = s[j]
            j += 1
        ordered = []
        for i in range(len(s)):
            ordered.append(rel.get(i))
        return "".join(ordered)