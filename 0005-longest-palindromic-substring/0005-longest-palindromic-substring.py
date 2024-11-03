class Solution:
    def longestPalindrome(self, s: str) -> str:
        result="";
        length = 0;
        for i in range(len(s)):
            #when s is odd 
            left=i;
            right=i;
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1) > length:
                    result=s[left:right+1];
                    length = right-left+1;
                left=left-1;
                right=right+1;
            
            #when s is even
            left=i;
            right=i+1;
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1) > length:
                    result=s[left:right+1];
                    length = right-left+1;
                left=left-1;
                right=right+1;
            
        return result;
        
        
        