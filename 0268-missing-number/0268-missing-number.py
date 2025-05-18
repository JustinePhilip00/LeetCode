class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set(nums);
        n = len(nums);
        for i in range(n+1):
            if i not in myset:
                return i;
        