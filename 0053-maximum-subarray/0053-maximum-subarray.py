class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # one way
        maxSub= nums[0];
        curSum =0;
        for i in range (0,len(nums)):
            if curSum <0:
                curSum =0;
            curSum = curSum + nums[i];
            maxSub = max(maxSub, curSum);
        return maxSub;
# #         2nd way
#         currSum = nums[0];
#         maxSum = nums[0];
#         for num in nums[1:]:
#             currSum = max(num,currSum+num );
#             maxSum = max(currSum,maxSum);
#         return maxSum;