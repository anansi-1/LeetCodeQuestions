class Solution:
    def maxArea(self, height: List[int]) -> int:
        x = len(height) - 1
        l = 0
        r = len(height) - 1
        max_amount = 0

        while l < r:
            current = x * (min(height[l], height[r]))
            max_amount = max(current, max_amount)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            x -= 1
        return max_amount