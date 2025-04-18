class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_sorted = sorted(nums)
        num_dict = {}
        for i in range(len(num_sorted)):
            number = num_sorted[i]
            if number not in num_dict:
                num_dict[number] = i
        for i in range(len(nums)):
            nums[i] = num_dict[nums[i]]
        return nums