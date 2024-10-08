class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0;
        longest_substring = 0;
        mymap = {};
        for r in range(len(s)):
            
            mymap[s[r]] = 1+mymap.get(s[r],0);
            if ((r-l+1) - max(mymap.values()) > k ):
                mymap[s[l]] = mymap[s[l]]-1;
                l=l+1;
        
        longest_substring = max(longest_substring, r-l+1);
        return longest_substring;
        
            
        