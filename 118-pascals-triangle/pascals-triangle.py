class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows - 1):
            r = [0] + ans[-1] + [0]
            row = []
            for i in range(len(ans[-1]) + 1):
                row.append(r[i] + r[i+1])
            ans.append(row)
        return ans    