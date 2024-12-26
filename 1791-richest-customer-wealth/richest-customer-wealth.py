class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = float('-inf')
        for account in accounts:
            total_money = sum(account)
            if total_money > richest:
                richest = total_money
        return richest