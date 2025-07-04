class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result=[]
        # hashmap={};
         # O(n^2) runtime
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             result.append(i);
        #             result.append(j);
        
        #Runtime O(n)
        mymap={};
        for i, num in enumerate(nums):
            if target - num not in mymap:
                mymap[num] = i;
            else:
                return [i, mymap[target - num]];


    
        
        # return result;
                    
                    
            
                