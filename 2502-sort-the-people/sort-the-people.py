class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict = {}
        ans = []
        j = 0
        for i in heights:
            dict[i] = names[j]
            j += 1
        heights.sort(reverse=True)
        for i in heights:
            ans.append(dict[i])
        return ans