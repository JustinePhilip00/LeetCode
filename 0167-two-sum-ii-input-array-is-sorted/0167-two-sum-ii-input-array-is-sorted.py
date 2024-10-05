class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = [];
        ptr1=0;
        ptr2=len(numbers)-1;
#         if numbers[ptr1]+numbers[ptr2] > target:
#             ptr2=ptr2-1;
#         elif numbers[ptr1]+numbers[ptr2] < target:
#             ptr1=ptr1+1;
#         else:
#             result.append(ptr1+1);
#             result.append(ptr2+1);
        while ptr1 < ptr2:
            if numbers[ptr1]+numbers[ptr2]==target:
                result.append(ptr1+1);
                result.append(ptr2+1);
            
            if numbers[ptr1]+numbers[ptr2] > target:
                ptr2=ptr2-1;
            else:
                ptr1=ptr1+1;
        
        return result;
            
            
            
        