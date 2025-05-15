class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # one way
        maxSub = nums[0];
        currSum = 0;
        for num in nums:
            if currSum <0:
                currSum =0;
            currSum = currSum+num;
            maxSub = max(currSum, maxSub);
        return maxSub;


# #         2nd way
#         currSum = nums[0];
#         maxSum = nums[0];
#         for num in nums[1:]:
#             currSum = max(num,currSum+num );
#             maxSum = max(currSum,maxSum);
#         return maxSum;