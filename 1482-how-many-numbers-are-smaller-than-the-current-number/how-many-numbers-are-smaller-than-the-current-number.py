class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        dic = {}
        result = []
        
        for i in range(len(sortedNums)):
            if sortedNums[i] not in dic:
                dic[sortedNums[i]]=i
        for i in nums:
            result.append(dic[i])
        return result