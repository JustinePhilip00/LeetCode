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
        res=set();
        count =0;
        l=0;r=0;
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l]);
                l=l+1;
            res.add(s[r]);
            count = max(count, r-l+1);
        return count; 



        