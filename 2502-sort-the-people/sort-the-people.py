class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans  = []
        name_height = {}
        for height,name in zip(heights,names):
            name_height[height] = name 

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i] <  heights[j]:
                    heights[i],heights[j] = heights[j],heights[i]
        for i in heights:
            ans.append(name_height[i])
        return ans