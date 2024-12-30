class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [];
        output = [];
        def dfs(i):
            
            if i>=len(nums):
                result.append(output.copy());
                return;
            output.append(nums[i]);
            dfs(i+1);
            output.pop();
            dfs(i+1);
        dfs(0);
        return result;