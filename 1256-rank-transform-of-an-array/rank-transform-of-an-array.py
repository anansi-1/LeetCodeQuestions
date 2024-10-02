class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        ranking = {}
        for rank,val in enumerate(sorted_unique):
            ranking[val] = rank + 1
        
        result = []
        for num in arr:
            result.append(ranking[num])
        
        return result