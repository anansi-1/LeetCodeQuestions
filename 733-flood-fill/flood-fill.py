class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            def dfs(r,c,orginal):
                image[r][c] = color
                for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if (0 <= i < len(image) and 0 <= j < len(image[0])) and image[i][j] == orginal:
                        dfs(i,j,orginal)
            
            if image[sr][sc] == color:
                return image

            orginal = image[sr][sc]
            image[sr][sc] = color
            
            for r,c in [(sr+1,sc),(sr-1,sc),(sr,sc+1),(sr,sc-1)]:
                if (0 <= r < len(image) and 0 <= c < len(image[0])) and image[r][c] == orginal:
                    print(orginal)
                    dfs(r,c,orginal)
            return image
