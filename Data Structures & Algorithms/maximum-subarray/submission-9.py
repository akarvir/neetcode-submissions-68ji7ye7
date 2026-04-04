# max(prefix[i-1]+curr,curr)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = nums[0]
        kad = nums[0]
        for i in range(1,len(nums)):
            prefix = max(nums[i], prefix +nums[i])
            kad = max(kad,prefix)
        return kad
        