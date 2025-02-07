class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [ ]
        rows = len(img) - 1 # 0 1 2
        cols = len(img[rows]) # 
        ans = [[0]*cols for _ in range(len(img))]

        for i in range(rows+1): # 0 1 2
            for j in range(cols): # 0 1 2
                directions.append((i,j))
        # print(directions)
        def inbound(x,y):
            return (0<= x < len(img)) and (0<=y < cols)
        #
        # img[i][j]
        # img[i][j-1]
        # img[i-1][j-1]
        # img[i-1][j]
        for i,j in directions:
            s = 0
            count = 0   #(0,0)
            for x in (i-1,i,i+1): 
                for y in (j-1,j,j+1):
                        if inbound(x,y):
                            s += img[x][y]
                            count += 1
            ans[i][j] = s//count
        
        return ans