class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mymap={};
        l=0;
        res = 0;
        for r in range(0,len(s)):
            mymap[s[r]] = 1+mymap.get(s[r],0);
            while (r-l+1)-max(mymap.values()) > k:
                mymap[s[l]] = mymap[s[l]]-1;
                l=l+1;
            res = max(res,r-l+1);
        return res;

        