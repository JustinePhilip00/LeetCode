class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]));
    
    def helper(self, nums):
        dp = [0]*(len(nums)+1);
        dp[len(nums)-1] = nums[len(nums)-1];
        dp[len(nums)-2] = nums[len(nums)-2];
        for i in range(len(nums)-3,-1,-1):
            dp[i]= nums[i]+max(dp[i+2],dp[i+3]);
        
        # print(dp);    
        return max(dp[0],dp[1]);
