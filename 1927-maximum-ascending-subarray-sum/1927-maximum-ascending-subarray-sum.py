class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curMax =nums[0];
        maxSum =nums[0];
        for i in range( 1, len(nums)):
            if nums[i] > nums[i-1]:
                curMax = curMax + nums[i];
            else:
                curMax = nums[i];
            maxSum = max(curMax,maxSum);
        return maxSum;
