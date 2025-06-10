class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0;
        r=0;
        myset=set();
        maxlength =0;
        while r<len(s):
            if s[r] not in myset:
                myset.add(s[r]);
                maxlength = max(maxlength, r-l+1);
                r=r+1;
            else:
                myset.remove(s[l]);
                l=l+1;
        return maxlength;



        