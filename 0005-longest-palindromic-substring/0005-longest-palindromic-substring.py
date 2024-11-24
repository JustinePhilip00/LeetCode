class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "";
        resLength = 0;
        
        for i in range(len(s)):
            l=i;
            r=i;
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLength < r-l+1:
                    res = s[l:r+1];
                    resLength = r-l+1;
                l=l-1;
                r=r+1;
                
        for i in range(len(s)):
            l=i;
            r=i+1;
            while l>=0 and r<len(s) and s[l]==s[r]:
                if resLength < r-l+1:
                    res = s[l:r+1];
                    resLength = r-l+1;
                l=l-1;
                r=r+1;
        return res;
            
        
        
        