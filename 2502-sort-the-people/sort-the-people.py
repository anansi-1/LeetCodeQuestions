class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            my_dict = {}
            ans = []
            for i in range(len(heights)):
                my_dict[heights[i]] = names[i]
            
            for i in range(len(heights)):
                for j in range(i + 1, len(heights)):
                    if heights[i] < heights[j]:
                        heights[i],heights[j] = heights[j], heights[i]
                    else:
                        continue
            for i in (heights):
                ans.append(my_dict[i])
            return ans
