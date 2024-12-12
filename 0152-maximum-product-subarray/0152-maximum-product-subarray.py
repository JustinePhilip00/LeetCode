class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res= max(nums);
        maximum = 1;
        minimum = 1; 
        for num in nums:
            if num ==0:
                maximum = 1;
                minimum = 1;
                continue;
            temp = maximum*num;
            maximum = max(maximum * num,minimum *num, num);
            minimum = min( temp , minimum * num,num) ;
            res = max(res,maximum);
        return res;
