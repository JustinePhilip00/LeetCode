class Solution:
    def canJump(self, nums: List[int]) -> bool:
        endpoint = len(nums)-1;
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= endpoint:
                endpoint = i;
        return True if endpoint==0 else False;


