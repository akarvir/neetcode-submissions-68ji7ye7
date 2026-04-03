class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [1,2,0,-1,10,8]
        min_price = float('inf')
        max_price = 0
        max_diff = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            max_diff = max(max_diff,prices[i] - min_price)
        return max_diff
    
        
            
