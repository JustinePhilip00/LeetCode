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
        res = set();
        val = 0 ;
        l=r=0;
        for r in range(0, len(s)):
            while s[r] in res:
                res.remove(s[l]);
                l=l+1;
            res.add(s[r]);
            val = max(val, r-l+1);
        return val;



        