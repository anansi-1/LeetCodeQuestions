class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                result.append(True)
            else:
                 result.append(False)
        return result