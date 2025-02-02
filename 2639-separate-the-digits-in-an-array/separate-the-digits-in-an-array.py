class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = "".join(map(str,nums))
        return [int(digit) for digit in ans]