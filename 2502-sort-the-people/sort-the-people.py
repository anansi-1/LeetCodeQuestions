class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        swapped = False
        for i in range(n-1):
            for j in range(n-1-i):
                if heights[j] < heights[j+1]:
                    heights[j],heights[j+1] = heights[j+1],heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
                    swapped = True
            if (swapped == False):
                break
        return names