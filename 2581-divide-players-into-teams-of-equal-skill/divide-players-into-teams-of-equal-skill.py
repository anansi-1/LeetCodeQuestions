class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        num_of_groups =n//2
        target = sum(skill)//num_of_groups
        chemistry = 0
       
        for i in range(n//2):
            if skill[i] + skill[n-1-i] != target:
                return -1
            chemistry += skill[i]*skill[n-1-i]
        return chemistry