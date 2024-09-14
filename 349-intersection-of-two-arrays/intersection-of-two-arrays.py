class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for i in set(nums1):
            if i in nums2:
                intersection.append(i)
        
        return intersection
        