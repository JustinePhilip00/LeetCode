class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {};
        elements = [[] for i in range(len(nums)+1)];
        output = []; 
        for n in nums:
            count[n]= 1+count.get(n,0);
        for num,count in count.items():
            elements[count].append(num);
        
        for i in range (len(elements)-1, 0, -1):
            for num in elements[i]: 
                output.append(num);
                if len(output)==k:
                    return output;
            
            
        