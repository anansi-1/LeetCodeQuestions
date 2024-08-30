class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredList = []
        for i in nums:
            squaredList.append(i*i)
        return sorted(squaredList)