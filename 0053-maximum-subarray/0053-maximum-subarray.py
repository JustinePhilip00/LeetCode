class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0;
        maxSub = nums[0];
        for num in nums:
            if currSum < 0:
                currSum = 0 ;
            currSum = currSum +num;
            maxSub = max(maxSub, currSum);
        return maxSub;
        