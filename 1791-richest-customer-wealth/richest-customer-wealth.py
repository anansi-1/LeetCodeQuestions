class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = float('-inf')
        for i in accounts:
            current_money = 0
            for j in i:
                current_money += j
            richest = max(richest,current_money)
        return richest
