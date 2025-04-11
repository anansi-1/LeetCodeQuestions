class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        def dfs(city: int):
            visited[city] = True
            for j in range(len(isConnected)):
                if isConnected[city][j] == 1 and not visited[j]:
                    dfs(j)     
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                count += 1      
        return count
        