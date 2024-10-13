class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0;
        j = len(nums)-1;
        res= nums[0];
        while i<=j:
            if nums[i]<nums[j]:
                res=min(res,nums[i]);
                break;
            mid = (i+j)//2;
            res= min(nums[mid],res);
            if nums[mid] >= nums[i]:
                i = mid+1;
            else: 
                j= mid-1;
            
      
        return res;
                
            
                
        