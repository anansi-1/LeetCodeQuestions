class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)): #0 1 2 3 4
            for j in range(0,i):
                if heights[i] > heights[j]:
                    names[i],names[j] = names[j],names[i]
                    heights[i],heights[j] = heights[j],heights[i]
        return names