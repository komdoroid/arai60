class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_index = {}
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                num_to_index[nums1[i]] = i
        return list(num_to_index)