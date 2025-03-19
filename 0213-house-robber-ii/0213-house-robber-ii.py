class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0];
        if len(nums) == 2:
            return max(nums[0],nums[1]);
        return max(nums[0],self.helper(nums[1:len(nums)]), self.helper(nums[0:len(nums)-1]));
    
    def helper(self,nums):
        rob1=0;
        rob2=0;
        for num in nums:
            temp = max(rob1+num,rob2);
            rob1 =rob2;
            rob2 = temp;
        return rob2;
    
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
#         return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]));
    
#     def helper(self, nums):
#         dp = [0]*(len(nums)+1);
#         dp[len(nums)-1] = nums[len(nums)-1];
#         dp[len(nums)-2] = nums[len(nums)-2];
#         for i in range(len(nums)-3,-1,-1):
#             dp[i]= nums[i]+max(dp[i+2],dp[i+3]);
        
#         # print(dp);    
#         return max(dp[0],dp[1]);
