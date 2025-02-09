class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = float('-inf')
        for customer in accounts:
            wealth = 0            
            for money in customer:
                wealth += money
            richest = max(richest,wealth)
        return richest

            