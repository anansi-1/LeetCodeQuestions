class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float('inf')
        curr_sum = 0
        start = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            while curr_sum >= target:
                min_size = min(min_size, i - start + 1)
                curr_sum -= nums[start]
                start += 1

        return min_size if min_size != float('inf') else 0
