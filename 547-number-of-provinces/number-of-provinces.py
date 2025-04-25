class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        adjlist = defaultdict(list)
        for i in range(0,n):
            for j in range(0,n):
                if i != j and isConnected[i][j] == 1:
                    adjlist[i+1].append(j+1)
        visited = [0]*(n+1)
        def dfs(node,visited,adj):
            if visited[node] != 1:
                visited[node] = 1
                for i in adj[node]:
                    dfs(i,visited,adj)
        for i in range(1,n+1):
            if visited[i] != 1:
                count += 1
                dfs(i,visited,adjlist)
        return count