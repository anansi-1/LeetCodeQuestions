class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        '''
        [[10,6,9,1],
         [7,5,11,2],
         [4,8,3,15]]
        '''
        m = len(score)
        ans = []
        col_k = [] # [11,9,3]
        for i in range(m):
            col_k.append(score[i][k])
        col_k.sort(reverse=True)
        for col in col_k:
            for i in range(m):
                if col==score[i][k]:
                    ans.append(score[i])
                    continue
        return ans