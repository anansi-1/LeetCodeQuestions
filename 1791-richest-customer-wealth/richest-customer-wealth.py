class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = float('-inf')
        for customer in accounts:
            wealth = sum(customer)
            richest = max(wealth,richest)
        return richest
            

            