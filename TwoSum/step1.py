class Solution(object):
    def twoSum(self, nums, target):
        l, r = 0, 0
        while l<len(nums):
            diff = target - nums[l]
            if diff in nums[l+1:]:
                r = l + nums.index(diff) + 1
                return ([l, r])