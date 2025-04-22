class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount+1] * (amount+1);
        # dp[0] = 0;
        # for a in range(1, amount+1):
        #     for c in coins:
        #         if a-c >= 0:
        #             dp[a] = min(dp[a], 1+dp[a-c]);
        # return dp[amount] if dp[amount]!=amount+1 else -1;
        dp = [float('inf')] * (amount+1);
        dp[0] = 0;
        print(dp);
        for i in range(1,amount+1):
            for c in coins:
                if i-c >=0:
                    dp[i] = min(dp[i], 1+dp[i-c]);
        print(dp);
        return dp[amount] if dp[amount] != float('inf') else -1;