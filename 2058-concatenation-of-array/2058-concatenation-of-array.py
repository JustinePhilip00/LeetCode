class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = 2* len(nums);
        # ans =[0]*n;
        # for i in range(len(nums)):
        #     ans[i] = nums[i];
        #     ans[i+len(nums)] = nums[i];
        # return ans;
        return nums+nums;

