class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[0];
        if n==0:
            return res;
        res.append(1);
        curr=1;
        for i in range(2,n+1):
            curr=curr*2;
            for j in range(len(res)-1,-1,-1):
                res.append(curr+res[j]);
        return res;