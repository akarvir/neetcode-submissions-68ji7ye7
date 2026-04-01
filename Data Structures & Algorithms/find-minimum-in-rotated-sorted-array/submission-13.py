class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        n = len(nums)
        # first, find index of min.  
        while l<r:
            mid = (l+r)//2
            if nums[mid] <= nums[r]: #[4,5,0,1,2,3]
                r = mid
            else:
                l = mid+1
        return nums[l]





# [2,3,4,5,1]
#[3,4,5,6,7,1,2]
# [5,1,2,3,4] , l = 2, r = 1, res = 1, while loop terminated. 
# [4,1,2,3]
