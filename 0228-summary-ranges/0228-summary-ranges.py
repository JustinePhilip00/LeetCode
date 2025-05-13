class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        output = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                output.append(str(start) if start == nums[i - 1] else str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        output.append(str(start) if start == nums[-1] else str(start) + "->" + str(nums[-1]))
        
        return output
            
                
        
        