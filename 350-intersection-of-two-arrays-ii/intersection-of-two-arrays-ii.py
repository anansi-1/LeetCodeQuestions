class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        output = []
        for n in nums2:
            if count[n]>0:
                output.append(n)
                count[n]-=1
        return output