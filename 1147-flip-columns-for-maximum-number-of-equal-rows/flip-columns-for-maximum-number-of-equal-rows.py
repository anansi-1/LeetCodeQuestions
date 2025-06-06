class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        for r in matrix:
            i = tuple(c if r[0] == 0 else 1 - c for c in r)
            if i not in d:
                d[i] = 0
            d[i] += 1      
        return max(d.values())