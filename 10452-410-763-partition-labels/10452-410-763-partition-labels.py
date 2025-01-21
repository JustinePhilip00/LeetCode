class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mydict = {};
        for i,ch in enumerate(s):
            mydict[ch] = i;
        res = [];
        size =0 ;
        end = 0;
        for i,ch in enumerate(s):
            size = size +1;
            end = max(end,mydict[ch]);
            if i==end:
                res.append(size);
                size= 0;
        return res;