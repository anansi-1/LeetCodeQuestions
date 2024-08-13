class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name = {}
        for h,n in zip(heights,names):
            height_to_name[h] = n
        
        sorted_names = []
        for h in  reversed(sorted(heights)):
            sorted_names.append(height_to_name[h])
        
        return sorted_names