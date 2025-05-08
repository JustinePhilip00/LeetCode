class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time complexity alogorithm with O(1) space complexity 
        res =[1]*len(nums);
        prefix = 1;
        for i in range(len(nums)):
            res[i] = prefix;
            prefix = prefix *nums[i];
        postfix=1;
        for j in range(len(nums)-1,-1,-1):
            res[j] = res[j] * postfix;
            postfix = postfix * nums[j];

        return res;

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
        