class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        m = max(nums) 
        n = -min(nums)
        multi = m + n + 1
        freq_arr = [0] * multi
        ans = []
        for num in nums:
            freq_arr[num+n] += 1
        for i in range(len(freq_arr)):
            for j in range((freq_arr[i])):
                ans.append(i-n)
        return ans