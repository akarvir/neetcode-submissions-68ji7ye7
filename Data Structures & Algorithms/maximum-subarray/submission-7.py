# max(prefix[i-1]+curr,curr)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = max(prefix[i-1]+nums[i],nums[i])
        return max(prefix)
            
        