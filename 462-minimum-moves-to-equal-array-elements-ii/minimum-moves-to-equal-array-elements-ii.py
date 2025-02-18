class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        num = [1,2,3]
        
        
        num = [1,2,9,10]
        1 ->1
        2 --> 0
        9 --> 7
        10 -->8

        '''
        count = 0
        nums.sort() 
        mid = len(nums)//2
        for i in range(len(nums)):
            count += abs(nums[i]-nums[mid])
        return count