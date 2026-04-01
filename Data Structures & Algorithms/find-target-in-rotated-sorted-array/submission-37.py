class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        pivot = l

        def binarysearch(l,h,target,arr):
            while l<=h:
                mid = (l+h)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    h = mid-1
                else:
                    l = mid+1
            return -1
        result = binarysearch(0,pivot-1,target,nums)
        if result == -1:
            return binarysearch(pivot,n-1,target,nums)
        return result



# [3,4,5,1,2]
# [2,3,4,5,1]

# [3,4,5,6,7,1,2]
# [5,1,2,3,4]

# given that nums[mid] < nums[l], and looking for 4, can go two ways:
# [5,1,2,3,4]
# [4,5,1,2,3]


