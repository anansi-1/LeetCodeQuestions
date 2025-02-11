class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        ans = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > target:
                break
            if sorted_nums[i] == target:
                ans.append(i)
        return ans