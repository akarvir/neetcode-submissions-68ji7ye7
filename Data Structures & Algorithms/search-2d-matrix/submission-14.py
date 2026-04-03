class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # why not append all to a bigass array, then perform binary search on it? [1,3,5,7] 
        def bs(l,r,nums,t):
            while l<=r:
                mid = (l+r)//2
                s = nums[mid]
                if s == t:
                    return mid
                if s>t:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        
        l = 0
        r = len(matrix)-1
        pivot = -1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                pivot = mid
                break
            elif matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        if pivot == -1:
            pivot = r
        return bs(0,len(matrix[0])-1,matrix[pivot],target) !=-1
        
                

# [1,2,4,5] l = 0, r = 3, mid = 1
# [1,2,4,5] l = 2, r= 3, mid = 2
# [1,2,4,5], l = 2, r =1, loop breaks
# r is what we want. 


            


