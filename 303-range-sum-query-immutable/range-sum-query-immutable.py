class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        if left == 0:
            leftSum = 0
        else:
            leftSum = self.prefix[left-1]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)