class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        ans = 0
        i,j = 0, n-1
        target = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] == target:
                ans += skill[i]*skill[j]
                i += 1
                j -= 1
            else:
                return - 1
        return ans
        
        

            