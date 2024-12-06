class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1);
        dp[len(nums)-1] = nums[len(nums)-1];
        dp[len(nums)-2] = nums[len(nums)-2];
        for i in range(len(nums)-3,-1,-1):
            dp[i]= nums[i]+max(dp[i+2],dp[i+3]);
        # print(dp);    
        return max(dp[0],dp[1]);


        