# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         cost.append(0);
#         for i in range(len(cost)-3,-1,-1):
#             cost[i] = cost[i]+min(cost[i+1], cost[i+2]);
        
#         return min(cost[0],cost[1]);
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]* (len(cost)+1);
        dp[len(cost)] = 0;
        dp[len(cost)-1] = cost[len(cost)-1];
        for i in range(len(cost)-2,-1,-1):
            dp[i] = min(cost[i] + dp[i+1],cost[i]+dp[i+2]);
        return min(dp[0],dp[1]);
