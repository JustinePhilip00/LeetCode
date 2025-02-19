class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0;
        l=0;
        r=0;
        while r<len(nums)-1:
            farthest = 0;
            for i in range (l,r+1):
                farthest = max(farthest, i+nums[i]);
            l=r+1;
            r=farthest;
            jumps=jumps+1;
        return jumps;