class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0;
        r = len(height)-1;
        maxArea = 0;
        currArea =0;
        while l<r and r<len(height):
            currArea = (min(height[l],height[r]))*(r-l);
            maxArea = max(maxArea, currArea);
            if height[l]<height[r]:
                l = l+1;
            else:
                r=r-1;
        return maxArea;
