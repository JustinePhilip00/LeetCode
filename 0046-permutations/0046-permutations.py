class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res=[];

        # permutation=[];
        # def dfs(used):
        #     if len(permutation)==len(nums):
        #         res.append(permutation.copy());
        #         return;
        #     for i in range(len(nums)):
        #         if not used[i]:
        #             used[i]=True;
        #             permutation.append(nums[i]);
        #             dfs(used);
        #             permutation.pop();
        #             used[i]=False;
        # dfs([False]*len(nums));
        # return res;
        if len(nums)==0:
            return [[]];
        perms = self.permute(nums[1:]);
        res=[];
        for p in perms:
            for i in range(len(p)+ 1):
                p_copy = p.copy();
                p_copy.insert(i,nums[0]);
                res.append(p_copy);
        return res;

