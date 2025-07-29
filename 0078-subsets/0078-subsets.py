class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output =[];
        res =[];
        def dfs(i):
            if i >= len(nums):
                output.append(res.copy());
                return;
            res.append(nums[i]);
            dfs(i+1);
            res.pop();
            dfs(i+1);
        dfs(0);
        return output;