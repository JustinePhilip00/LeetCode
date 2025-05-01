class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         outputset= set();
#         maxLength = 0;
#         i=0;
#         j=0;
#         while j<len(s):
#                 if s[j] not in outputset:
#                     outputset.add(s[j]);
#                     maxLength = max(maxLength, j-i+1);
#                     j=j+1;
#                 else:
#                     outputset.remove(s[i]);
#                     i=i+1;
#         print(outputset);            
#         return maxLength;
        myset = set();
        l=0;
        r=0;
        maxlen = 0;
        while r < len(s):
            if s[r] not in myset:
                myset.add(s[r]);
                maxlen=max(maxlen, r-l+1)
                r=r+1;
            else:
                myset.remove(s[l]);
                l=l+1;
        return maxlen;



        