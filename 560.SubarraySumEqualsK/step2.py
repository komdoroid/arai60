from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_to_count = {0: 1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k  in prefix_to_count:
                count += prefix_to_count[prefix_sum - k]
            if prefix_sum in prefix_to_count:
                prefix_to_count[prefix_sum] += 1
            else:
                prefix_to_count[prefix_sum] = 1
        return count
