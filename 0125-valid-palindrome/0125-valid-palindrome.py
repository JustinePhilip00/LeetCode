class Solution:
    def isPalindrome(self, s: str) -> bool:
        output="";
        
        if len(s)==1 or len(s)==0:
            return True;
        for ch in s:
            if ch.isalnum():
                output=output+ch.lower();
        
        ptr1=0;
        ptr2=len(output)-1;
        while ptr1<= ptr2:
            if output[ptr1]!=output[ptr2]:
                return False;
            ptr1=ptr1+1;
            ptr2=ptr2-1;
        
        return True;
                
            
        
            
        
        
            