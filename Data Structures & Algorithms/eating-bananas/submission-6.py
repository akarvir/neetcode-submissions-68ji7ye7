import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def can_eat(k):
            s = 0
            for i in range(n):
                s+=math.ceil(piles[i]/k)
            return s<=h
        l = 1
        r = max(piles)
        prev = r
        while l<=r:
            mid = (l+r)//2
            if can_eat(mid):
                prev = mid
                r = mid-1
            else:
                l = mid+1
        return prev
        