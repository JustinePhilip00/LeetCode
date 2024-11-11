class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0;
#         num_set= set(nums);
#         highest_length = 0;
        
#         for num in num_set:
#             if num-1 not in num_set:
#                 current_length= 0 ;
#                 while (num+current_length) in num_set:
#                     current_length=current_length+1;
#                     highest_length = max(highest_length,current_length);
        
#         return highest_length;
        if not nums:
            return 0;    
        myset=set(nums);
        maxlength=0;
        for num in myset:
            if num-1 not in myset:
                currlength =0;
                while (num+currlength) in myset:
                    currlength=currlength+1;
                    maxlength = max(currlength, maxlength);
        return maxlength;
                    
                
            
            
        
            
            
        
        