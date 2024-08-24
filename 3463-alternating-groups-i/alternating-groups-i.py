class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        return sum(colors[i-1] != colors[i] != colors[(i+1)%len(colors)] for i in range(len(colors)))