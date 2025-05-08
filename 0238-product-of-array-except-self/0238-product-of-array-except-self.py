class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = [1]*len(nums);
        # for i in range(1,len(nums)):
        #     output[i]= output[i-1]*nums[i-1];
        # postfix =1;
        # for i in range(len(nums)-1,-1,-1):
        #     output[i]= output[i]*postfix;
        #     postfix = postfix*nums[i];
        
        # return output;

        # division method
        product = 1;
        result =[];
        zeroCount = 0;
        for num in nums:
            if num != 0:
                product = product * num;
            else:
                product = product *1;
                zeroCount = zeroCount + 1;
        if zeroCount > 1:
            return [0] * len(nums)
        print(product);
        for num in nums:
            if num == 0:
                result.append(product);
            elif zeroCount == 0:
                result.append(int(product/num));
            else:
                result.append(0);
            
        return result;
        