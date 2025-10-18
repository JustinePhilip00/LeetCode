class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0;
        curProf = 0;
        buy = prices[0];
        for r in range(1, len(prices)):
            curProf = prices[r]- buy;
            maxProf = max(maxProf, curProf);
            if prices[r]<buy:
                buy = prices[r];
        return maxProf;



            
