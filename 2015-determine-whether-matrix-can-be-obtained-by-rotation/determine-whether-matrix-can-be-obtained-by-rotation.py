class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        if mat == target:
            return True
        for i in range(3):
            temp = [[0]*n for _ in range(n)]
            for rows in range(n):
                for cols in range(n):
                    temp[cols][n-1-rows] = mat[rows][cols]
            mat = temp
            if temp == target:
                return True
        return False
