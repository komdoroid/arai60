from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_to_count = defaultdict(int)

        prefix_to_count[0] = 1
        for num in nums:
            prefix_sum += num
            count += prefix_to_count[prefix_sum - k]
            prefix_to_count[prefix_sum] += 1
        return count
