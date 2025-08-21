class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower();
        newS =""
        for ch in s:
            if ch.isalnum():
                newS = newS+ch;
        l =0;
        r= len(newS)-1;
        while l<=r:
            if newS[l]!=newS[r]:
                return False;
            l=l+1;
            r=r-1;
        return True
            
        
            
        
        
            