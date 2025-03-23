class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr="";
        for ch in s:
            if ch.isalnum():
                newstr= newstr+ch;
        newstr= newstr.lower();
        l=0;
        r=len(newstr)-1;
        while l<r:
            if newstr[l]!=newstr[r]:
                return False;
            l=l+1;
            r=r-1;
        return True;
            
        
            
        
        
            