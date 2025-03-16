class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        ans = []
        for i,v in enumerate(groupSizes):
            d[v].append(i) 
            if len(d[v]) == v:
                ans.append(d.pop(v))
        return ans