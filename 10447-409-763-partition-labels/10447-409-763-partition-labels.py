class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {};
        for i, c in enumerate(s):
            lastindex[c]=i;
        
        res = [];
        currSize = 0;
        end = 0;
        for i, c in enumerate(s):
            currSize= currSize+1;
            end = max(end,lastindex[c]);

            if i == end:
                res.append(currSize);
                currSize = 0;
        return res;