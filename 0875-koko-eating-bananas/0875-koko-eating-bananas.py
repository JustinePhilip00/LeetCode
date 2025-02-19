class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left= 1;
        right= max(piles);
        output = right;
        while left<= right:
            k= (left+right)//2;
            hours = 0;
            for p in piles:
                hours = hours+ math.ceil(p/k);
            
            if hours <= h:
                output = min(output,k);
                right = k-1;
            else:
                left = k+1;
        return output;
        