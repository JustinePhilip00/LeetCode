class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # one way
        currSum = 0;
        maxSum =nums[0];
        for num in nums:
            if currSum <0:
                currSum =0;
            currSum = currSum+num;
            maxSum = max(maxSum,currSum);
        return maxSum;


# #         2nd way
#         currSum = nums[0];
#         maxSum = nums[0];
#         for num in nums[1:]:
#             currSum = max(num,currSum+num );
#             maxSum = max(currSum,maxSum);
#         return maxSum;