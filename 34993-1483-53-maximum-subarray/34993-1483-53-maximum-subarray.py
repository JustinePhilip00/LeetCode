class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # one way
        curSum = 0 ;
        maxSum = nums[0];
        for num in nums:
            if curSum < 0:
                curSum = 0;
    
            curSum =curSum + num;
            maxSum = max(maxSum, curSum);
        return maxSum;


# #         2nd way
#         currSum = nums[0];
#         maxSum = nums[0];
#         for num in nums[1:]:
#             currSum = max(num,currSum+num );
#             maxSum = max(currSum,maxSum);
#         return maxSum;