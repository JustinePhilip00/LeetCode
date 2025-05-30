class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output =[];
        curr=[];
        def dfs(i,curr,total):
            if i>=len(candidates) or total > target:
                return;
            if total == target:
                output.append(curr.copy());
                return;
            curr.append(candidates[i]);
            dfs(i,curr,total+candidates[i]);
            curr.pop();
            dfs(i+1,curr,total);
        dfs(0,[],0);
        return output;
        

        