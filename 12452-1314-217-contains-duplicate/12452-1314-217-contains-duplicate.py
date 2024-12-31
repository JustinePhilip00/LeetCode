class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result  = set();
        for i in range(0,len(nums)):
            if nums[i] in result:
                return True;
            else:
                result.add(nums[i]);
        return False;