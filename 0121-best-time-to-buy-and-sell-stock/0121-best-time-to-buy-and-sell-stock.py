class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0];
        profit = 0; 
        for r in range(1,len(prices)):
            if prices[r]< buy:
                buy = prices[r];
            profit = max(profit, prices[r]-buy);
        return profit; 
            
