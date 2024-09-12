class Solution {
    public int[] countBits(int n) {
        int[] dp = new int[n+1];
        int significantBit=1;
        dp[0] = 0;
        for(int i=1;i<=n;i++)
        {   if(i== 2*significantBit){
            significantBit= i;
        }
            dp[i] = 1+dp[i-significantBit];
        }
        return dp;
    }
}