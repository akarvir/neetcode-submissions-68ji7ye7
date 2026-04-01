class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[l]:
                if nums[l] <=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<nums[l]:
                    l = mid+1
                else:
                    r = mid-1
        return -1


# [3,4,5,1,2]
# [2,3,4,5,1]

# [3,4,5,6,7,1,2]
# [5,1,2,3,4]

# given that nums[mid] < nums[l], and looking for 4, can go two ways:
# [5,1,2,3,4]
# [4,5,1,2,3]


