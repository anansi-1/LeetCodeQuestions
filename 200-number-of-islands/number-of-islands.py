class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j,queue):
            if grid[i][j] == "1":
                grid[i][j] = 0
                while queue:
                    i,j = queue.popleft()
                    for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if ((0 <= r <len(grid)) and 0 <= c < (len(grid[0]))) and grid[r][c] == "1":
                            grid[r][c] = "0"
                            queue.append((r,c))
        

        row,col = len(grid),len(grid[0])
        count = 0
        queue = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    queue.append((i,j))
                    bfs(i,j,queue)
        return count
